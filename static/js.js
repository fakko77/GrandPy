var bt = document.getElementById('bt')
let map;
//Send txt
function myFunction() {
	const a = document.getElementById("msg").value;
	var div = document.getElementById('mine messages');
	var para = document.createElement("div");
	para.setAttribute("class", "message last");
	var node = document.createTextNode(a);
	para.appendChild(node);
	div.appendChild(para);
}

function namecaller(){
      $.getJSON($SCRIPT_ROOT + '/requestAjax',
    {
      msg: $('input[name="msg"]').val(),
    },
    function(data,status){
      $("#result").text(data.result);
	  initMap(data.lat, data.lng)
    });
}



function xx() {
    myFunction();
    document.getElementById('spinner-border').style.display = "block";
    document.getElementById('result').style.display = "none";
    setTimeout(function(){
    document.getElementById('spinner-border').style.display = "none";
    }, 5000);
    setTimeout(function(){
     document.getElementById('result').style.display = "block";
    }, 6000);
    setTimeout(namecaller,7000)
}


//Google map
function initMap(a, b) {
	if (a == null) {
		map = new google.maps.Map(document.getElementById("map"), {
			center: {
				lat: 48.856614,
				lng: 2.3522219
			},
			zoom: 8
		});
	} else {
		map = new google.maps.Map(document.getElementById("map"), {
			center: {
				lat: a,
				lng: b
			},
			zoom: 8
		});
		var myLatLng = {
			lat: a,
			lng: b
		};
		var marker = new google.maps.Marker({
			position: myLatLng,
			map: map
		});
	}
}



document.addEventListener("keydown", function(event) {
    if (event.keycode == 13){
        xx();
    }

})

//Ajax Request send/receive

//
// $(function() {
//	$('#bt').bind('click', function () {
//		$.getJSON($SCRIPT_ROOT + '/requestAjax', {
//			msg: $('input[name="msg"]').val(),
//		}, function (data) {
//
//			$("#result").text(data.result);
//			initMap(data.lat, data.lng)
//		});
//		return false;
//	});
//	$(document).on('keypress', function (e) {
//
//		if (e.which == 13) {
//		    myFunction()
//			$.getJSON($SCRIPT_ROOT + '/requestAjax', {
//				msg: $('input[name="msg"]').val(),
//			}, function (data) {
//			    console.log("ici");
//				$("#result").text(data.result);
//				initMap(data.lat, data.lng)
//			});
//			return false;
//		}
//	});
//});
