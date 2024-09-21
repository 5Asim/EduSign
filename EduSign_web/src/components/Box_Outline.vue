<template>
	<div class="Box">
			<div class="box-text">
				<p class="heading">{{ heading }}</p>
				<p class="body">{{ body }}</p>
			</div>
			<div>
				<img  src="./icons/logo.png" alt="" width="200" height="200">
			</div>

	</div>

</template>
      

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'BoxOutlineComponent',
  props: {
    heading: {
      type: String,
      required: true,
    },
    body: {
      type: String,
      required: true,
    },
    src: {
      type: String,
      required: true,
    },
  },

});
</script>

<style scoped>
	.Box{
		display: flex;
		flex-direction: row;
		width: 650px;
		height: 380px;
		gap: 30px;
		justify-content: space-around;
		align-items: center;
		border-radius: 50px; /* Ensures rounded corners */
		padding-left: 40px;
		padding-right: 30px;
		padding-top: 70px;
		padding-bottom: 70px;
		background-color: rgba(36, 26, 74, 1)	;
		

		
		
		
	}

	.box-text{
		display: flex;
		flex-direction: column;
		gap: 40px;
		width: 60%;
	}
	.heading{
		font-size: 48px;
		font-weight: bold;
		font-family: 'Poppins', sans-serif;
		background: linear-gradient(90deg, rgba(104,53,203,1) 0%, rgba(245,193,68,1) 100%);
		-webkit-background-clip: text;
		-webkit-text-fill-color: transparent; 
	}

	.body{
		font-size: 16px;
		font-family: 'Poppins', sans-serif;
		font-weight: lighter;
		color: white;
	}
</style>
