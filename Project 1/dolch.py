
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge,chrome=1">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Web Login Service</title>
        <link href="https://www1.umn.edu/twincities/favicon.ico" rel="shortcut icon" type="image/x-icon">
        <link href="https://fonts.googleapis.com/css?family=Raleway|Roboto:300,300i,400,400i,700,700i" rel="stylesheet">
        <link href="/idp/css/font-awesome.min.css" rel="stylesheet">
        <link href="/idp/css/bootstrap.min.css" rel="stylesheet">
        <link href="/idp/css/bootstrap-accessibility.css" rel="stylesheet">
        <link href="/idp/css/umn-header.css" rel="stylesheet">
        <link href="/idp/css/umn-footer.css" rel="stylesheet">
        <link href="/idp/css/umn-bootstrap-theme.css" rel="stylesheet">
        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
    </head>
    <body>
        <header class="umn_header" aria-label="University of Minnesota">
            <div class="container">
                <a href="http://umn.edu" class="umn_header-logo pull-left">University of Minnesota website</a>
                <div class="umn_header-search pull-right hidden-xs">
                    <a href="https://www.myu.umn.edu/">MyU <i class="fa fa-lock"></i>: For student, faculty, and staff</a>
                    <form action="https://search.umn.edu/tc/" role="search" class="umn_header-search-form hidden-xs">
                        <input type="search" name="q" class="umn_header-search-input form-control" aria-label="Search terms" placeholder="Search UMN...">
                        <button type="submit" class="umn_header-search-submit" aria-label="Search submit">
                            <i class="fa-search fa" aria-hidden="true"></i>
                        </button>
                        <input type="hidden" name="s" value="tc">
                        <input type="hidden" name="u" value="1">
                    </form>
                </div>
            </div>
        </header>
    	<main role="main">
            <div class="container">
<h1>Sign In</h1>
<div class="row">
	<div class="col-md-7 col-sm-6">
		
		
		
		<form action="/idp/profile/SAML2/Redirect/SSO?execution=e1s1" method="post" class="idp3_form" autocomplete="off">
							<div class="form-group-lg">
	                <label for="username">Internet ID</label>
	                <input type="text" class="form-control" id="username" name="j_username" autocapitalize="none" autocorrect="off" tabindex="1" value="">
	                <span class="help-block"><a href="https://my-account.umn.edu/forgot-login"><i class="fa fa-user" aria-hidden="true"></i>Recover your Internet ID</a></span>
                    </div>
	            <div class="form-group-lg">
	                <label for="password">Password</label>
	                <input type="password" class="form-control" id="password" name="j_password" tabindex="1">
	            <span class="help-block"><a href="https://my-account.umn.edu/forgot-password"><i class="fa fa-key" aria-hidden="true"></i>Reset your password</a></span>
                  </div>
	            <button type="submit" class="idp3_form-submit btn-lg" name="_eventId_proceed" tabindex="1">Sign In</button>
            		  			</form>
	</div>
	<div class="idp3_sidebar col-md-5 col-sm-6">
		
		
		<h2>Get an Account</h2>
		<p>Find the University <a href="https://idp2.shib.umn.edu/idp/umn/getaccount.jsp" class="idp3_sidebar-link">Internet account</a> that's right for you.</p>
	</div>
</div>
		
			</div>
		</main>
		<footer class="umn_footer col-xs-12 text-center" role="contentinfo">
            <div class="umn_footer-help">
                <h2 class="umn_footer-help-title">
                    Need Help?                    <button type="button" id="umn_footer-help-toggle" aria-haspopup="true" aria-expanded="false">
                        <i class="fa fa-eye" aria-hidden="true"></i>
                        <span class="umn_footer-help-text">Show Help Options</span>
                    </button>
                </h2>
                <ul class="umn_footer-help-list list-inline" aria-labelledby="umn_footer-help-toggle">
                    <li>
                        <a href="https://it.umn.edu/help" target="_blank"><i class="fa fa-desktop" aria-hidden="true"></i>Technology Help Website</a>
                    </li>
                    <li>
                        <i class="fa fa-phone" aria-hidden="true"></i>Call 612-301-4357
                    </li>
                    <li>
                        <a href="https://umnprd.service-now.com/nav_to.do?uri=chat/chat.do" target="_blank"><i class="fa fa-comment-o" aria-hidden="true"></i>Chat Online</a>
                    </li>
                    <li>
                        <a href="https://it.umn.edu/help/walk-in" target="_blank"><i class="fa fa-map-marker" aria-hidden="true"></i>Visit Walk-in Locations</a>
                    </li>
                    <li>
                        <a href="mailto:help@umn.edu"><i class="fa fa-envelope-o" aria-hidden="true"></i>Email help@umn.edu</a>
                    </li>
                </ul>
            </div>
            <div class="umn_footer-content">
                <small>
                    &copy; 2016 Regents of the University of Minnesota. All rights reserved. The University of Minnesota is an equal opportunity educator and employer. <a href="http://privacy.umn.edu">Online Privacy Statement</a>
                </small>
                <!--v3.2.1@PRD-->
            </div>
        </footer>
		<script src="/idp/js/jquery.min.js"></script>
		<script src="/idp/js/bootstrap.min.js"></script>
		<script src="/idp/js/bootstrap-accessibility.min.js"></script>
		<script src="/idp/js/umn-sign-in-custom.js"></script>
	</body>
</html>