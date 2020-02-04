#!/usr/bin/env python

class AgentDeskSearchMatch(object):

    searches = [

        {"id": 1, "latitude": 12.6787, "longitude": 77.657,"min_price": 14800, "max_price": 20000, "min_bedroom": 2, "max_bedroom": 3, "min_bathroom": 2, "max_bathroom": 3, "distance": 10},
        {"id": 2, "latitude": 12.6787, "longitude": 77.657, "min_price": 10000, "max_price": 14000, "min_bedroom": 2, "max_bedroom": 3, "min_bathroom": 2, "max_bathroom": 3, "distance": 4},
         {"id": 3, "latitude": 12.6787, "longitude": 77.657, "min_price": 12500, "max_price": 20000, "min_bedroom": 2, "max_bedroom": 3, "min_bathroom": 2, "max_bathroom": 3, "distance": 10}
    ]

    def get_search_matches(self):
        for item in self.searches:
            self.get_location_weightage()
            item["location_weight"] = self.fetch_location_weight(item)
            item["price_weight"] = self.get_price_weightage(item)
            item["bedroom_weight"] = self.get_bedroom_weightage(item)
            item["bathroom_weight"] = self.bathroom_weightage(item)
            item["total_weight"] = item["location_weight"] + item["price_weight"] + item["bedroom_weight"]+ item["bathroom_weight"]
        print(self.searches)

    def get_location_weightage(self):
        pass

    def get_price_weightage(self, item):
        price_wt = 0
        if item.get("min_price") and item.get("max_price"):
            price_wt = self.get_min_price_wt(item) + self.get_max_price_wt(item)

        elif item.get("min_price"):
            if self.price - self.price /10 <= item["min_price"] <= self.price + self.price /10:
                price_wt = 30
            else:
                place_wt = self.get_min_price_wt(item)
        else:
            place_wt = self.get_max_price_wt(item)

        return price_wt

    def fetch_location_weight(self, item):
        loc_wt = None
        if 0 <= item["distance"] <= 2:
            loc_wt = 30

        elif 3 <= item["distance"] <= 4:
            loc_wt = 25

        elif 5 <= item["distance"] <= 6:
            loc_wt = 20

        elif 7 <= item["distance"] <= 8:
            loc_wt = 15

        elif 9 <= item["distance"] <= 10:
            loc_wt = 10
        else:
            loc_wt = 0
        return loc_wt

    def get_min_price_wt(self, item):
        if self.price - self.price * 5 / 100 <= item["min_price"]:
            price_wt = 30 / 2
        elif self.price - self.price * 10 / 100 <= item["min_price"]:
            price_wt = 25 / 2
        elif self.price - self.price * 15 / 100 <= item["min_price"]:
            price_wt = 20 / 2
        elif self.price - self.price * 20 / 100 <= item["min_price"]:
            price_wt = 15 / 2
        elif self.price - self.price * 10 / 100 <= item["min_price"]:
            price_wt = 10 / 2
        else:
            price_wt = 0
        return price_wt

    def get_max_price_wt(self, item):
        if self.price + self.price * 5 / 100 >= item["max_price"]:
            price_wt = 30 / 2
        elif self.price + self.price * 10 / 100 >= item["max_price"]:
            price_wt = 25 / 2
        elif self.price + self.price * 15 / 100 >= item["max_price"]:
            price_wt = 20 / 2
        elif self.price + self.price * 20 / 100 >= item["max_price"]:
            price_wt = 15 / 2

        elif self.price + self.price * 25 / 100 >= item["max_price"]:
            price_wt = 10 / 2
        else:
            price_wt = 0
        return price_wt

    def get_bedroom_weightage(self, item):
        bedroom_wt = 0
        if item.get("min_bedroom") and item.get("max_bedroom"):
            bedroom_wt = self.get_min_bedroom_wt(item) + self.get_max_bedroom_wt(item)
        elif item.get("min_bedroom"):
            bedroom_wt = self.bedroom(item)
        else:
            bedroom_wt = self.get_max_bedroom_wt(item)
        return bedroom_wt

    def get_min_bedroom_wt(self, item):
        bedroom_min_wt =0
        if item["min_bedroom"] <= self.bedroom <= item["max_bedroom"]:
            bedroom_min_wt = 20
        elif self.bedroom - 1 == item["min_bedroom"]:
            bedroom_min_wt = 10
        elif self.bedroom -2 == item["min_bedroom"]:
            bedroom_min_wt = 5
        else:
            bedroom_min_wt =0
        return bedroom_min_wt

    def get_max_bedroom_wt(self, item):
        bedroom_max_wt = 0
        if item["max_bedroom"] <= self.bedroom <= item["max_bedroom"]:
            bedroom_min_wt = 20
        if self.bedroom + 1 == item["max_bedroom"]:
            bedroom_max_wt = 10
        elif self.bedroom + 2 == item["max_bedroom"]:
            bedroom_max_wt = 5
        else:
            bedroom_max_wt = 0
        return bedroom_max_wt

    def bathroom_weightage(self, item):
        if item.get("min_bathroom") and item.get("max_bathroom"):
            bathroom_wt = self.get_min_bathroom_wt(item) + self.get_max_bathroom_wt(item)
        elif item.get("min_bathroom"):
            bathroom_wt = self.get_min_bathroom_wt(item)
        else:
            bathroom_wt = self.get_max_bathroom_wt(item)
        return bathroom_wt

    def get_min_bathroom_wt(self, item):
        bathroom_min_wt = 0
        if self.bathroom - 1 == item["min_bedroom"]:
            bathroom_min_wt = 10
        elif self.bathroom - 2 == item["min_bedroom"]:
            bathroom_min_wt = 5
        else:
            bedroom_min_wt = 0
        return bathroom_min_wt

    def get_max_bathroom_wt(self, item):
        bathroom_max_wt = 0
        if self.bathroom - 1 == item["min_bathroom"]:
            bathroom_max_wt = 10
        elif self.bathroom - 2 == item["min_bathroom"]:
            bathroom_max_wt = 5
        else:
            bedroom_min_wt = 0
        return bathroom_max_wt
