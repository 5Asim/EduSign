<template>
	<div class="py-2"></div>
	
	<div class="flex flex-col gap-10">
		<div class="flex flex-row items-center justify-center gap-20 fade-in-slide-up">
		<div class="icon-container floating">
		<img src="../components/icons/Barrier.png" alt="AI Barrier" width="350" height="350" />
		</div>
		<div class="w-1/3 flex flex-col gap-4">
		<p class="text-4xl font-extrabold">AI Can Break Down Barriers!</p>
		<p class="text-2xl font-normal">
			With artificial intelligence, we can solve the issues with digital accessibility that hearing-impaired and deaf people face in today's technological world!
		</p>
		</div>
		</div>
		
		<div class="flex flex-row items-center justify-center gap-20 fade-in-slide-up">
		<div class="w-1/3 flex flex-col gap-4">
		<p class="text-4xl font-extrabold">Everybody has a right to digital accessibility!</p>
		<p class="text-2xl font-normal">
			Even if we are not born under equal conditions, digital accessibility is everyone's right with an artificial intelligence supported sign language translator tool.
		</p>
		</div>
		<div class="icon-container floating">
		<img src="../components/icons/Accesibiity.png" alt="Right" width="350" height="350" />
		</div>
		</div>
	</div>
      </template>
      
      
      <script>
      import { defineComponent } from 'vue';
      export default defineComponent({
	name: 'Content_Component',
      });
</script>

<style scoped>
.heading_part {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100vw;
  padding-top: 80px;
}

/* Hover animation for icons */
.icon-container {
  transition: transform 0.3s ease;
}

.icon-container:hover {
  transform: scale(1.1);
}

.floating {
  animation: floating 3s ease-in-out infinite;
}

@keyframes floating {
  0% { transform: translate(0, 0); }
  50% { transform: translate(0, 15px); }
  100% { transform: translate(0, 0); }
}
</style>

      