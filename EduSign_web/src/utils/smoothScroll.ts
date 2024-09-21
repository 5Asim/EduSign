export function initSmoothScroll() {
	document.querySelectorAll('a[href^="#"]').forEach(anchor => {
		anchor.addEventListener('click', function (this: HTMLAnchorElement, e) {
		e.preventDefault();
  
		const targetId = this.getAttribute('href')!.substring(1);
		const targetElement = document.getElementById(targetId);
  
		if (targetElement) {
			const navbarHeight = 80; // Adjust this value based on your navbar height
			const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
  
			window.scrollTo({
			top: targetPosition,
			behavior: 'smooth'
			});
		}
		});
	});
  }