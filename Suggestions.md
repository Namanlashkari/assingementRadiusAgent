Here are a few suggestions for resulting in an more optimal result generating architecture 


Using better and tested languages such as GO for the following reason:

    High-throughput and low-latency requirements: 
      Geofence lookups are required on every request from Uber’s mobile apps and must quickly (99th percentile < 100 
      milliseconds) answer a high rate (hundreds of thousands per second) of queries.
    
    CPU intensive workload: 
      Geofence lookups require CPU-intensive point-in-polygon algorithms. While Node.js works great for our other services 
      that are I/O intensive, it’s not optimal in this use case due to Node’s interpreted and dynamic-typed nature.
    
    Non-disruptive background loading: 
      To ensure we have the freshest geofences data to perform the lookups, this service must keep refreshing the in-memory   
      geofences data from multiple data sources in the background. Because Node.js is single threaded, background refreshing 
      can tie up the CPU for an extended period of time (e.g., for CPU-intensive JSON parsing work), causing a spike in query 
      response times. This isn’t a problem for Go, since goroutines can execute on multiple CPU cores and run background jobs 
      in parallel with foreground queries.




Ray casting algorithm

    The number of intersections for a ray passing from the exterior of the polygon to any point; if odd, it shows that the 
    point lies inside the polygon. If it is even, the point lies outside the polygon; this test also works in three 
    dimensions.
    One simple way of finding whether the point is inside or outside a simple polygon is to test how many times a ray, 
    starting from the point and going in any fixed direction, intersects the edges of the polygon. If the point is on the 
    outside of the polygon the ray will intersect its edge an even number of times. If the point is on the inside of the 
    polygon then it will intersect the edge an odd number of times. This method won't work if the point is on the edge of the 
    polygon.



To Geo Index or Not: 

    Given a location specified as a lat/lon pair, how do we find which of our many tens of thousands of geofences this 
    location falls into? The brute-force way is simple: go through all the geofences and do a point-in-poly check using an 
    algorithm, like the ray casting algorithm. But this approach is too slow. So how do we narrow down the search space 
    efficiently?

    Instead of indexing the geofences using R-tree or the complicated S2, we chose a simpler route based on the observation 
    that Uber’s business model is city-centric; the business rules and the geofences used to define them are typically 
    associated with a city. This allows us to organize the geofences into a two-level hierarchy where the first level is the 
    city geofences (geofences defining city boundaries), and the second level is the geofences within each city.

    For each lookup, we first find the desired city with a linear scan of all the city geofences, and then find the containing 
    geofences within that city with another linear scan. While the runtime complexity of the solution remains O(N), this 
    simple technique reduced N from the order of 10,000s to the order of 100s.



Spark uses :
   
    Resilient Distributed Datasets (RDD)to perform parallel processing across a cluster or computer processors. ... Spark 
    applications consist of a driver process and executor processes. Briefly put, the driver process runs the main function, 
    and analyzes and distributes work across the executors.


