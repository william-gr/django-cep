$(document).ready(function(){
    $(".zip-field").blur(function(){
        var arr;
        $.get('/address/'+$(".zip-field").val()+'/', function(data,status)
        {
            eval("var arr = "+data);
            $("#"+address.street).val(arr.street);
            $("#"+address.district).val(arr.district);
            $("#"+address.city).val(arr.city);
            $("#"+address.state).val(arr.state);
        });
    })
});
