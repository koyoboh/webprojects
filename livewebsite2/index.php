<!DOCTYPE html>
<html>
<head>
	<script id="Cookiebot" src="https://consent.cookiebot.com/uc.js" data-cbid="70ef37b2-2efc-4d4e-8d49-8e103bc331b8" data-blockingmode="auto" type="text/javascript"></script>
	<meta charset="utf-8">
	<meta name="viewport" content="width-device-width, initial-scale=1">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Jura&display=swap" rel="stylesheet">
	<link rel="stylesheet" type="text/css" href="css/thenisda.css">
	<link rel = "shortcut icon" href ="image/sft.ico"  type = "image/ico">
	<meta name="description" content="DJ | Producer | Sound Engineer based in London, UK">
	

	<title>Thenisda World</title>
</head>

<!-- header logo -->

<div style="background-color: #000;">
	<a href="index.php"><img src="image/sft2.png" alt="thenisda logo" class="toplogo"></a>
</div>

	
<!-- body -->

<body>


<!-- nav bar -->
	
			<div class="topnav" id="myTopnav">
				
			<a href="index.php" class="active"><strong>Home</strong></a>
			<a href="page/music.php">Music</a>
			<a href="page/video.php">Video</a>
			<a href="page/contact.php">Contact</a>
			
			<div class="dropdown">
				<button class="dropbtn"><em>News</em> <i class="fa fa-caret-down"></i></button>
				<div class="dropdown-content">
					<a href="newrelease/newmusic.php">New Music</a>
					<a href="newrelease/newvideo.php">New Video</a>
				</div>
			</div>
			<a href="javascript:void(0);" class="icon"; onclick="myMenu()";>
				<i class="fa fa-bars"></i>
			</a>
			

		</div>
	
<!-- javascript -->
	<script>
		function myMenu(){
			var x = document.getElementById("myTopnav");
			if(x.className === "topnav") {
				x.className += " responsive";
			} else {
				x.className = "topnav";
			}
		};




	</script>
	
<!-- side banner -->
	<div class="sdsBanner"
		style="position: sticky; top: 0; 
		position: -webkit-sticky;
		margin-bottom: 0px; 
		margin-top: 0px;
		text-align: center;
		font-size: 30px;
		padding: 5px 5px;
		background-color: #000;
		color: #fff;
		z-index: 2;
		" 

	>SOUND<small><em> Detect </em></small>SOUND</div>

	<div class="sdsBanner"
		style="position: static;  
		margin-bottom: 50px;
		margin-top: 0px; 
		text-align: center;
		font-size: 20px;
		padding: 20px;
		background-color: #ffcc00;
		color: #000;
		" 

	>Beats | Instrumentals | Dubs</div>

	<button onclick="darkMode()" class="darkMode"><p id="dark">Change Mode</p></button>
	
	
	<p id="light">Light Mode</p>
	<p id="dark1"></p>

	<div style="text-align: center;">
		<div>PEACE TO YOU AND YOURS</div>
		<h2><small>Thenisda is a London based producer and sound engineer from the Smiling Coast (West Africa). Thenisda sound is unorthodoxly unique. It's polished and preserved with very low bottom frequencies and intricate melodies of Afro rhythms and reggae basslines.</small></h2>
		<h2><small>All tracks are produced by Thenisda and are available to purchase or lease.</small></h2>
		<p>See below for latest <strong>Dub, Instrumental and Beats</strong> </p>
	</div>
	
	
	
<!-- script to change body to light or dark mode -->
	<script>
		function darkMode(){
			var l = document.getElementById("light");
			var d = document.getElementById("dark1")
			var  element = document.body;
			element.classList.toggle("darkmode");
			
			if(l.style.display === "none"){
				l.style.display = "block";

			} else {
				l.style.display = "none";
			}
			d.innerHTML = "The Energy Is Dark-Mode";


	

		}

		

	</script>
	
<!-- music content -->

<div class="beats" >

		<div class="b1">
			<h3>Beats For Sale</h3>
			<h1>New Release</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"Pom"</h2>
				<div class="forplayer">

						<button onclick="naPlayer01()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer01">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/pom.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer01(){
								var p = document.getElementById("getnaplayer01");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							



						</script>

						</div>

						
			</div>



				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Contact me if you would like to use. Exclusive or Non - Exclusive.
				Available in mp3, wav and stems.
				<small> Then </small>
			</p>
		
			
		</div>

		<div class="b2">
			<h3>Beats For Sale</h3>
			<h1>New Release</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"Still At Peace"</h2>
				<div class="forplayer">

						<button onclick="naPlayer02()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>
						
						

						<div id="getnaplayer02">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/stillatpeace.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer02(){
								var p = document.getElementById("getnaplayer02");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							



						</script>

						</div>

						

			</div>

				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Contact me if you would like to use. Exclusive or Non - Exclusive.
				Available in mp3, wav and stems.
				<small> Then </small>
			</p>

		</div>

		<div class="b1">
			<h3>Beats For Sale</h3>
			<h1>New Release</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"Ritual Of Thee"</h2>
				<div class="forplayer">

						<button onclick="naPlayer03()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer03">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/rot.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer03(){
								var p = document.getElementById("getnaplayer03");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							

						</script>

						</div>


			</div>
				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Contact me if you would like to use. Exclusive or Non - Exclusive.
				Available in mp3, wav and stems.
				<small> Then </small>
			</p>

		</div>

		<div class="b2">
			<h3>Beats For Sale</h3>
			<h1>New Release</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"Sea Spirits"</h2>
				<div class="forplayer">

						<button onclick="naPlayer04()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer04">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/ss.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer04(){
								var p = document.getElementById("getnaplayer04");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							

						</script>

						</div>

						

			</div>
				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Contact me if you would like to use. Exclusive or Non - Exclusive.
				Available in mp3, wav and stems.
				<small> Then </small>
			</p>
			

		</div>

		<div class="b1">

			<h3>Streaming</h3>
			<h1>New Release</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"Wisdom Steel"</h2>
				<div class="forplayer">

						<button onclick="naPlayer05()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer05">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/wisdomsteel.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer05(){
								var p = document.getElementById("getnaplayer05");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							

						</script>

						</div>

						

			</div>
				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				From the album 'Sound from Thenisda'.
				Streaming everywhere.
				<small> Then </small>
			</p>
			




			
		</div>

		<div class="b2">
			<h3>Thenisda Music</h3>
			<h1 style="color: red">Sold</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"In Bass We Trust"</h2>
				<div class="forplayer">

						<button onclick="naPlayer06()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer06">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/inbasswetrust.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer06(){
								var p = document.getElementById("getnaplayer06");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							

						</script>

						</div>

						

			</div>
				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Not Available for Purchase.
				<small> Then </small>
			</p>

		</div>

		<div class="b1">
			<h3>Thenisda Music</h3>
			<h1>For Sale</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"23 Enigma"</h2>
				<div class="forplayer">

						<button onclick="naPlayer07()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer07">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/23e.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer07(){
								var p = document.getElementById("getnaplayer07");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							

						</script>

						</div>

						

			</div>
				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Contact me if you would like to use. Exclusive or Non - Exclusive.
				Available in mp3, wav and stems.
				<small> Then </small>
			</p>

		</div>

		<div class="b2">
			<h3>Beats For Sale</h3>
			<h1>New Release</h1>
				<div><img src="image/soundtrack.png" alt="photo" class="sideImage"></div>
				<h2>"Eternal Energies"</h2>
				<div class="forplayer">

						<button onclick="naPlayer08()" class="audioButton">Hide Player</button>
						<button class="audioButton"><a href="../page/contact.php" class="inner-a">Email</a></button><br><br>

						<div id="getnaplayer08">
						<audio  controls controlslist="nodownload" class="adp">
							<source src="song/ee.mp3" type="audio/mp3">
							Your browser does not support HTML5 Audio.
						</audio><br><br>

						<script>
							function naPlayer08(){
								var p = document.getElementById("getnaplayer08");
								if(p.style.display === "none") {
									p.style.display = "block";
								} else {
									p.style.display = "none";
								}
							}
							

						</script>

						</div>

						

			</div>
				<h5>Producer: <em >Thenisda</em></h5>
				<h5>Original Productions</h5>
			<p>
				Contact me if you would like to use. Exclusive or Non - Exclusive.
				Available in mp3, wav and stems.
				<small> Then </small>
			</p>

		</div>
			
			
</div>
	

	


<div style="color: #000;background-color: #fff; text-align: center; padding: 20px;
		margin-bottom: 0px; 

		" >
			<H1>MUSIC</H1>
			<small>Music Uplift Souls In Communities</small>
		</div>

		


<div style="

		position: sticky; bottom: 0;
		position: -webkit-sticky; 
		margin-bottom: 0px; 
		margin-top: 100px;
		max-width: 100%;
		text-align: center;
		background-color: #000;


		 " >
		 <div onclick="spotLink()">
		 	<a href="https://open.spotify.com/album/3KBZNk16OjBU9GZgrHvtei?si=F-_RB3R2TZOjH2G6damaSQ&nd=1">
		 		<img src="image/spotify.png"  class="mediaLogos">
		 	</a>

		
		</div>
		

</div>

<div style="background-color: #fff; color: #990000; padding: 20px; text-align: center;"><a  style="text-decoration: none;" class="footer-a" >COIVID IS REAL <small>Stay Safe!</small></a></div>




	<footer class="footer" style="position: sticky; margin-top: 0;position: -webkit-sticky">

		<div class="footer-row">

		

		<div class="footer-social">
		<h3>Social</h3>
		<p>
			<a href="https://www.facebook.com/koyoboh" class="fa fa-facebook" id="Socials" style="font-size: 30px; text-decoration: none; padding: 10px 10px;
			color: #191919; margin: 5px 2px;" ></a>
			<a href="https://www.instagram.com/koyoboh" id="Socials" class="fa fa-instagram" style="font-size: 30px; text-decoration: none; padding: 10px 10px;
			color: #191919; margin: 5px 2px;"></a>
			<a href="https://www.twitter.com/koyoboh" class="fa fa-twitter" id="Socials" style="font-size: 30px; text-decoration: none; padding: 10px 10px;
			color: #191919; margin: 5px 2px;"></a>
			

		</p>

		<h5>Drop Me A Message For Collaborations</h5>
		<h4>Contact Me</h4>
		<button onclick="dropMess()" id="dropmess" class="audioButton">See Email</button>
		<script >
			function dropMess(){
				document.getElementById("dropmess").innerHTML = "info@thenisda.com";
			
			}
		</script>

		

		</div>
		
		<div class="footer-music">
		<h3>Music</h3>
			
			<a href="https://www.beatstars.com/thenisda/tracks?type=all" class="footer-a"><h5 class="footer-music-link">Beats For Sale</h5></a>
			<a href="https://www.beatstars.com/thenisda/tracks?type=all" class="footer-a"><h5 class="footer-music-link">Instrumentals For Sale</h5></a>
			<a href="https://www.beatstars.com/thenisda/tracks?type=all" class="footer-a"><h5 class="footer-music-link">Dubs For Sale</h5></a>
			

		</div>

		<div class="footer-new">
		<h3>New Release</h3>
			
			<a href="newrelease/newmusic.php" class="footer-a" class="footer-a"><h5 class="footer-music-link">New Music</h5></a>
			<a href="newrelease/newvideo.php" class="footer-a" class="footer-a"><h5 class="footer-music-link">New Video</h5></a>
		

		</div>

		<div class="footer-contact">
				<h3>Web Designs</h3>
				<small> &copy; 2021  Thenisda  </small><br><br>
				<small> Designs By Koyoboh  </small><br><br>
		
				<a href="https://www.koyoboh.co.uk"><img src="image/koyobologo.png" alt="koyobohlogo" 
				 
				style="max-width: 100px;
				height: auto;
				
				"
				></a> <br><br>
				<button onclick="london()" id="seeWorks" class="audioButton">Designs</button>


		</div>

		

		</div>

	</footer>
	<div style="
 
		margin-bottom: 0px; 
		margin-top: 0px;
		text-align: center;
		font-size: 40px;
		padding: 20px;
		background-color: #000;
		background-image: url(image/de.jpg);
		background-repeat: no-repeat;
		background-size: contain;
		color: #fff;
		width: 100%;
		height: auto;



"><h6></h6>
 </div>
<script src="thenscript.js"></script>
</body>
</html>
