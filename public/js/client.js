/* global TrelloPowerUp */

var Promise = TrelloPowerUp.Promise;

var BLACK_ROCKET_ICON = 'https://cdn.glitch.global/8337a74e-0496-4e24-8c29-0717ecda77d1/bread.png?v=1677247874887';

TrelloPowerUp.initialize({
  // Start adding handlers for your capabilities here!
	'card-buttons': function(t, options) {
	return t.set("member", "shared", "hello", "world")
	.then(function(){
		  return [{
	icon: BLACK_ROCKET_ICON,
			  text: 'ChronoReverse',
	      callback: function(t) {
	        return t.popup({
	          title: "Put Checklists in Reverse Chronological Order",
	          url: "test.py",
	        });
	      }
		  }];
	})
	},
});
