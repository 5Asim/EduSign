<template>
	<div class="homepage">
		<!-- Background video -->
		<video autoplay muted loop class="background-video">
		<!-- Static file referenced from the public directory -->
		<source src="/videos/DigitalHealth.mp4" type="video/mp4" />
		Your browser does not support the video tag.
		</video>
	
		<!-- Overlay text -->
		<div class="overlay-text">
		<h1>Welcome to My Website</h1>
		<p>Engage with stunning experiences</p>
		<button>Install Now</button>


		</div>
	</div>
	<div></div>
      </template>
      
      

<script lang="ts">
import { defineComponent } from 'vue';


	export default defineComponent({
		name: 'DashboardComponent',
		
		
	})
</script>

<style scoped>
.homepage {
  position: relative;
  width: 100vw;
  height: 100vh;
  overflow: hidden;
}

.background-video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  object-fit: cover; /* Ensures the video covers the screen without distortion */
  z-index: 1; /* Places video behind the text */
}

.overlay-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* Centers the text */
  color: black;
  text-align: center;
  z-index: +1; /* Ensures the text is on top of the video */
}

.overlay-text h1 {
	font-family: 'Poppins', sans-serif;
  font-size: 72px;
  font-weight: 700;
  margin: 0;
}

.overlay-text p {
	font-family: 'Poppins', sans-serif;
  font-size: 32px;
  font-weight: 400;
}

button {
	--b: 3px; /* border thickness */
	--s: 0.15em; /* size of the corner */
	--c: black;
      
	padding: calc(0.05em + var(--s)) calc(0.3em + var(--s));
	color: var(--c);
	--_p: var(--s);
	background: conic-gradient(
		from 90deg at var(--b) var(--b),
		#0000 90deg,
		var(--c) 0
		)
		var(--_p) var(--_p) / calc(100% - var(--b) - 2 * var(--_p))
		calc(100% - var(--b) - 2 * var(--_p));
	transition: 0.3s linear, color 0s, background-color 0s;
	outline: var(--b) solid #0000;
	outline-offset: 0.2em;
	font-family: system-ui, sans-serif;
	font-weight: bold;
	font-size: 4rem;
	cursor: pointer;
	border: none;
	margin: 0.1em;
      }
      
      button:hover,
      button:focus-visible {
	--_p: 0px;
	outline-color: var(--c);
	outline-offset: 0.05em;
      }
      
      button:active {
	background: var(--c);
	color: #fff;
      }
      
      body {
	height: 100vh;
	margin: 0;
	display: grid;
	grid-template-columns: auto;
	place-content: center;
	background: #daedfb;
      }

</style>
