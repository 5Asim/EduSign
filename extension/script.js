document.addEventListener('DOMContentLoaded', function() {
    const hearingLevelInput = document.getElementById('hearingLevel');
    const signLiteracyInput = document.getElementById('signLiteracy');
    const hearingLevelValue = document.getElementById('hearingLevelValue');
    const signLiteracyValue = document.getElementById('signLiteracyValue');
  
    // Display slider values
    hearingLevelInput.addEventListener('input', function() {
      hearingLevelValue.textContent = hearingLevelInput.value;
    });
  
    signLiteracyInput.addEventListener('input', function() {
      signLiteracyValue.textContent = signLiteracyInput.value;
    });
  
    // Handle form submission
    document.getElementById('configForm').addEventListener('submit', function(event) {
      event.preventDefault();
  
      // Get values from form
      const hearingLevel = parseInt(hearingLevelInput.value);
      const comprehension = document.getElementById('comprehension').value;
      const signLiteracy = parseInt(signLiteracyInput.value);
      const educationLevel = document.getElementById('educationLevel').value;
      const age = parseInt(document.getElementById('age').value);
  
      // Basic weighting algorithm suggestion:
      let weights = {
        hearingLevelWeight: hearingLevel / 100,
        comprehensionWeight: comprehension === 'low' ? 0.25 : comprehension === 'moderate' ? 0.5 : 0.75,
        signLiteracyWeight: signLiteracy / 100,
        educationWeight: educationLevel === 'primary' ? 0.25 : educationLevel === 'secondary' ? 0.5 : 0.75,
        ageWeight: age / 100
      };
  
      console.log("Calculated Weights:", weights);
      
      // Apply any further logic or save settings as needed
      alert('Settings Saved Successfully');
    });
  });
  