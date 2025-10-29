document.addEventListener("DOMContentLoaded", () => {
  const typingElement = document.getElementById("typing-text");
  const dynamicStringElement = document.getElementById("dynamic-string");

  if (!typingElement || !dynamicStringElement) return;

  let currentTextIndex = 0;
  let currentCharIndex = 0;
  let isDeleting = false;
  const typingSpeed = 120;
  const deletingSpeed = 50;
  const pauseTime = 2000;

  function typeText() {
    const currentText = texts[currentTextIndex];

    if (isDeleting) {
      const newText = currentText.substring(0, currentCharIndex - 1);
      typingElement.textContent = newText;
      dynamicStringElement.textContent = `"${newText}"`;
      currentCharIndex--;

      if (currentCharIndex === 0) {
        isDeleting = false;
        currentTextIndex = (currentTextIndex + 1) % texts.length;
        setTimeout(typeText, 500);
        return;
      }

      setTimeout(typeText, deletingSpeed);
    } else {
      const newText = currentText.substring(0, currentCharIndex + 1);
      typingElement.textContent = newText;
      dynamicStringElement.textContent = `"${newText}"`;
      currentCharIndex++;

      if (currentCharIndex === currentText.length) {
        isDeleting = true;
        setTimeout(typeText, pauseTime);
        return;
      }

      setTimeout(typeText, typingSpeed);
    }
  }

  typeText();
});
