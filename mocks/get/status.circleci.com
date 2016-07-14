<!DOCTYPE html>
<html lang="en">
 <head>
  <meta content="IE=edge" http-equiv="X-UA-Compatible">
   <!-- force IE browsers in compatibility mode to use their most aggressive rendering engine -->
   <meta charset="utf-8">
    <title>
     CircleCI Status
    </title>
    <meta content="Welcome to CircleCI's home for real-time and historical data on system performance." name="description">
     <meta content="TQFwNXX-22Rp3iu0w0iSSZOGHlgyojpElPrhqwzgaH" name="globalsign-domain-verification"/>
     <!-- Mobile viewport optimization h5bp.com/ad -->
     <meta content="True" name="HandheldFriendly">
      <meta content="320" name="MobileOptimized">
       <meta content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0" name="viewport">
        <!-- Mobile IE allows us to activate ClearType technology for smoothing fonts for easy reading -->
        <meta content="on" http-equiv="cleartype">
         <!-- Le fonts -->
         <style>
          @font-face {
    font-family: 'proxima-nova';
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaLight.eot?host=status.circleci.com');
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaLight.eot?host=status.circleci.com#iefix') format('embedded-opentype'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaLight.woff?host=status.circleci.com') format('woff'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaLight.ttf?host=status.circleci.com') format('truetype');
    font-weight:300;
    font-style:normal;
  }
   
  @font-face {
    font-family: 'proxima-nova';
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegular.eot?host=status.circleci.com');
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegular.eot?host=status.circleci.com#iefix') format('embedded-opentype'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegular.woff?host=status.circleci.com') format('woff'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegular.ttf?host=status.circleci.com') format('truetype');
    font-weight:400;
    font-style:normal;
  }
   
  @font-face {
    font-family: 'proxima-nova';
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegularIt.eot?host=status.circleci.com');
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegularIt.eot?host=status.circleci.com#iefix') format('embedded-opentype'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegularIt.woff?host=status.circleci.com') format('woff'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaRegularIt.ttf?host=status.circleci.com') format('truetype');
    font-weight:400;
    font-style:italic;
  }
   
  @font-face {
    font-family: 'proxima-nova';
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaSemibold.eot?host=status.circleci.com');
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaSemibold.eot?host=status.circleci.com#iefix') format('embedded-opentype'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaSemibold.woff?host=status.circleci.com') format('woff'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaSemibold.ttf?host=status.circleci.com') format('truetype');
    font-weight:500;
    font-style:normal;
  }
   
  @font-face {
    font-family: 'proxima-nova';
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaBold.eot?host=status.circleci.com');
    src: url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaBold.eot?host=status.circleci.com#iefix') format('embedded-opentype'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaBold.woff?host=status.circleci.com') format('woff'),
         url('//dka575ofm4ao0.cloudfront.net/assets/ProximaNovaBold.ttf?host=status.circleci.com') format('truetype');
    font-weight:700;
    font-style:normal;
  }
         </style>
         <link href="img/touch/apple-touch-icon-144x144-precomposed.png" rel="apple-touch-icon-precomposed" sizes="144x144"/>
         <link href="img/touch/apple-touch-icon-114x114-precomposed.png" rel="apple-touch-icon-precomposed" sizes="114x114"/>
         <link href="img/touch/apple-touch-icon-72x72-precomposed.png" rel="apple-touch-icon-precomposed" sizes="72x72"/>
         <link href="img/touch/apple-touch-icon-57x57-precomposed.png" rel="apple-touch-icon-precomposed"/>
         <link href="//dka575ofm4ao0.cloudfront.net/pages-favicon_logos/original/350/open-uri20131231-13916-1fw4tbi" rel="shortcut icon">
          <link href="http://status.circleci.com/history.atom" rel="alternate" title="CircleCI Status History - Atom Feed" type="application/atom+xml">
           <link href="http://status.circleci.com/history.rss" rel="alternate" title="CircleCI Status History - RSS Feed" type="application/rss+xml">
            <link href="http://status.circleci.com/history.atom" rel="alternate" title="ATOM" type="application/atom+xml"/>
            <meta content="authenticity_token" name="csrf-param"/>
            <meta content="XDfuyWUL3+DpIlysCi++nrSUrlyNi/WjuEazMo51yxs=" name="csrf-token"/>
            <!-- Le styles -->
            <link href="//dka575ofm4ao0.cloudfront.net/assets/status_manifest-ca111bd07c784440770ca047e2025124.css" media="all" rel="stylesheet"/>
            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">
            </script>
            <style>
             /* BODY BACKGROUND */ /* BODY BACKGROUND */ /* BODY BACKGROUND */ /* BODY BACKGROUND */ /* BODY BACKGROUND */ 
  body,
  .layout-content.status.status-api .section .example-container .example-opener .color-secondary,
  .grouped-items-selector {
    background-color:#fbfbfb;
  }





  /* PRIMARY FONT COLOR */ /* PRIMARY FONT COLOR */ /* PRIMARY FONT COLOR */ /* PRIMARY FONT COLOR */ 
  body.status,
  .color-primary,
  .color-primary:hover,
  .layout-content.status-index .status-day .update-title.impact-none a,
  .layout-content.status-index .status-day .update-title.impact-none a:hover,
  .layout-content.status-index .timeframes-container .timeframe.active,
  .layout-content.status-full-history .month .incident-container .impact-none,
  .layout-content.status.status-index .incidents-list .incident-title.impact-none a,
  .layout-content.status .grouped-items-selector.inline .grouped-item.active {
    color: #555555;
  }

  .layout-content.status.status-index .components-statuses .component-container .name {
    color:#555555;
    color:rgba(85,85,85,.8);
  }






  /* SECONDARY FONT COLOR */ /* SECONDARY FONT COLOR */ /* SECONDARY FONT COLOR */ /* SECONDARY FONT COLOR */ 
  small,
  .layout-content.status .table-row .date,
  .color-secondary,
  .layout-content.status .grouped-items-selector.inline .grouped-item {
    color: #898989;
  }









  /* BORDER COLOR */  /* BORDER COLOR */  /* BORDER COLOR */  /* BORDER COLOR */  /* BORDER COLOR */  /* BORDER COLOR */ 
  body.status .layout-content.status .border-color, hr, .tooltip-base, .markdown-display table {
    border-color: #e3e3e3;
  }

  .markdown-display table td {
    border-top-color: #e3e3e3;
  }

  .markdown-display table td + td, .markdown-display table th + th {
    border-left-color: #e3e3e3; 
  }






  /* CSS REDS */ /* CSS REDS */ /* CSS REDS */ /* CSS REDS */ /* CSS REDS */ /* CSS REDS */ /* CSS REDS */ 
  .layout-content.status.status-index .status-day .update-title.impact-critical a,
  .layout-content.status.status-index .status-day .update-title.impact-critical a:hover,
  .layout-content.status.status-index .page-status.status-critical,
  .layout-content.status.status-index .unresolved-incident.impact-critical .incident-title,
  .flat-button.background-red {
    background-color: #c13737;
  }
  .layout-content.status-index .components-statuses .component-container.status-red:after,
  .layout-content.status-full-history .month .incident-container .impact-critical,
  .layout-content.status-incident .incident-name.impact-critical,
  .layout-content.status.status-index .incidents-list .incident-title.impact-critical a,
  .status-red .icon-indicator,
  .components-container .component-inner-container.status-red .component-status,
  .components-container .component-inner-container.status-red .icon-indicator {
    color: #c13737;
  }

  .layout-content.status.status-index .unresolved-incident.impact-critical .updates {
    border-color:#c13737;
  }






  /* CSS ORANGES */ /* CSS ORANGES */ /* CSS ORANGES */ /* CSS ORANGES */ /* CSS ORANGES */ /* CSS ORANGES */ 
  .layout-content.status.status-index .status-day .update-title.impact-major a,
  .layout-content.status.status-index .status-day .update-title.impact-major a:hover,
  .layout-content.status.status-index .page-status.status-major,
  .layout-content.status.status-index .unresolved-incident.impact-major .incident-title {
    background-color: #e95900;
  }
  .layout-content.status-index .components-statuses .component-container.status-orange:after,
  .layout-content.status-full-history .month .incident-container .impact-major,
  .layout-content.status-incident .incident-name.impact-major,
  .layout-content.status.status-index .incidents-list .incident-title.impact-major a,
  .status-orange .icon-indicator,
  .components-container .component-inner-container.status-orange .component-status,
  .components-container .component-inner-container.status-orange .icon-indicator {
    color: #e95900;
  }

  .layout-content.status.status-index .unresolved-incident.impact-major .updates {
    border-color: #e95900;
  }







/* CSS YELLOWS */ /* CSS YELLOWS */ /* CSS YELLOWS */ /* CSS YELLOWS */ /* CSS YELLOWS */ /* CSS YELLOWS */ 
  .layout-content.status.status-index .status-day .update-title.impact-minor a,
  .layout-content.status.status-index .status-day .update-title.impact-minor a:hover,
  .layout-content.status.status-index .page-status.status-minor,
  .layout-content.status.status-index .unresolved-incident.impact-minor .incident-title, 
  .layout-content.status.status-index .scheduled-incidents-container .tab {
    background-color: #ffc40d;
  }
  .layout-content.status-index .components-statuses .component-container.status-yellow:after,
  .layout-content.status-full-history .month .incident-container .impact-minor,
  .layout-content.status-incident .incident-name.impact-minor,
  .layout-content.status.status-index .incidents-list .incident-title.impact-minor a,
  .status-yellow .icon-indicator,
  .components-container .component-inner-container.status-yellow .component-status,
  .components-container .component-inner-container.status-yellow .icon-indicator {
    color: #ffc40d;
  }

  .layout-content.status.status-index .unresolved-incident.impact-minor .updates,
  .layout-content.status.status-index .scheduled-incidents-container {
    border-color:#ffc40d;
  }






/* CSS BLUES */ /* CSS BLUES */ /* CSS BLUES */ /* CSS BLUES */ /* CSS BLUES */ /* CSS BLUES */
  .layout-content.status.status-index .status-day .update-title.impact-maintenance a,
  .layout-content.status.status-index .status-day .update-title.impact-maintenance a:hover,
  .layout-content.status.status-index .page-status.status-maintenance,
  .layout-content.status.status-index .unresolved-incident.impact-maintenance .incident-title,
  .layout-content.status.status-index .scheduled-incidents-container .tab {
    background-color: #3498DB;
  }

  .layout-content.status-index .components-statuses .component-container.status-blue:after,
  .layout-content.status-full-history .month .incident-container .impact-maintenance,
  .layout-content.status-incident .incident-name.impact-maintenance,
  .layout-content.status.status-index .incidents-list .incident-title.impact-maintenance a,
  .status-blue .icon-indicator,
  .components-container .component-inner-container.status-blue .component-status,
  .components-container .component-inner-container.status-blue .icon-indicator {
    color: #3498DB;
  }

  .layout-content.status.status-index .unresolved-incident.impact-maintenance .updates,
  .layout-content.status.status-index .scheduled-incidents-container {
    border-color:#3498DB;
  }





  /* CSS GREENS */ /* CSS GREENS */ /* CSS GREENS */ /* CSS GREENS */ /* CSS GREENS */ /* CSS GREENS */ /* CSS GREENS */ 
  .layout-content.status.status-index .page-status.status-none {
    background-color: #229922;
  }
  .layout-content.status-index .components-statuses .component-container.status-green:after,
  .status-green .icon-indicator,
  .components-container .component-inner-container.status-green .component-status,
  .components-container .component-inner-container.status-green .icon-indicator {
    color: #229922;
  }




  /* CSS LINK COLOR */  /* CSS LINK COLOR */  /* CSS LINK COLOR */  /* CSS LINK COLOR */  /* CSS LINK COLOR */  /* CSS LINK COLOR */  
  a,
  a:hover,
  .layout-content.status-index .page-footer span a:hover,
  .layout-content.status-index .timeframes-container .timeframe:not(.active):hover,
  .layout-content.status-incident .subheader a:hover {
    color: #0096c8;
  }
  .flat-button, .masthead .updates-dropdown-container .show-updates-dropdown {
    background-color:#0096c8;
  }
            </style>
            <!-- custom css -->
            <!-- Le HTML5 shim -->
            <!--[if lt IE 9]>
      <script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
            <!-- injection for static -->
           </link>
          </link>
         </link>
        </meta>
       </meta>
      </meta>
     </meta>
    </meta>
   </meta>
  </meta>
 </head>
 <body class="status index status-none">
  <div class="status-page-tour-info" data-js-hook="status-page-tour-info" style="display:none">
   <div class="container inner">
    Welcome to the demo status page.
    <a data-js-hook="restart-tour" href="#">
     Take the tour
    </a>
    .
   </div>
  </div>
  <div class="layout-content status status-index premium">
   <div class="masthead-container premium">
    <div class="masthead">
     <div class="images-container" data-js-hook="images-container" id="cover-image-container">
     </div>
     <style>
      #cover-image-container {
            background-image:url("//dka575ofm4ao0.cloudfront.net/pages-hero_covers/normal/350/y15mjCQ7T3iLEJpRUXC5");
          }

          @media only screen and (-webkit-min-device-pixel-ratio: 2), 
                 only screen and (min-resolution: 192dpi) { 
            #cover-image-container {
              background-image:url("//dka575ofm4ao0.cloudfront.net/pages-hero_covers/retina/350/y15mjCQ7T3iLEJpRUXC5") !important;
            }
          }
     </style>
     <div class="text-container">
      <span class="page-name font-largest">
       <a href="https://circleci.com" target="_blank">
        CircleCI
       </a>
      </span>
      <div class="updates-dropdown-container" data-js-hook="updates-dropdown-container">
       <a class="show-updates-dropdown" data-js-hook="show-updates-dropdown" href="#" id="show-updates-dropdown">
       </a>
       <div class="updates-dropdown" data-js-hook="updates-dropdown" style="display:none">
        <div class="updates-dropdown-nav nav-items-6">
         <a href="#updates-dropdown-email" id="updates-dropdown-email-btn">
          <span class="icon-container email">
          </span>
         </a>
         <a href="#updates-dropdown-sms" id="updates-dropdown-sms-btn">
          <span class="icon-container sms">
          </span>
         </a>
         <a href="#updates-dropdown-webhook" id="updates-dropdown-webhook-btn">
          <span class="icon-container webhook">
          </span>
         </a>
         <a href="#updates-dropdown-twitter" id="updates-dropdown-twitter-btn">
          <span class="icon-container twitter">
          </span>
         </a>
         <a href="#updates-dropdown-atom" id="updates-dropdown-atom-btn">
          <span class="icon-container rss">
          </span>
         </a>
         <a data-js-hook="updates-dropdown-close" href="#" id="updates-dropdown-close-btn">
          x
         </a>
        </div>
        <div class="updates-dropdown-sections-container">
         <div class="updates-dropdown-section email" id="updates-dropdown-email" style="display:none">
          <div class="directions">
           Get email notifications whenever CircleCI creates or updates an incident.
          </div>
          <form accept-charset="UTF-8" action="/subscribe.json" data-remote="true" id="subscribe-form-email" method="post">
           <div style="display:none">
            <input name="utf8" type="hidden" value="✓"/>
           </div>
           <!-- make sure not to put cookie values in here since this gets cached -->
           <input class="full-width" data-js-hook="email-notification-field" id="email" name="email" placeholder="Email Address" type="text">
            <input class="flat-button full-width" data-disabled-text="Subscribing..." data-revert-on-success="true" id="subscribe-btn-email" type="submit" value="Subscribe via Email">
            </input>
           </input>
          </form>
         </div>
         <div class="updates-dropdown-section phone" id="updates-dropdown-sms" style="display:none">
          <div class="directions">
           Get SMS notifications whenever CircleCI
           <strong>
            creates
           </strong>
           or
           <strong>
            resolves
           </strong>
           an incident.
          </div>
          <form accept-charset="UTF-8" action="/subscribe.json" data-remote="true" id="subscribe-form-sms" method="post">
           <div style="display:none">
            <input name="utf8" type="hidden" value="✓"/>
           </div>
           <div class="control-group">
            <div class="controls externalities-sms-container ">
             <!-- make sure not to put cookie values in here since this gets cached -->
             <select data-js-hook="phone-country" id="phone-country" name="phone_country">
              <option value="af">
               Afghanistan (+93)
              </option>
              <option value="al">
               Albania (+355)
              </option>
              <option value="dz">
               Algeria (+213)
              </option>
              <option value="as">
               American Samoa (+1684)
              </option>
              <option value="ad">
               Andorra (+376)
              </option>
              <option value="ao">
               Angola (+244)
              </option>
              <option value="ai">
               Anguilla (+1264)
              </option>
              <option value="ag">
               Antigua and Barbuda (+1268)
              </option>
              <option value="ar">
               Argentina (+54)
              </option>
              <option value="am">
               Armenia (+374)
              </option>
              <option value="aw">
               Aruba (+297)
              </option>
              <option value="au">
               Australia/Cocos/Christmas Island (+61)
              </option>
              <option value="at">
               Austria (+43)
              </option>
              <option value="az">
               Azerbaijan (+994)
              </option>
              <option value="bs">
               Bahamas (+1)
              </option>
              <option value="bh">
               Bahrain (+973)
              </option>
              <option value="bd">
               Bangladesh (+880)
              </option>
              <option value="bb">
               Barbados (+1246)
              </option>
              <option value="by">
               Belarus (+375)
              </option>
              <option value="be">
               Belgium (+32)
              </option>
              <option value="bz">
               Belize (+501)
              </option>
              <option value="bj">
               Benin (+229)
              </option>
              <option value="bm">
               Bermuda (+1441)
              </option>
              <option value="bo">
               Bolivia (+591)
              </option>
              <option value="ba">
               Bosnia and Herzegovina (+387)
              </option>
              <option value="bw">
               Botswana (+267)
              </option>
              <option value="br">
               Brazil (+55)
              </option>
              <option value="bn">
               Brunei (+673)
              </option>
              <option value="bg">
               Bulgaria (+359)
              </option>
              <option value="bf">
               Burkina Faso (+226)
              </option>
              <option value="bi">
               Burundi (+257)
              </option>
              <option value="kh">
               Cambodia (+855)
              </option>
              <option value="cm">
               Cameroon (+237)
              </option>
              <option value="ca">
               Canada (+1)
              </option>
              <option value="cv">
               Cape Verde (+238)
              </option>
              <option value="ky">
               Cayman Islands (+1345)
              </option>
              <option value="cf">
               Central Africa (+236)
              </option>
              <option value="td">
               Chad (+235)
              </option>
              <option value="cl">
               Chile (+56)
              </option>
              <option value="cn">
               China (+86)
              </option>
              <option value="co">
               Colombia (+57)
              </option>
              <option value="km">
               Comoros (+269)
              </option>
              <option value="cg">
               Congo (+242)
              </option>
              <option value="cd">
               Congo, Dem Rep (+243)
              </option>
              <option value="cr">
               Costa Rica (+506)
              </option>
              <option value="hr">
               Croatia (+385)
              </option>
              <option value="cy">
               Cyprus (+357)
              </option>
              <option value="cz">
               Czech Republic (+420)
              </option>
              <option value="dk">
               Denmark (+45)
              </option>
              <option value="dj">
               Djibouti (+253)
              </option>
              <option value="dm">
               Dominica (+1767)
              </option>
              <option value="do">
               Dominican Republic (+1809)
              </option>
              <option value="eg">
               Egypt (+20)
              </option>
              <option value="sv">
               El Salvador (+503)
              </option>
              <option value="gq">
               Equatorial Guinea (+240)
              </option>
              <option value="ee">
               Estonia (+372)
              </option>
              <option value="et">
               Ethiopia (+251)
              </option>
              <option value="fo">
               Faroe Islands (+298)
              </option>
              <option value="fj">
               Fiji (+679)
              </option>
              <option value="fi">
               Finland/Aland Islands (+358)
              </option>
              <option value="fr">
               France (+33)
              </option>
              <option value="gf">
               French Guiana (+594)
              </option>
              <option value="pf">
               French Polynesia (+689)
              </option>
              <option value="ga">
               Gabon (+241)
              </option>
              <option value="gm">
               Gambia (+220)
              </option>
              <option value="ge">
               Georgia (+995)
              </option>
              <option value="de">
               Germany (+49)
              </option>
              <option value="gh">
               Ghana (+233)
              </option>
              <option value="gi">
               Gibraltar (+350)
              </option>
              <option value="gr">
               Greece (+30)
              </option>
              <option value="gl">
               Greenland (+299)
              </option>
              <option value="gd">
               Grenada (+1473)
              </option>
              <option value="gp">
               Guadeloupe (+590)
              </option>
              <option value="gu">
               Guam (+1671)
              </option>
              <option value="gt">
               Guatemala (+502)
              </option>
              <option value="gn">
               Guinea (+224)
              </option>
              <option value="gy">
               Guyana (+592)
              </option>
              <option value="ht">
               Haiti (+509)
              </option>
              <option value="hn">
               Honduras (+504)
              </option>
              <option value="hk">
               Hong Kong (+852)
              </option>
              <option value="hu">
               Hungary (+36)
              </option>
              <option value="is">
               Iceland (+354)
              </option>
              <option value="in">
               India (+91)
              </option>
              <option value="id">
               Indonesia (+62)
              </option>
              <option value="ir">
               Iran (+98)
              </option>
              <option value="iq">
               Iraq (+964)
              </option>
              <option value="ie">
               Ireland (+353)
              </option>
              <option value="il">
               Israel (+972)
              </option>
              <option value="it">
               Italy (+39)
              </option>
              <option value="jm">
               Jamaica (+1876)
              </option>
              <option value="jp">
               Japan (+81)
              </option>
              <option value="jo">
               Jordan (+962)
              </option>
              <option value="ke">
               Kenya (+254)
              </option>
              <option value="kr">
               Korea, Republic of (+82)
              </option>
              <option value="kw">
               Kuwait (+965)
              </option>
              <option value="kg">
               Kyrgyzstan (+996)
              </option>
              <option value="la">
               Laos (+856)
              </option>
              <option value="lv">
               Latvia (+371)
              </option>
              <option value="lb">
               Lebanon (+961)
              </option>
              <option value="ls">
               Lesotho (+266)
              </option>
              <option value="lr">
               Liberia (+231)
              </option>
              <option value="ly">
               Libya (+218)
              </option>
              <option value="li">
               Liechtenstein (+423)
              </option>
              <option value="lt">
               Lithuania (+370)
              </option>
              <option value="lu">
               Luxembourg (+352)
              </option>
              <option value="mo">
               Macao (+853)
              </option>
              <option value="mk">
               Macedonia (+389)
              </option>
              <option value="mg">
               Madagascar (+261)
              </option>
              <option value="mw">
               Malawi (+265)
              </option>
              <option value="my">
               Malaysia (+60)
              </option>
              <option value="mv">
               Maldives (+960)
              </option>
              <option value="ml">
               Mali (+223)
              </option>
              <option value="mt">
               Malta (+356)
              </option>
              <option value="mq">
               Martinique (+596)
              </option>
              <option value="mr">
               Mauritania (+222)
              </option>
              <option value="mu">
               Mauritius (+230)
              </option>
              <option value="mx">
               Mexico (+52)
              </option>
              <option value="mc">
               Monaco (+377)
              </option>
              <option value="mn">
               Mongolia (+976)
              </option>
              <option value="me">
               Montenegro (+382)
              </option>
              <option value="ms">
               Montserrat (+1664)
              </option>
              <option value="ma">
               Morocco/Western Sahara (+212)
              </option>
              <option value="mz">
               Mozambique (+258)
              </option>
              <option value="na">
               Namibia (+264)
              </option>
              <option value="np">
               Nepal (+977)
              </option>
              <option value="nl">
               Netherlands (+31)
              </option>
              <option value="nz">
               New Zealand (+64)
              </option>
              <option value="ni">
               Nicaragua (+505)
              </option>
              <option value="ne">
               Niger (+227)
              </option>
              <option value="ng">
               Nigeria (+234)
              </option>
              <option value="no">
               Norway (+47)
              </option>
              <option value="om">
               Oman (+968)
              </option>
              <option value="pk">
               Pakistan (+92)
              </option>
              <option value="ps">
               Palestinian Territory (+970)
              </option>
              <option value="pa">
               Panama (+507)
              </option>
              <option value="py">
               Paraguay (+595)
              </option>
              <option value="pe">
               Peru (+51)
              </option>
              <option value="ph">
               Philippines (+63)
              </option>
              <option value="pl">
               Poland (+48)
              </option>
              <option value="pt">
               Portugal (+351)
              </option>
              <option value="pr">
               Puerto Rico (+1)
              </option>
              <option value="qa">
               Qatar (+974)
              </option>
              <option value="re">
               Reunion/Mayotte (+262)
              </option>
              <option value="ro">
               Romania (+40)
              </option>
              <option value="ru">
               Russia/Kazakhstan (+7)
              </option>
              <option value="rw">
               Rwanda (+250)
              </option>
              <option value="ws">
               Samoa (+685)
              </option>
              <option value="sm">
               San Marino (+378)
              </option>
              <option value="sa">
               Saudi Arabia (+966)
              </option>
              <option value="sn">
               Senegal (+221)
              </option>
              <option value="rs">
               Serbia (+381)
              </option>
              <option value="sc">
               Seychelles (+248)
              </option>
              <option value="sl">
               Sierra Leone (+232)
              </option>
              <option value="sg">
               Singapore (+65)
              </option>
              <option value="sk">
               Slovakia (+421)
              </option>
              <option value="si">
               Slovenia (+386)
              </option>
              <option value="za">
               South Africa (+27)
              </option>
              <option value="es">
               Spain (+34)
              </option>
              <option value="lk">
               Sri Lanka (+94)
              </option>
              <option value="kn">
               St Kitts and Nevis (+1869)
              </option>
              <option value="lc">
               St Lucia (+1758)
              </option>
              <option value="vc">
               St Vincent Grenadines (+1784)
              </option>
              <option value="sd">
               Sudan (+249)
              </option>
              <option value="sr">
               Suriname (+597)
              </option>
              <option value="sz">
               Swaziland (+268)
              </option>
              <option value="se">
               Sweden (+46)
              </option>
              <option value="ch">
               Switzerland (+41)
              </option>
              <option value="sy">
               Syria (+963)
              </option>
              <option value="tw">
               Taiwan (+886)
              </option>
              <option value="tj">
               Tajikistan (+992)
              </option>
              <option value="tz">
               Tanzania (+255)
              </option>
              <option value="th">
               Thailand (+66)
              </option>
              <option value="tg">
               Togo (+228)
              </option>
              <option value="to">
               Tonga (+676)
              </option>
              <option value="tt">
               Trinidad and Tobago (+1868)
              </option>
              <option value="tn">
               Tunisia (+216)
              </option>
              <option value="tr">
               Turkey (+90)
              </option>
              <option value="tc">
               Turks and Caicos Islands (+1649)
              </option>
              <option value="ug">
               Uganda (+256)
              </option>
              <option value="ua">
               Ukraine (+380)
              </option>
              <option value="ae">
               United Arab Emirates (+971)
              </option>
              <option value="gb">
               United Kingdom (+44)
              </option>
              <option selected="selected" value="us">
               United States (+1)
              </option>
              <option value="uy">
               Uruguay (+598)
              </option>
              <option value="uz">
               Uzbekistan (+998)
              </option>
              <option value="ve">
               Venezuela (+58)
              </option>
              <option value="vn">
               Vietnam (+84)
              </option>
              <option value="vg">
               Virgin Islands, British (+1284)
              </option>
              <option value="vi">
               Virgin Islands, U.S. (+1340)
              </option>
              <option value="ye">
               Yemen (+967)
              </option>
              <option value="zm">
               Zambia (+260)
              </option>
              <option value="zw">
               Zimbabwe (+263)
              </option>
             </select>
             <input class="prepend full-width" data-js-hook="sms-notification-field" id="phone-number" name="phone_number" placeholder="ex. 6505551234" type="text">
              <div class="clearfix">
              </div>
              <p class="help-block">
               <a data-js-hook="externalities-show-sms-country-toggle" href="#" id="phone-country">
                Not a US/CA phone number?
               </a>
              </p>
             </input>
            </div>
           </div>
           <input class="flat-button full-width" data-disabled-text="Subscribing..." data-revert-on-success="true" id="subscribe-btn-sms" type="submit" value="Subscribe via SMS">
            <div class="small" style="text-align:center;margin-top:10px;font-size:12px;line-height:14px;margin-bottom:-6px;">
             Message and data rates may apply. Go to www.statuspage.io/terms for terms and conditions.
            </div>
           </input>
          </form>
         </div>
         <div class="updates-dropdown-section webhook" id="updates-dropdown-webhook" style="display:none">
          <div class="directions">
           Get webhook notifications whenever CircleCI creates an incident, updates an incident, or changes a component status.
          </div>
          <form accept-charset="UTF-8" action="/subscribe.json" data-remote="true" id="subscribe-form-webhook" method="post">
           <div style="display:none">
            <input name="utf8" type="hidden" value="✓"/>
           </div>
           <div class="control-group">
            <div class="controls">
             <input class="full-width" data-js-hook="endpoint" id="endpoint-webhooks" name="endpoint" placeholder="http://www.yourdomain.com/endpoint/here" type="text"/>
             <p class="help-block">
              The URL we should send the webhooks to
             </p>
            </div>
           </div>
           <div class="control-group">
            <div class="controls">
             <input class="full-width" data-js-hook="email" id="email-webhooks" name="email" placeholder="Email Address" type="text"/>
             <p class="help-block">
              We'll send you email if your endpoint fails
             </p>
            </div>
           </div>
           <div class="form-actions">
            <input class="flat-button full-width" data-disabled-text="Subscribing..." data-revert-on-success="true" id="subscribe-btn-webhook" type="submit" value="Subscribe To Notifications">
            </input>
           </div>
          </form>
         </div>
         <div class="updates-dropdown-section twitter" id="updates-dropdown-twitter" style="display:none">
          <a class="twitter-follow-button" data-show-count="false" data-show-screen-name="true" data-width="59px" href="https://twitter.com/CircleCIstatus">
           Follow @CircleCIstatus
          </a>
          or
          <a href="http://www.twitter.com/CircleCIstatus" target="_blank">
           view our profile
          </a>
          .
          <style>
           .twitter-follow-button {
              margin-bottom: -6px;
            }
          </style>
          <script>
           !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');
          </script>
         </div>
         <div class="updates-dropdown-section atom" id="updates-dropdown-atom">
          Get the
          <a href="http://status.circleci.com/history.atom" target="_blank">
           Atom Feed
          </a>
          or
          <a href="http://status.circleci.com/history.rss" target="_blank">
           RSS Feed
          </a>
          .
         </div>
        </div>
       </div>
      </div>
     </div>
    </div>
   </div>
   <!-- this is outside of the .container so that the cover photo can go full width on mobile -->
   <div class="container">
    <div class="page-status status-none">
     <span class="status font-large">
      All Systems Operational
     </span>
     <span class="last-updated-stamp font-small">
     </span>
    </div>
    <div class="components-section font-regular">
     <div class="components-container one-column">
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         CircleCI
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         GitHub
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         Heroku
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         AWS
         <span class="tooltip-base" data-js-hook="tooltip" data-original-title="EC2 in us-east-1" data-responsive-placement="right-when-small">
          ?
         </span>
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         Pusher Pusher REST API
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         Pusher WebSocket client API
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         OS X Builds
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         Test Result Processing
         <span class="tooltip-base" data-js-hook="tooltip" data-original-title="Processing of JUnit XML and Cucumber test results." data-responsive-placement="right-when-small">
          ?
         </span>
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
      <div class="component-container border-color">
       <div class="component-inner-container status-green " data-js-hook="">
        <span class="name">
         Ubuntu 14.04 Builds
         <span class="tooltip-base" data-js-hook="tooltip" data-original-title="&amp;quot;Trusty&amp;quot; Build Fleet" data-responsive-placement="right-when-small">
          ?
         </span>
        </span>
        <span class="component-status">
         Operational
        </span>
        <span class="icon-indicator fa fa-check" data-js-hook="tooltip" data-original-title="Operational">
        </span>
       </div>
      </div>
     </div>
     <div class="component-statuses-legend font-small">
      <div class="legend-item status-green">
       <span class="icon-indicator fa fa-check">
       </span>
       Operational
      </div>
      <div class="legend-item status-yellow">
       <span class="icon-indicator fa fa-minus-square">
       </span>
       Degraded Performance
      </div>
      <div class="legend-item status-orange">
       <span class="icon-indicator fa fa-exclamation-triangle">
       </span>
       Partial Outage
      </div>
      <div class="legend-item status-red">
       <span class="icon-indicator fa fa-times">
       </span>
       Major Outage
      </div>
     </div>
    </div>
    <div class="incidents-list format-expanded">
     <div class="font-largest">
      Past Incidents
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        14
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported today.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        13
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular ">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        12
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <div class="incident-container">
       <div class="incident-title impact-major font-large">
        <a href="/incidents/k1zsjt7vplsk">
         GitHub Outage
        </a>
       </div>
       <div class="updates-container">
        <div class="update font-regular resolved">
         <strong>
          Resolved
         </strong>
         - 
        	

          	GitHub events have been flowing and their status page shows them as Operational. We will continue to monitor things closely and please do reach out to our Support team if you have any questions.
         <br>
          <small>
           Jul 12, 10:36 PDT
          </small>
         </br>
        </div>
        <div class="update font-regular update">
         <strong>
          Update
         </strong>
         - 
        	

          	We are continuing to closely monitor GitHub's status and recovery, and we are scaling to meet the expected influx of builds. Another update in 20(ish) minutes.
         <br>
          <small>
           Jul 12, 10:04 PDT
          </small>
         </br>
        </div>
        <div class="update font-regular monitoring">
         <strong>
          Monitoring
         </strong>
         - 
        	

          	GitHub is actively working to restore service and while you may be able to log in we are still not receiving build notifications. Will update in 20 minutes or when status changes.
         <br>
          <small>
           Jul 12, 09:43 PDT
          </small>
         </br>
        </div>
        <div class="update font-regular identified">
         <strong>
          Identified
         </strong>
         - 
        	

          	GitHub is currently showing an outage which impacts our ability to handle logins and receive build events, we are monitoring their status closely.
         <br>
          <small>
           Jul 12, 09:25 PDT
          </small>
         </br>
        </div>
       </div>
      </div>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        11
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        10
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        9
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        8
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        7
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        6
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        5
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        4
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        3
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular no-incidents">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        2
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <p class="color-secondary">
       No incidents reported.
      </p>
     </div>
     <div class="status-day font-regular ">
      <div class="date border-color font-large">
       Jul
       <var data-var="date">
        1
       </var>
       ,
       <var data-var="year">
        2016
       </var>
      </div>
      <div class="incident-container">
       <div class="incident-title impact-minor font-large">
        <a href="/incidents/4nl5cbz2sf7f">
         Increased OS X queue times
        </a>
       </div>
       <div class="updates-container">
        <div class="update font-regular resolved">
         <strong>
          Resolved
         </strong>
         - 
        	

          	We've fully recovered.
         <br>
          <small>
           Jul  1, 00:09 PDT
          </small>
         </br>
        </div>
        <div class="update font-regular monitoring">
         <strong>
          Monitoring
         </strong>
         - 
        	

          	We've recovered and will continue to monitor. Please let us know if you see unexpectedly high queue times.
         <br>
          <small>
           Jun 30, 23:18 PDT
          </small>
         </br>
        </div>
        <div class="update font-regular investigating">
         <strong>
          Investigating
         </strong>
         - 
        	

          	We lost several of our OS X builder instances and so we're running at reduced capacity. We anticipate increased queue times until we recover.
         <br>
          <small>
           Jun 30, 22:54 PDT
          </small>
         </br>
        </div>
       </div>
      </div>
     </div>
    </div>
    <div class="page-footer border-color font-small">
     <a class="history-footer-link" href="/history">
      <span style="font-family:arial">
       ←
      </span>
      Incident History
     </a>
     <span class="color-secondary powered-by">
      Powered by
      <a class="color-secondary" href="http://www.statuspage.io" target="_blank">
       StatusPage.io
      </a>
     </span>
    </div>
   </div>
  </div>
  <!-- register the global modal if necessary -->
  <!-- register the incident modals, has to be done here since content_for isn't evaluated in cache context -->
  <!-- custom metrics stuff -->
  <script src="//dka575ofm4ao0.cloudfront.net/assets/status_manifest-7bc30cb1957fdf1eb38c59eee311c004.js">
  </script>
  <!-- all of the content_for stuff -->
  <script type="text/javascript">
   $(function() {
        SP.currentPage.registerSubscriptionForm('email');

        SP.currentPage.registerSubscriptionForm('sms');

        SP.currentPage.registerSubscriptionForm('webhook');

          //weird bug here with capybara not playing nice with the mask lib
          $('[data-js-hook="phone-number"]').mask('999 999 9999');
      })
  </script>
  <script type="text/javascript">
   $(function() {
      })
  </script>
  <script src="//dka575ofm4ao0.cloudfront.net/assets/status_common-19141d98cec6e650a209414a4cdfb174.js">
  </script>
  <script src="//dka575ofm4ao0.cloudfront.net/assets/register_subscription_form-50eafe0fa351c9c82d3a8635b3cf4f81.js">
  </script>
  <script src="//dka575ofm4ao0.cloudfront.net/assets/status_idle-f412aff2b1a053dd639ec07d72c20475.js">
  </script>
  <script>
   $(function() {

      // clicks on first tab in subscribe popout since we won't know which is first
      // upon construction in the ruby code
      $('.updates-dropdown-nav > a').eq(0).click();

      // twitter follow button needs some margin
      $('.twitter-follow-button').css('margin-right', '6px');
    });


    $(function() {
      // open/close component groups
      HRB.utils.djshook('component-group-opener').on('click', function() {
        $(this).find('.group-parent-indicator').toggleClass('fa-plus-square-o').toggleClass('fa-minus-square-o').end().parent().toggleClass('open');
      });
    });
  </script>
  <script>
   //<![CDATA[
window.webpackManifest = {"1":"components-bundle-fad2bc0efd0793c4e8bc.js","2":"globals-bundle-a45f85f5ec5916d63e48.js","3":"hipchat_sidebar-bundle-2d427b9c6d1aaa7785bf.js","4":"manage-bundle-a43d4b34e9292fc82d0c.js"}
//]]>
  </script>
  <script src="//dka575ofm4ao0.cloudfront.net/assets/common-78932b00c34778b3db7a.js">
  </script>
  <script src="//dka575ofm4ao0.cloudfront.net/assets/globals-bundle-a45f85f5ec5916d63e48.js">
  </script>
  <script src="//dka575ofm4ao0.cloudfront.net/assets/react_ujs-0717138a1da7425da375c308afb97800.js">
  </script>
  <!-- FOR FLASH NOTICES -->
  <!-- FOR ERROR -->
  <script>
   $(function() {
    $('.powered-by').show().css('display','inline-block !important');
  });
  </script>
 </body>
</html>
