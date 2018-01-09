$(function(){
	$('#btnDelete').click(function(){
		
		$.ajax({
			url: '/delete',
			type: 'GET',
			success: function(response){
				$("#respuesta1").html("Modelo reiniciado");
			},
			
		});
	});
});
