$( document ).ready( function() {

	function Location(name, location) {
	    var self = this;
	    self.name = name;
	    self.location = location;
	}

	function Locations() {
	    var self = this; 
	    self.filter_locations = ko.observable(""); 

	    self.locList = ko.observableArray([]);
	    locations.forEach(function(locItem){
	    	self.locList.push(new Location(locItem.name, locItem.location));
	    });
	    
	    self.apply_filter = function(){
	    	self.locList.removeAll();
	    	locations.forEach(function(locItem){
	    		if (locItem.name.toLowerCase().includes(self.filter_locations().toLowerCase()))
		    		self.locList.push(new Location(locItem.name, locItem.location));
		    });
		    initMap(self.locList(), true);
	    }

	    self.clear_filter = function(){
	    	self.filter_locations(""); 
	    	self.locList.removeAll();
	    	locations.forEach(function(locItem){
		    	self.locList.push(new Location(locItem.name, locItem.location));
		    });
		    initMap(self.locList(), true);
	    }

	    this.clicked_location = function(loc){
	    	initMap([loc], true, true);
	    }
	}

	ko.applyBindings(new Locations());
});