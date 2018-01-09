$(function(){
        $("#formuploadajax").on("submit", function(e){
            e.preventDefault();
            var f = $(this);
            var formData = new FormData(document.getElementById("formuploadajax"));
            formData.append("dato", "valor");
            //formData.append(f.attr("name"), $(this)[0].files[0]);
            $.ajax({
                url: "/upload_image",
                type: "post",
                dataType: "json",
                data: formData,
                cache: false,
                contentType: false,
             processData: false
            })
             
                .done(function(res){
                    $("#mensaje").html("Respuesta: " );
                });
            
        });
    });


/*     
   $(function(){ 
       $("#formuploadajax").on("submit", function(){
          var formData = new FormData(document.getElementById("formuploadajax"));
            var formData = new FormData($("#formulario")[0]);
            $.ajax({
                url: '/upload_image',
                type: "POST",
                data: formData,
                contentType: false,
                processData: false,
                success: function(res)
                {
                    $("#destino").html("yes");
                    //$("#destino").load(res);
                }
            });
         });
     });
*/
