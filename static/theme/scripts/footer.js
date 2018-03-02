require(["jquery","tmpl","geturlparam"],function($){ 	

$(document).ready(function(e){

	var footer_article = $('#footer_article'),
		article_nav=$('div#article_nav');


	$.post('/common/get_article',function(data){
		var data = $.parseJSON(data);
		
		if(footer_article.length){
			$.tmpl($('#footer_tmpl').html(),data.data).appendTo(footer_article);
		}
		if(article_nav.length){			
			$.tmpl($('#articlenav_tmpl').html(),data.data).appendTo(article_nav);
		}

		
	});

	var wechater = $('a#wechater'),
		wechatqrcode = $('div.wechatqrcode');

	wechater.mouseenter(function() {
		wechatqrcode.show();
	}).mouseleave(function() {
		wechatqrcode.slideUp('fast');
	});




});

});