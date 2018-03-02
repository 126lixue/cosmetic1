require(["jquery","tmpl","geturlparam"],function($){ 	

$(document).ready(function(e){

  var navigation = $('#navigation'),
      aside_category = $('span#aside_category','div.aside'),
      uri=geturlparam('category'),
      /*
      navbrand = $('div.navigationbrand'),
      navbrandbtn = navbrand.find('i'),
      brandlist = navbrand.find('ol'),
      databrand = {}
      */

      subnav = $('div.subnav'),
      databrand = {},
      dataskin = {},

      navcategory=$('a.nav_category')
      ;

  if(navigation.length){

    $.post('/common/get_category',function(data){
      var data = $.parseJSON(data);
      if(data.status===1){
        $.tmpl($('#tmpl_navigation').html(),data.data).appendTo(navigation);
        $.each(navigation.find('li'),function(i,l){
          var me = $(l);
          if(String(me.data('uri'))===uri){
            me.addClass('current');
            aside_category.text(me.find('a').text());
          }

          if(me.hasClass('nav_category')){
            var meid=me.data('uri'),sndnav = me.find('div.navcategorylist');

            $.post('/common/get_secondary',{category_id:meid},function(snd){
              var snd = $.parseJSON(snd);
              if(snd.status===1 && snd.data.length){
                sndnav.empty().append($.tmpl($("#tmpl_navsecondary").html(),snd.data));
              }
            });




            
            me.on('mouseover',function(e){
              me.addClass('current');
              sndnav.show();
            }).on('mouseleave',function(e){
              sndnav.hide();
              me.removeClass('current');
            });
          }

        });



      }
    });


  $.each(subnav,function(i,s){
    var 
      subnavIcon = $(s).find('i'),
      subnavList = $(s).find('ol');
    $(s).hover(function(e){    

      if($(s).hasClass('navigationbrand')){
          if(databrand.length){
            subnavList.empty().append($.tmpl($('#tmpl_navbrand').html(),databrand));
          }else{
            $.post('/common/data_brand',function(data){
              var data = $.parseJSON(data);
              if(data.status === 1){
                databrand=data.data;        
                subnavList.empty();
                $.tmpl($('#tmpl_navbrand').html(),data.data).appendTo(subnavList);
              }
            });
          }
      }
      
      if($(s).hasClass('navigationskin')){
          if(dataskin.length){
            subnavList.empty().append($.tmpl($('#tmpl_navskin').html(),dataskin));
          }else{
            $.post('/common/get_skin',function(data){
              var data = $.parseJSON(data);
              if(data.status === 1){
                dataskin=data.data;        
                subnavList.empty();
                $.tmpl($('#tmpl_navskin').html(),data.data).appendTo(subnavList);
              }
            });
          }
      }
      
      subnavIcon.removeClass('icon-folder-close').addClass('icon-folder-open');
      subnavList.slideDown('fast');
    },function(e){
      subnavIcon.removeClass('icon-folder-open').addClass('icon-folder-close');
      subnavList.slideUp('fast');
    });
  });






  }

















/*
  navbrand.hover(function(e){    
    if(databrand.length){
      brandlist.empty().append($.tmpl($('#tmpl_navbrand').html(),databrand));
    }else{
      $.post('/common/data_brand',function(data){
        var data = $.parseJSON(data);
        if(data.status === 1){
          databrand=data.data;        
          brandlist.empty();
          $.tmpl($('#tmpl_navbrand').html(),data.data).appendTo(brandlist);
        }
      });
    }
    navbrandbtn.removeClass('icon-folder-close').addClass('icon-folder-open');
    brandlist.slideDown('fast');
  },function(e){
    navbrandbtn.removeClass('icon-folder-open').addClass('icon-folder-close');
    brandlist.slideUp('fast');
  });
*/


});


});