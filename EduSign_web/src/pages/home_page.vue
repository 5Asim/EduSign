<script lang="ts">
import AppNavbar from '../components/navbar.vue'
import DashboardComponent from '../components/dashboard.vue'
import { defineComponent } from 'vue';



	export default defineComponent({
		name: 'Home_Page',
		components: {
			AppNavbar,
			DashboardComponent
		},
		props:{

		}
	})
</script>


<template>
	<div>
		<AppNavbar/>
		<div>
			<DashboardComponent heading="Heading" body="Body" src="../components/icons/convert.png"/>
			
			

		</div>

	</div>
</template>

