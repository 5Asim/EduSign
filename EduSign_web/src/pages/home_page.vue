<script lang="ts">
import { defineComponent, ref, onMounted, onUnmounted } from 'vue';
import AppNavbar from '../components/navbar.vue';
import Dashboard from '@/components/dashboard.vue';
import Features from '@/components/features.vue';
import Content_Component from '@/components/content.vue';

export default defineComponent({
  name: 'Home_Page',
  components: {
    AppNavbar,
    Dashboard,
    Features,
    Content_Component
  },
  setup() {
    const stars = ref([]);
    const maxStars = 5;

    const createStar = () => {
      const star = {
        left: `${Math.random() * 100}vw`,
        top: `${Math.random() * 100}vh`,
        animationDuration: `${Math.random() * 1 + 0.5}s`,
      };
      stars.value.push(star);
      if (stars.value.length > maxStars) {
        stars.value.shift();
      }
    };

    const handleScroll = () => {
      if (Math.random() < 0.1) { // 10% chance to create a star on each scroll event
        createStar();
      }
    };

    onMounted(() => {
      window.addEventListener('scroll', handleScroll);
      // Create initial stars
      for (let i = 0; i < maxStars; i++) {
        createStar();
      }
    });

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll);
    });

    return {
      stars,
    };
  },
});
</script>

<template>
  <AppNavbar />
  <div class="page" id="one">
    <div class="dashboard">
      <Dashboard />
    </div>
    <div v-for="(star, index) in stars" :key="index" class="shooting-star" :style="star"></div>

    <div id="two" class="features">
      <Features />
    </div>

    <div id="three" class="goals">
      <!-- Mission Section -->
      <div class="flex flex-row items-center justify-center gap-20 fade-in-slide-up">
        <div class="icon-container floating">
          <img src="../components/icons/mission.png" alt="Mission Icon" width="350" height="350" />
        </div>
        <div class="w-1/3 flex flex-col gap-4">
          <p class="text-4xl font-extrabold">Mission</p>
          <p class="text-2xl font-normal">We aim to remove communication barriers between the deaf and hearing communities, especially in education. Our goal is to make learning accessible for everyone by translating educational videos and materials.</p>
        </div>
      </div>
      <!-- Vision section -->
      <div class="flex flex-row items-center justify-center gap-20 fade-in-slide-up">
        <div class="w-1/3 flex flex-col gap-4">
          <p class="text-4xl font-extrabold">Vision</p>
          <p class="text-2xl font-normal">We aim to remove communication barriers between the deaf and hearing communities, especially in education. Our goal is to make learning accessible for everyone by translating educational videos and materials.</p>
        </div>
        <div class="icon-container floating">
          <img src="../components/icons/vision.png" alt="Vision Icon" width="350" height="350" />
        </div>
      </div>
      <div v-for="(star, index) in stars" :key="index" class="shooting-star" :style="star"></div>
      <div>
        <Content_Component />
      </div>
    </div>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');

.page {
  font-family: 'Roboto Condensed', sans-serif;
  display: flex;
  flex-direction: column;
  gap: 50px;
  align-items: center;
  background: whitesmoke;
  background-size: 400% 400%;
  animation: gradientBG 15s ease infinite;
}

.dashboard {
  background: transparent;
  width: 100%;
}

.goals {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  gap: 40px;
  padding-top: 40px;
}

/* Animation styles */
.fade-in-slide-up {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInSlideUp 1s ease forwards;
}

@keyframes fadeInSlideUp {
  0% {
    opacity: 0;
    transform: translateY(20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Hover and floating animation for icons */
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
  0% { transform: translate(0,  0px); }
  50%  { transform: translate(0, 15px); }
  100%   { transform: translate(0, -0px); }   
}

/* Shooting star styles */
.shooting-star {
  position: fixed;
  width: 4px;
  height: 4px;
  background-color: white;
  border-radius: 50%;
  box-shadow: 0 0 0 4px rgba(255,255,255,0.1),
              0 0 0 8px rgba(255,255,255,0.1),
              0 0 20px rgba(255,255,255,1);
  animation: shoot linear infinite;
  pointer-events: none;
}

@keyframes shoot {
  0% {
    transform: rotate(215deg) translateX(0);
    opacity: 1;
  }
  70% {
    opacity: 1;
  }
  100% {
    transform: rotate(215deg) translateX(100vw);
    opacity: 0;
  }
}

/* Background gradient animation */
@keyframes gradientBG {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>