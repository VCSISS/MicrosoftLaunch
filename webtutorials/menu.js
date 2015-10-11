$(document).ready(function() {

	$.ajax({
		url: "menu.php",
			
		success: function(result) {
			$("#menu-container").html(result);
		},
		
		error: function(xhr, status, error) {
			alert("Error loading the menu:\nxhr: " + xhr + "\nstatus: " + status + "\nerror: " + error);
		}
	});
	
});
