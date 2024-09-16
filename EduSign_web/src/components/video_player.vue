<template>
	<div class="video-container">
		<video
			ref="videoPlayer"
			:src="src"
			:width="width"
			:height="height"
			controls
			@play="playBoth"
			@pause="pauseBoth"
			@seeked="syncVideos"
		></video>

		<div class="video-controls">
			<img
				src="@/components/icons/convert.png"
				alt="Convert"
				class="control-icon edu-sign"
				@click="showSecondVideo"
			/>
		</div>

		<div v-if="showVideo" class="second-video-container">
			<video
				ref="secondVideoPlayer"
				:src="secondSrc"
				width="150"
				height="150"
				muted
				@loadeddata="syncVideos"
			></video>
		</div>
	</div>
</template>

<script lang="ts">
	import { defineComponent, ref, onMounted } from 'vue';

	export default defineComponent({
		name: 'VideoPlayer',

		props: {
			src: {
				type: String,
				required: true,
			},
			secondSrc: {
				type: String,
				default:
					'https://www.w3schools.com/html/mov_bbb.mp4',
			},
			width: {
				type: Number,
				default: 640,
			},
			height: {
				type: Number,
				default: 360,
			},
		},
		setup() {
			const videoPlayer = ref<HTMLVideoElement | null>(null);
			const secondVideoPlayer = ref<HTMLVideoElement | null>(null);
			const showVideo = ref(false); 

			const showSecondVideo = () => {
				showVideo.value = true;
				videoPlayer.value?.pause(); 
				syncVideos(); 
			};

			const syncVideos = () => {
				if (videoPlayer.value && secondVideoPlayer.value) {
					secondVideoPlayer.value.currentTime = videoPlayer.value.currentTime;
				}
			};

			const playBoth = () => {
				if (secondVideoPlayer.value) {
					secondVideoPlayer.value.play();
				}
			};

			const pauseBoth = () => {
				if (secondVideoPlayer.value) {
					secondVideoPlayer.value.pause();
				}
			};

			onMounted(() => {
				if (secondVideoPlayer.value) {
					secondVideoPlayer.value.pause();
				}
			});

			return {
				videoPlayer,
				secondVideoPlayer,
				showVideo,
				showSecondVideo,
				syncVideos,
				playBoth,
				pauseBoth,
			};
		},
	});
</script>

<style scoped>
	.video-container {
		position: relative;
		width: fit-content;
		margin: auto;
	}

	.video-controls {
		position: absolute;
		top: 0;
		right: 0;
		padding: 10px;
		z-index: 10; /* Ensure the button is above other content */
	}

	.control-icon {
		width: 25px;
		height: 25px;
		cursor: pointer;
	}

	.control-icon:hover {
		opacity: 0.7;
	}

	.edu-sign {
		position: absolute;
		top: 10px;
		right: 10px;
	}

	.second-video-container {
		position: absolute;
		bottom: 30px;
		right: 10px; 
		 /* Ensure the second video is below the controls */
	}

	/* Hide fullscreen button using CSS */
	video::-webkit-media-controls-fullscreen-button {
		display: none;
	}
	video::-moz-media-controls-fullscreen-button {
		display: none;
	}
	video::-ms-media-controls-fullscreen-button {
		display: none;
	}
	video::media-controls-fullscreen-button {
		display: none;
	}
</style>
