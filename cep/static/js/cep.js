$(document).ready(function(){
	$(".zip-field").blur(function(){
		function getHTTPObject() {
		  var xmlhttp;
		  /*@cc_on
		  @if (@_jscript_version >= 5)
		    try {
		      xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
		      } catch (e) {
		      try {
		        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		        } catch (E) {
		        xmlhttp = false;
		        }
		      }
		  @else
		  xmlhttp = false;
		  @end @*/
		  if (!xmlhttp && typeof XMLHttpRequest != 'undefined') {
		    try {
		      xmlhttp = new XMLHttpRequest();
		      } catch (e) {
		      xmlhttp = false;
		      }
		    }
		  return xmlhttp;
		}
		var http = getHTTPObject();

        http.open("GET", '/address/'+$(".zip-field").val()+'/', true);
    	http.onreadystatechange = handleHttpResponse;
		http.send(null);

		var arr; //array with return data

		function handleHttpResponse() 
	    {
			if (http.readyState == 4) 
			{
				var response = http.responseText;
				eval("var arr = "+response); //creates object with json info
				$("#"+address.street).val(arr.street);
				$("#"+address.district).val(arr.district);
				$("#"+address.city).val(arr.city);
				$("#"+address.state).val(arr.state);
			}
		}
	})
});