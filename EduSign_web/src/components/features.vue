<template>
	<div class="features">
		<p class="heading">What's More!!!!!</p>
	<div class="feature">
		<Box 
		heading="Career Opportunities" 
		body="Showcase talents, gain hands-on experience, and develop crucial skills like problem-solving and teamwork for career success." 
		src="./icons/logo.png" 
		backgroundGradient="white" />
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
		
		
	</div>
</div>
</template>


<script lang="ts">
	import { defineComponent } from 'vue';
	import Box from './Box.vue';
	import BoxOutline from './Box_Outline.vue';
	export default defineComponent({
		name: 'FeaturesComponent',
		components: {
			Box,
			BoxOutline
		}
	})
</script>

<style scoped>
	.features{
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		gap: 40px;
		
		width: 100vw;
		min-height: 100vh;
		padding-top: 20px;
	}
	.feature {
		display: flex;
		justify-content:center ;
		align-items: center;
		gap:50px
	}
	
	.heading {
		
		font-size: 48px;
		font-weight: bold;
		font-family: 'Poppins', sans-serif;
		text-align: center;
		/* Make sure the gradient applies to a larger area */
		background: linear-gradient(90deg, rgba(104,53,203,1) 0%, rgba(245,193,68,1) 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent;
		
		
	
	}

</style>