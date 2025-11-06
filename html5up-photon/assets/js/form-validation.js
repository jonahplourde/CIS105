// Form Validation and Lightbox JavaScript

(function() {
	'use strict';

	// Form Validation
	function validateForm(formId) {
		const form = document.getElementById(formId);
		if (!form) return;

		const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
		let isValid = true;

		inputs.forEach(input => {
			const errorId = input.id + '-error';
			const errorElement = document.getElementById(errorId);
			
			// Clear previous errors
			if (errorElement) {
				errorElement.textContent = '';
				errorElement.style.display = 'none';
			}

			// Remove error styling
			input.style.borderColor = '';
			
			// Validate field
			if (!input.value.trim()) {
				isValid = false;
				if (errorElement) {
					errorElement.textContent = 'This field is required';
					errorElement.style.display = 'block';
					errorElement.style.color = '#d4af37';
					errorElement.style.fontSize = '0.875em';
					errorElement.style.marginTop = '0.5em';
				}
				input.style.borderColor = '#d4af37';
			}

			// Email validation
			if (input.type === 'email' && input.value.trim()) {
				const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
				if (!emailRegex.test(input.value)) {
					isValid = false;
					if (errorElement) {
						errorElement.textContent = 'Please enter a valid email address';
						errorElement.style.display = 'block';
					}
					input.style.borderColor = '#d4af37';
				}
			}
		});

		return isValid;
	}

	// Contact Form Handler
	const contactForm = document.getElementById('contactForm');
	if (contactForm) {
		contactForm.addEventListener('submit', function(e) {
			e.preventDefault();
			
			const statusDiv = document.getElementById('form-status');
			
			if (validateForm('contactForm')) {
				// Show loading state
				const submitBtn = document.getElementById('submit-btn');
				submitBtn.disabled = true;
				submitBtn.value = 'Sending...';
				statusDiv.innerHTML = '<p style="color: #d4af37;">Sending your message...</p>';

				// Submit to Formspree
				const formData = new FormData(contactForm);
				fetch(contactForm.action, {
					method: 'POST',
					body: formData,
					headers: {
						'Accept': 'application/json'
					}
				})
				.then(response => {
					if (response.ok) {
						statusDiv.innerHTML = '<p style="color: #d4af37;">✓ Thank you! Your message has been sent successfully.</p>';
						contactForm.reset();
					} else {
						throw new Error('Network response was not ok');
					}
				})
				.catch(error => {
					statusDiv.innerHTML = '<p style="color: #d4af37;">There was a problem sending your message. Please try again later or email us directly.</p>';
				})
				.finally(() => {
					submitBtn.disabled = false;
					submitBtn.value = 'Send Message';
				});
			} else {
				statusDiv.innerHTML = '<p style="color: #d4af37;">Please fill in all required fields correctly.</p>';
			}
		});
	}

	// Registration Form Handler
	const registrationForm = document.querySelector('form[action="#"]');
	if (registrationForm && registrationForm.id !== 'contactForm') {
		registrationForm.addEventListener('submit', function(e) {
			e.preventDefault();
			
			if (validateForm(registrationForm.id)) {
				alert('Thank you for your registration! We will contact you shortly.');
				registrationForm.reset();
			}
		});
	}

	// Real-time validation
	const forms = document.querySelectorAll('form');
	forms.forEach(form => {
		const inputs = form.querySelectorAll('input, select, textarea');
		inputs.forEach(input => {
			input.addEventListener('blur', function() {
				const errorId = this.id + '-error';
				const errorElement = document.getElementById(errorId);
				
				if (this.hasAttribute('required') && !this.value.trim()) {
					if (errorElement) {
						errorElement.textContent = 'This field is required';
						errorElement.style.display = 'block';
						this.style.borderColor = '#d4af37';
					}
				} else {
					if (errorElement) {
						errorElement.textContent = '';
						errorElement.style.display = 'none';
					}
					this.style.borderColor = '';
				}

				// Email validation
				if (this.type === 'email' && this.value.trim()) {
					const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
					if (!emailRegex.test(this.value)) {
						if (errorElement) {
							errorElement.textContent = 'Please enter a valid email address';
							errorElement.style.display = 'block';
							this.style.borderColor = '#d4af37';
						}
					}
				}
			});
		});
	});

	// Image Lightbox
	function initLightbox() {
		const images = document.querySelectorAll('.image.fit img, .image img');
		
		images.forEach(img => {
			img.style.cursor = 'pointer';
			img.addEventListener('click', function() {
				openLightbox(this.src, this.alt);
			});
		});
	}

	function openLightbox(imageSrc, imageAlt) {
		// Create lightbox overlay
		const overlay = document.createElement('div');
		overlay.id = 'lightbox-overlay';
		overlay.style.cssText = `
			position: fixed;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			background: rgba(0, 0, 0, 0.9);
			backdrop-filter: blur(10px);
			z-index: 10000;
			display: flex;
			align-items: center;
			justify-content: center;
			cursor: pointer;
			animation: fadeIn 0.3s ease;
		`;

		// Create lightbox image container
		const container = document.createElement('div');
		container.style.cssText = `
			position: relative;
			max-width: 90%;
			max-height: 90%;
			cursor: default;
		`;

		// Create lightbox image
		const img = document.createElement('img');
		img.src = imageSrc;
		img.alt = imageAlt || '';
		img.style.cssText = `
			max-width: 100%;
			max-height: 90vh;
			border-radius: 8px;
			box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
			animation: zoomIn 0.3s ease;
		`;

		// Create close button
		const closeBtn = document.createElement('button');
		closeBtn.innerHTML = '&times;';
		closeBtn.style.cssText = `
			position: absolute;
			top: -40px;
			right: 0;
			background: rgba(212, 175, 55, 0.9);
			border: none;
			color: #2d2d2d;
			font-size: 2.5em;
			width: 50px;
			height: 50px;
			border-radius: 50%;
			cursor: pointer;
			transition: all 0.3s;
			font-weight: bold;
			line-height: 1;
		`;

		closeBtn.addEventListener('mouseenter', function() {
			this.style.background = 'rgba(244, 208, 63, 0.95)';
			this.style.transform = 'scale(1.1)';
		});

		closeBtn.addEventListener('mouseleave', function() {
			this.style.background = 'rgba(212, 175, 55, 0.9)';
			this.style.transform = 'scale(1)';
		});

		container.appendChild(img);
		container.appendChild(closeBtn);
		overlay.appendChild(container);

		// Close handlers
		function closeLightbox() {
			overlay.style.animation = 'fadeOut 0.3s ease';
			setTimeout(() => {
				document.body.removeChild(overlay);
				document.body.style.overflow = '';
			}, 300);
		}

		closeBtn.addEventListener('click', closeLightbox);
		overlay.addEventListener('click', function(e) {
			if (e.target === overlay) {
				closeLightbox();
			}
		});

		// ESC key handler
		function handleEsc(e) {
			if (e.key === 'Escape') {
				closeLightbox();
				document.removeEventListener('keydown', handleEsc);
			}
		}
		document.addEventListener('keydown', handleEsc);

		// Add to page
		document.body.appendChild(overlay);
		document.body.style.overflow = 'hidden';

		// Add CSS animations
		if (!document.getElementById('lightbox-styles')) {
			const style = document.createElement('style');
			style.id = 'lightbox-styles';
			style.textContent = `
				@keyframes fadeIn {
					from { opacity: 0; }
					to { opacity: 1; }
				}
				@keyframes fadeOut {
					from { opacity: 1; }
					to { opacity: 0; }
				}
				@keyframes zoomIn {
					from { transform: scale(0.8); opacity: 0; }
					to { transform: scale(1); opacity: 1; }
				}
				.error-message {
					display: none;
					color: #d4af37;
					font-size: 0.875em;
					margin-top: 0.5em;
				}
			`;
			document.head.appendChild(style);
		}
	}

	// Initialize lightbox when DOM is ready
	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', initLightbox);
	} else {
		initLightbox();
	}

})();

