$(document).ready(function() {

	$.ajax({
		url: "menu.php",
			
		success: function(result) {
			$("#menu-container").html(result);
		},
		
		error: function(xhr, status, error) {
			$("#menu-container").html("Error loading the menu:<br>xhr: " + xhr + "<br>status: " + status + "<br>error: " + error);
			$("body").css("margin-top", 50);
		}
	});
	
});
