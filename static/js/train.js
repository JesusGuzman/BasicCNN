$(function(){
	$('#btnTrain').click(function(){
		
		$.ajax({
			url: '/train',
			type: 'GET',
                        cache: false,
			success: function(response){
                                $("#respuesta").html("Modelo entrenado");
			},
			
		});
	});
});
