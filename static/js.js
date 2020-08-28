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

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

function spinner(txt) {
	document.getElementById("result").innerHTML = txt;
}
//Ajax Request send/receive

 $(function Test () {
	$('#bt').bind('click', function () {
		$.getJSON($SCRIPT_ROOT + '/requestAjax', {
			msg: $('input[name="msg"]').val(),
		}, function (data) {

			$("#result").text(data.result);
			initMap(data.lat, data.lng)
		});
		return false;
	});
	$(document).on('keypress', function (e) {

		if (e.which == 13) {
		    myFunction()
			$.getJSON($SCRIPT_ROOT + '/requestAjax', {
				msg: $('input[name="msg"]').val(),
			}, function (data) {
			    console.log("ici");
				$("#result").text(data.result);
				initMap(data.lat, data.lng)
			});
			return false;
		}
	});
});