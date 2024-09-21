<template>
	<nav class="relative flex justify-between items-center py-4 px-8 bg-white shadow-md w-full">
		<div class="flex items-center space-x-4">
			<img src="./icons/logo.png" alt="EduSign" class="w-14 h-auto">
			
		</div>
		<ul class="hidden md:flex gap-8 list-none">
			<li><a href="#one" class="text-gray-800 font-semibold px-3 py-2 rounded-lg transition-colors duration-300 hover:text-white hover:bg-pink-700">Home</a></li>
			<li><a href="#two" class="text-gray-800 font-semibold px-3 py-2 rounded-lg transition-colors duration-300 hover:text-white hover:bg-pink-700">Features</a></li>
			<li><a href="#three" class="text-gray-800 font-semibold px-3 py-2 rounded-lg transition-colors duration-300 hover:text-white hover:bg-pink-700">About</a></li>
		</ul>
 
		<!-- Hamburger Menu for Mobile -->
		<button @click="toggleMenu" class="md:hidden focus:outline-none">
			<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
				<path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
			</svg>
		</button>
		<!-- Dropdown Menu for Mobile -->
		<div v-if="isMenuOpen" class="absolute top-16 left-0 w-full bg-white shadow-md md:hidden">
			<ul class="flex flex-col gap-4 p-4 list-none">
				<li><a href="#one" class="text-gray-800 font-semibold px-3 py-2 transition-colors duration-300 hover:text-blue-500">Home</a></li>
				<li><a href="#two" class="text-gray-800 font-semibold px-3 py-2 transition-colors duration-300 hover:text-blue-500">Features</a></li>
				<li><a href="#three" class="text-gray-800 font-semibold px-3 py-2 transition-colors duration-300 hover:text-blue-500">About</a></li>
			</ul>
		</div>
	</nav>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
	name: 'AppNavbar',
	setup() {
		const isMenuOpen = ref(false);
		const toggleMenu = () => {
			isMenuOpen.value = !isMenuOpen.value;
		};
		return { isMenuOpen, toggleMenu };
	},
});
</script>

<style scoped>
nav {
	z-index: 1000;
	background-color: #f9fafb; /* Lighter background */
}
@media (max-width: 768px) {
	nav ul {
		display: none;
	}
}
</style>
