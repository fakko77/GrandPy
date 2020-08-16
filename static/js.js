var bt=document.getElementById('bt')
let map;
function myFunction() {
  const a = document.getElementById("msg").value;
  var div = document.getElementById('mine messages');
  var para = document.createElement("div");
  para.setAttribute("class", "message last");
  var node = document.createTextNode(a);
  para.appendChild(node);
  div.appendChild(para);
}
function initMap(a,b) {
   if(a == null ){
    map = new google.maps.Map(document.getElementById("map"), {
         center: {
          lat: 48.856614,
          lng: 2.3522219
         },
          zoom: 8
        });
    }else{
       map = new google.maps.Map(document.getElementById("map"), {
         center: {
         lat: a,
         lng: b
        },
         zoom: 8
       });
       var myLatLng = {lat: a,lng: b};
       var marker = new google.maps.Marker({position: myLatLng, map: map});
      }
     }
$(function() {
  $('#bt').bind('click', function() {
    $.getJSON($SCRIPT_ROOT + '/requestAjax', {
      msg: $('textarea[name="msg"]').val(),
    }, function(data) {
      $("#result").text(data.result);
//      $('div[name="botmsg"]').append('<div class="mine message">' + data.result + '</div>');
      initMap(data.lat,data.lng)
    });
    return false; 
  });
});

