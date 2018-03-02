require.config({     
    baseUrl: 'http://img.zhenyuemei.com/',
    paths: { 
        "jquery": "common/jquery/jquery-1.11.0.min",
        "jquery2": "common/jquery/jquery-2.1.1.min",
        "tmpl": "common/jquery/jquery.tmpl.min",
        "ui":"common/ui/ui.min",
        "featureList":"common/jquery/jquery.featureList",
        "jcarousellite":"common/jquery/jquery.jcarousellite",
        "scrollup":"theme/scripts/scrollup",
        "segment":"theme/scripts/segment",
        "geturlparam":"theme/scripts/geturlparam",
        "tmplappend":"theme/scripts/tmplappend",
        "register":"theme/scripts/register",
        "sign":"theme/scripts/sign",
        "lazyload": "common/jquery/jquery.lazyload.min",
        "jqueryui":"common/jqueryui/jquery-ui.min",
        "timepicker":"common/jqueryui/jquery.ui.timepicker",
        "imagesLoaded":"common/jquery/jquery.imagesloaded",
        "wookmark":"common/jquery/jquery.wookmark.min"
    },  
    shim: {  
        "tmpl": {  
            deps: ["jquery"],  
            exports: "tmpl"  
        },
        "ui":{
            deps:["jquery"],
            exports:"ui"
        },
        "featureList":{
            deps:["jquery"],
            exports:"featureList"
        },
        "jcarousellite":{
            deps:["jquery"],
            exports:"jcarousellite"
        },
        "scrollup":{
            deps:["jquery"],
            exports:"scrollup"
        },
        "tmplappend":{
            deps:["jquery","tmpl"],
            exports:"tmplappend"
        },
        "lazyload": {  
            deps: ["jquery"],  
            exports: "lazyload"
        },
        "jqueryui": {  
            deps: ["jquery"],  
            exports: "jqueryui"
        },
        "timepicker": {  
            deps: ["jquery","jqueryui"],  
            exports: "timepicker"
        },
        "imagesLoaded": {  
            deps: ["jquery"],  
            exports: "imagesLoaded"
        },
        "wookmark": {  
            deps: ["jquery"],  
            exports: "wookmark"
        }

    }  
 });

