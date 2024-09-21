<template>
	<div class="feature_page">
	<div class="features">
		<p class="font-bold text-6xl">Empowering Education Through Accessibility</p>
		<p class="font-bold text-6xl">Making Learning Open to All</p>
		<p class="text-xl font-normal py-8">We give a voice to the voiceless by translating educational materials for the deaf, ensuring equal access to knowledge and fostering inclusivity.</p>
	</div>
	<div class="flex flex-row items-center justify-center gap-8">
		<Feature_box heading=" Real-time Sign-Language Translation" body="Showcase talents, gain hands-on experience, and develop crucial skills" bgcolor="rgba(94, 204, 160, 1)" :src="RealTime"/>
		<Feature_box heading=" Cross platform integration" body="Showcase talents, gain hands-on experience, and develop crucial skills" bgcolor="rgba(10, 10, 10, 1)" textcolor="white" :src="social"/>
		<Feature_box heading=" Script translation" body="Showcase talents, gain hands-on experience, and develop crucial skills" bgcolor="rgba(203, 155, 250, 1)"  :src="Signn"/>
		<Feature_box heading=" Communication Interface" body="Showcase talents, gain hands-on experience, and develop crucial skills" bgcolor="rgba(209, 59, 125, 1)"  :src="Interface"/>
	</div>
</div>
		<!-- <div class="feature">
		<Box 
		heading="Career Opportunities" 
		body="Showcase talents, gain hands-on experience, and develop crucial skills like problem-solving and teamwork for career success." 	
		src="./icons/logo.png" 
		backgroundGradient="white" />white
		<BoxOutline 
		heading="Career Opportunities" 
		body="Showcase talents, gain hands-on experience, and develop crucial skills like problem-solving and teamwork for career success." 
		src="./icons/logo.png" 
		backgroundGradient="white" />
		
	</div>
	<div class="feature">
		<BoxOutline 
		heading="Career Opportunities" 
		body="Showcase talents, gain hands-on experience, and develop crucial skills like problem-solving and teamwork for career success." 
		src="./icons/logo.png" 
		backgroundGradient="white" />
		<Box 
		heading="Career Opportunities" 
		body="Showcase talents, gain hands-on experience, and develop crucial skills like problem-solving and teamwork for career success." 
		src="./icons/logo.png" 
		backgroundGradient="white" />
		
		
	</div> -->
</template>


<script lang="ts">
	import { defineComponent } from 'vue';
	import RealTime from './icons/RealTime.png';
	import Interface from './icons/interface.png';
	import Signn from './icons/signnn.png';
	import social from './icons/social.png';
	import Feature_box from './feature_box.vue';
	export default defineComponent({
		name: 'FeaturesComponent',
		components: {
			Feature_box
		},
		data() {
			return {
				RealTime,
				Interface,
				social,
				Signn
			};
		}
	})
</script>

<style scoped>

	.features{
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		width: 100vw;
		padding-top: 80px;
		
	}

	
	.heading {
		
		font-size: 48px;
		font-weight: bold;
		font-family: 'Poppins', sans-serif;
		text-align: center;
		color: black;
		
		
	
	}

	.feature_page{
		display: flex;
		flex-direction: column;
		gap: 80px;
		height: 100vh;
	}

</style>