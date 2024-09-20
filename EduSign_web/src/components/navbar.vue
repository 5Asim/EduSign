<template>
	<nav class="flex justify-between items-center py-4 px-8 bg-gray-100 shadow-md w-full">
		<div class="flex-1">
			<img src="./icons/logo.png" alt="EduSign" class="w-10">
		</div>
		<ul class="flex gap-8 list-none">
			<li><a href="#" class="text-gray-800 font-bold px-2 py-1 transition-colors duration-300 hover:text-blue-500">Home</a></li>
			<li><a href="#" class="text-gray-800 font-bold px-2 py-1 transition-colors duration-300 hover:text-blue-500">How It Works</a></li>
			<li><a href="#" class="text-gray-800 font-bold px-2 py-1 transition-colors duration-300 hover:text-blue-500">Features</a></li>
		</ul>
	</nav>
      </template>
      
<script lang="ts">
      import { defineComponent } from 'vue';
      
      export default defineComponent({
	name: 'AppNavbar',
      });
</script>
      