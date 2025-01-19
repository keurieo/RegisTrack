document.addEventListener('DOMContentLoaded', function() {
    const items = document.querySelectorAll('.timeline-item');
  
    items.forEach(item => {
      item.addEventListener('mouseenter', function() {
        item.querySelector('.timeline-content').style.transform = 'scale(1.05)';
      });
      
      item.addEventListener('mouseleave', function() {
        item.querySelector('.timeline-content').style.transform = 'scale(1)';
      });
    });
  });
  