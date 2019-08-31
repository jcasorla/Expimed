$(document).ready(function(){
    console.log("in js file");
    $('#username').keyup(function(){
        var data = $("#regForm").serialize();  // capture all the data in the form in the variable data
        console.log(data);
        $.ajax({
            method: "POST",   // we are using a post request here, but this could also be done with a get
            url: "/username",
            data: data
        })
        .done(function(res){
            console.log(res);
            $('#usernameMsg').html(res); // manipulate the dom when the response comes back
        });
    });
});