console.log('Loading posts.js');
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');
    // Get menu items buttons/links
    const menuItems = document.querySelectorAll('.x-link');
    const pages = document.querySelectorAll('.x-page');

    // Hide all pages
    pages.forEach(function(page) {
        console.log('Hiding page', page);
        page.style.display = 'none';
    });

    // Add event listeners to menu items
    menuItems.forEach(function(item) {
        item.addEventListener('click', function(event) {
            // Prevent the default action of the link
            //event.preventDefault();
            console.log('Clicked on menu item')

            // Get the target DIV to hide/unhide
            const targetDivId = item.dataset.target;
            const targetDiv = document.getElementById(targetDivId);

            
        });
    });
});
