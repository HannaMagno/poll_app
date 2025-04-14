function typeText(element, text, speed = 100) {
    let index = 0;
    element.style.opacity = '1';
    
    function type() {
        if (index < text.length) {
            element.textContent += text.charAt(index);
            index++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

document.addEventListener('DOMContentLoaded', function() {
    const typingElement = document.querySelector('.typing-text');
    if (typingElement) {
        const text = typingElement.textContent;
        typingElement.textContent = '';
        typingElement.style.opacity = '0';
        
        // Add cursor element
        const cursor = document.createElement('span');
        cursor.className = 'cursor';
        typingElement.parentNode.appendChild(cursor);
        
        // Start typing after a short delay
        setTimeout(() => {
            typeText(typingElement, text);
        }, 500);
    }
});
