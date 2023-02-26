/* global TrelloPowerUp */
var Promise = TrelloPowerUp.Promise;

var BLACK_ROCKET_ICON = 'https://cdn.glitch.global/345b4a37-e5cb-4b8c-bcd6-71b41bee8341/clock.png?v=1677370074042';

  
// Start adding handlers for your capabilities here!
  TrelloPowerUp.initialize({ 	
    'card-buttons': function(t, options) {
    return t.set("member", "shared", "hello", "world")
    .then(function(){
        return [{
    icon: BLACK_ROCKET_ICON,
          text: 'ReverseChrono',
          callback: function(t) {
            var context = t.getContext();
            var cardID = context["card"];
            var boardID = context["board"];
            var urlString = "test" + "?cardID=" + cardID + "&boardID=" + boardID;
            return t.popup({
              title: "Reverse Checklist Date Order",
              url: urlString, 
              height: 65
            });
          }
        }];
    })
    }
});
