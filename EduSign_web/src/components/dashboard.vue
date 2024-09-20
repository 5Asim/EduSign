<template>
	<div>
		<div class="">
			<p class="font-roboto text-lg">{{heading}}</p>
			<p class="font-roboto text-sm">{{body}}</p>
		</div>
		<div>
			<img :src="src" alt="">
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'DashboardComponent',
		props: {
			heading:{
				type: String,
				required: true
			},
			body:{
				type: String,
				required: true
			},
			src:{
				type: String,
				required: true
			}
		}
	})
</script>

<style scoped>
</style>