$(".reply-form").hide();
$(document).ready(function(){

	$(".reply-form").hide();

	$("#subscribe").click(function(){
		var email=$(".email").val();
		
		if(email=="")
			 alert("Invalid e-mail");
        
        else
		
			$.ajax({
				type:'POST',
				headers: {
      				'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'),
   						},
				url: "/subscribe",
				data: {
   						'email_ID':email,
   						
   						},
				success: function(data){
					$(".abc").html(data);
					}
				
		});
	});

	$("#comment").click(function(){
		var name=$(".name").val();
		var email=$(".email").val();
		var comment=$(".comment").val();
		var id=$(".abc").val();

		if(name==""||email==""||comment=="")
			 alert("Enter all fields");
        
        else
        {
			
			$.ajax({
				type:'POST',
				headers: {
      				'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'),
   						},
				url: "/comment",
				data: { 
					    'name':name,
   						'email_ID':email,
   						'reply':reply,
   						'id':id,

   					  },
				success: function(data){
						$(".xyz").html(data);
					}
				
				});
		}
	});

	$(".reply-btn").click(function(){
		var comment_id=$(this).attr('id');
		console.log(comment_id);
		$("#"+comment_id+".reply-form").show();
	});

	$(".reply-submit").click(function(){
		var comment_id=$(this).attr('id');
		var name=$("#"+comment_id+".reply_name").val();
		var email=$("#"+comment_id+".reply_email").val();
		var reply=$("#"+comment_id+".reply").val();

		
		if(name==""||email==""||reply=="")
			 alert("Enter all fields");
        
        else
        {
			
			$.ajax({
				type:'POST',
				headers: {
      				'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content'),
   						},
				url: "/reply",
				data: { 
					    'name':name,
   						'email_ID':email,
   						'reply':reply,
   						'id':comment_id,
   					},
				success: function(data){
						$(".pqr").html("name:"+name+"email:"+email+"reply:"+reply);
					}
				
				});
		}
	

	});
})