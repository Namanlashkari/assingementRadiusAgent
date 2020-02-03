Detailed discussion on Quadtree approach:


	The first thing we need to get out of the way is 
	the cost of the point-in-polygon check (I like to 
	call it the polygon inclusion query). Thetwo 
	common algorithms used for polygon inclusion; ray 
	casting and the winding number. Both algorithms 
	need to compare the query point to every vertex 
	of the polygon, so their efficiency is a function 
	of the number of vertices. If we break down the 
	problem using Uber’s city-centric model

	Ray casting:


	Winding number:


	we end up with a few variables that we can use for our analysis.

		q := Point Query

		C := Number of cities

		V := Number of vertices that define a city boundary

		n := Number of fence polygons in a city

		v := Number of vertices in a fence polygon 




Augmented Brute Force:


	Uber augmented the brute force approach by first 
	checking which city the point is in, then going 
	through the fences in that individual city. This 
	effectively trims the search space by an order of 
	however many cities the data had. The cost of 
	comparing the query point to every point in the 
	city boundary still needs to be account for. In 
	this two stage approach, here’s what we get:


	Abrute() -> O(CV) + O(nv)



Overview of Quadtree:

	A quadtree is a specialization of a generic 
	kd-tree for 2-dimensional indexing. Basically you 
	take a flat projection of your search space and 
	divide it into quarters that we’ll call cells. 
	You then divide each of those cells into quarters 
	recursively until you hit a defined maximum depth 
	which will be the leaves of the tree. If we take 
	a mercator projection of the Earth and label each 
	of the cells by appending an identifier to the 
	parent label we can leverage a quadtree structure 
	to create a tiling system fast geospatial 
	searches like Bing Maps does/did.Bing Maps 
	provides a world map that users can directly 
	manipulate to pan and zoom. To make this 
	interaction as fast and responsive as possible, 
	we chose to pre-render the map at many different 
	levels of detail, and to cut each map into tiles 
	for quick retrieval and display.


	Qtree() -> O(T) + O(v) 



	We could use bounding boxes to avoid many of the 
	expensive point-in-polygon queries.Applying a 
	bounding box check to their algorithm gets us on 
	the same order of magnitude as the spatial 
	indexes.


	It’s evident that the majority of the work in the 
	brute force family of fences is done in 
	searching, while the spatial indexes are 
	serializing more data and responding to more 
	requests.


Spatial indexing:
	
	It is an increasingly important area of 
	geo-spatial application design.The entities Uber 
	rides, Facebook users) and associated meta-data 
	are stored in traditional tables and a spatial 
	index is built separately with the coordinates 
	of the entities. The spatial index allows 
	special geometric queries to be executed 
	efficiently.
	
	Geo-distance Range Queries:
		These queries help retrieve entities 
		within a specified range. Some use-cases 
		include finding all cabs within a 2km 
		radius from a user’s location. Yeah, 
		Uber comes to mind here.
		A properly designed spatial indexing 
		scheme is a central part of building 
		high performance geo-apps.


Algorithm:

	def getPointsInRange(root, range):
    	points = []
    	# If there is no intersection with the
    	area, return
    	if not root.intersect(range):
        	return points
    	# Return all data points on a leaf node
    	if root.isLeaf():
        	points.append(root.getNodes())
        	return points
    	# Recursively append the points from the 
    	4 quadrants
    	points.append(getPointsInRange(root.northwest, range))
    	points.append(getPointsInRange(root.northeast, range))
    	points.append(getPointsInRange(root.southeast, range))
    	points.append(getPointsInRange(root.southwest, range))
    	return points
