<script lang="ts">
import AppNavbar from '../components/navbar.vue'
import Dashboard from '@/components/dashboard.vue';
import Features from '@/components/features.vue';
import { defineComponent } from 'vue';



	export default defineComponent({
		name: 'Home_Page',
		components: {
			AppNavbar,
			Dashboard,
			Features
		},
		props:{

		}
	})
</script>


<template>
	<AppNavbar/>
	<div class="page">
		
		<div class="dashboard">
			<Dashboard/>
		</div>
		<div class="features">
			
			<Features/>
		</div>

	</div>
</template>

<style>
	.page {
		display: flex;
		flex-direction: column;
		gap: 50px;
		align-items: center;
		background-color: rgba(17, 12, 36, 1);
		
	}

	.dashboard {
			background: transparent; /* Ensure the dashboard has no background */
			width: 100%; /* Optional: Make sure it spans the width */
	}
</style>

