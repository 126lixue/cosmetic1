$(function(){
	//首页微信二维码移入移除事件
	$('#wechater').mouseover(function(){
		$('.wechatqrcode').show();
	});
	$('.wechatqrcode').mouseout(function(){
		$(this).hide();
	});
	
	
	
	//首页导航栏目鼠标移入移除事件
	$('.container ul li').mouseover(function(){
		$(this).find('.navcategorylist').show();
	});
	$('.container ul li').mouseout(function(){
		$(this).find('.navcategorylist').hide();
	});
  //首页导航条检索移入移除事件
	$('.container .subnav').mouseover(function(){
		$(this).find('ol').show();
		$(this).find('i').css('background-position','-410px -120px'); 
	});
	$('.container .subnav').mouseout(function(){
		$(this).find('ol').hide();
		$(this).find('i').css('background-position','-384px -120px');
	});
	
//首页中部滑动门事件
	$('.home_title1 a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
	$('.brand_recommend').show();
	$('.home_title1').click(function(){ 
		$(this).parent().find('li a').css('background','#fff').css('color','#969696').css('font-weight','normal');
		$('.majorbrand ul').hide();
		$('.brand_recommend').show();
		$(this).find('a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
	});
	$('.home_title2').click(function(){ 
		$('.majorbrand ul').hide();
		$('.brand_ea').show();
		$(this).parent().find('li a').css('background','#fff').css('color','#969696').css('font-weight','normal');
		$(this).find('a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
		
	});
	$('.home_title3').click(function(){ 
		$('.majorbrand ul').hide();
		$('.brand_jp').show();
		$(this).parent().find('li a').css('background','#fff').css('color','#969696').css('font-weight','normal');
		$(this).find('a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
		
	});
	$('.home_title4').click(function(){ 
		$('.majorbrand ul').hide();
		$('.brand_kr').show();
		$(this).parent().find('li a').css('background','#fff').css('color','#969696').css('font-weight','normal');
		$(this).find('a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
		
	});
	$('.home_title5').click(function(){ 
		$('.majorbrand ul').hide();
		$('.brand_cn').show();
		$(this).parent().find('li a').css('background','#fff').css('color','#969696').css('font-weight','normal');
		$(this).find('a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
		
	});
	$('.home_title6').click(function(){ 
		$('.majorbrand ul').hide();
		$('.brand_other').show();
		$(this).parent().find('li a').css('background','#fff').css('color','#969696').css('font-weight','normal');
		$(this).find('a').css('color','#EA2690').css('background','#eee').css('font-weight','700');
	});
	
	
	
 //	首页中部分类产品列表移入移除事件	
    $('.majorbrand ul li').hover(function(){
    	$(this).stop();
        	$(this).find('a img').animate({left:'-20px'});
    	
    },function(){
    	$(this).stop();
        	$(this).find('a img').animate({left:'0'});
    		
    });
    
    
  //首页主体区图片移入移除功能
    $('.todaylist').mouseover(function(){
    	$(this).css('border','1px solid #ED145B');
    	$(this).find('.foot').css('background','#F25B8C');
    });
    
    $('.todaylist').mouseout(function(){
    	$(this).css('border','1px solid #DDD');
    	$(this).find('.foot').css('background','#E9F5E4');
    });
    
    
    
    
    
    
	
	
	
});