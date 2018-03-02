require(["jquery","tmpl","scrollup","geturlparam"],function($){ 
	$.ajaxSetup({
      cache: false,
      type: "POST",
      beforeSend: function (x) {
          x.setRequestHeader("ajax", "true");
      },
      error:function (event, jqXHR, ajaxSettings, thrownError) {          
          var response = $.parseJSON(jqXHR.responseText);     
          alert(response);
             /*
          $( "#dialog-message" ).dialog({
            modal: true,
            title:'提示',
            buttons: [{
              text:"关闭",
              click: function() {
                $( this ).dialog( "close" );
              }
            }]
          }).find('#message-content').text(response);
*/
      }
  });

});