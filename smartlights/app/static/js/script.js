
var lightToggleApi = '/api/v1/lights';

var toggleOutlet = function (buttonClicked) {

    var lightId =  buttonClicked.attr('data-outletId');
    var action = buttonClicked.attr('data-outletStatus');
    var jsonDataStr = ""; // No data in request body

    $.ajax({
        type: "PUT",
        url: lightToggleApi + "/" + lightId + "/" + action,
        contentType: "application/json",
        data: jsonDataStr,
        success: function (data, status) {
            alert(lightId + " " + action);
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("jqXHR statusCode" + jqXHR.statusCode());
            console.log("textStatus " + textStatus);
            console.log("errorThrown " + errorThrown);
        }
    });
};

$(function () {
    $('.toggleOutlet').click(function () {
        toggleOutlet($(this));
    });
});

$(document).ready(function(){
	$(".nav a").on("click", function(){
		$(".nav").find(".active").removeClass("active");
		$(this).parent().addClass("active");
	});
});
