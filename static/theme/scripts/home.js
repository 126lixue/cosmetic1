require(["jquery","tmpl","lazyload","featureList"],function($){   
	var 
		json = $('div#homedata').text(),
		data = $.parseJSON(json);

	if(data.outbreak!==false){
		$.tmpl($('#outbreak_tmpl').html(),data.outbreak).appendTo('#outbreak');
	}
	 
	if(data.group!==false){
		$.tmpl($('#group_tmpl').html(),data.group).appendTo('#group_list');
	}

	$.tmpl($('#slidelist_tmpl').html(),data.slider).appendTo('ul#slide_list');
	$.tmpl($('#slideindex_tmpl').html(),data.slider).appendTo('ul#slide_index');

	$.tmpl($('#brandshow_tmpl').html(),data.brand_ea).appendTo('ul.brand_ea');
	$.tmpl($('#brandshow_tmpl').html(),data.brand_jp).appendTo('ul.brand_jp');
	$.tmpl($('#brandshow_tmpl').html(),data.brand_kr).appendTo('ul.brand_kr');
	$.tmpl($('#brandshow_tmpl').html(),data.brand_cn).appendTo('ul.brand_cn');
	$.tmpl($('#brandshow_tmpl').html(),data.brand_other).appendTo('ul.brand_other');
	$.tmpl($('#brandshow_tmpl').html(),data.brand_recommend).appendTo('ul.brand_recommend');


/*
	$("#carousel").jCarouselLite({
		 visible: 1,
		 auto: 22000,
		 speed: 300,
		 circular: true,
		 btnNext: ".next",
		 btnPrev: ".prev"
	});
*/

	$('div.majorbrand').find('a').mouseover(function(){
		$(this).find('img').animate({left:'-36px'},'fast');
	}).stop().mouseout(function(){
		$(this).find('img').animate({left:'0'},'fast');
	}).stop();

	  
	$('li.todaylist').on('mouseover',function(e){
		$(this).addClass('border');
	}).on('mouseout',function(e){
		$(this).removeClass('border');
	});

	$('img.pic').lazyload({
		effect : "fadeIn",
		threshold : 100
	});

    $.featureList(
        $("div.homebrandtabs li"),
        $("div.majorbrand ul"), {
        start_item  :   0,
        transition_interval:0
    });


    $.featureList(
        $("ul#slide_index li"),
        $("ul#slide_list li"), {
        start_item  :   0,
        transition_interval:10000
    });


    function jsDivide(molecular,denominator){
        var number_molecular = parseFloat(molecular),
            number_denominator = parseFloat(denominator);

        return formatFloat((number_denominator/number_molecular)*10,1);

    }

    function formatFloat(number, pos) {
        return Math.round(number * Math.pow(10, pos)) / Math.pow(10, pos);
    }

    var discountlist = $('div.iteminfo');

    $.each(discountlist,function(i,d){
    	discount = $('.discount',d),
	    market_price = $.trim($('.market_price',d).text()),
	    price = $.trim($('.price',d).text());
	    discount.text(jsDivide(market_price,price));
    });
  
  	if(data.topic_brand!=false){
		$.tmpl($('#topicbrand_tmpl').html(),data.topic_brand).appendTo('ul#brandtopic');
	}
	if(data.topic_theme!=false){
		$.tmpl($('#topic_tmpl').html(),data.topic_theme).appendTo('ul#topic_list');
	}


});