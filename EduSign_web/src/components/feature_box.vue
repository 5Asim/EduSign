<template>
	<div class="featureBox" :style="{ backgroundColor: bgcolor, color: textcolor}">
		<div>
			<img :src="src" alt="" width="150" height="150">
		</div>
		<hr class="divider">
		<div class="flex flex-col">
			<p class="font-bold text-xl">{{heading}}</p>
			<p class="font-normal text-md">{{body}}</p>
		</div>
	</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

	export default defineComponent({
		name: 'FeatureBox',

		props: {
			heading: {
				type: String,
				required: true
			},
			body: {
				type: String,
				required: true
			},
			src: {
				type: String,
				required: false
			},
			bgcolor: {
				type: String,
				required: false
			},
			textcolor: {
				type: String,
				required: false
			}
			
		}
	})
</script>

<style>
	.featureBox{
		width: 320px;
		height: 350px;
		border-radius: 20px;
		padding: 20px;
		display: flex;
		flex-direction: column;
		justify-content: center;  /* Center content vertically */
		align-items: center;     /* Center content horizontally */
		text-align: left;
	}

	hr.divider {
		width: 100%; /* Ensure the hr takes up the full width of the container */
		border: 0;
		border-top: 1px solid #e0e0e0;
		margin: 15px 0;
	}
</style>