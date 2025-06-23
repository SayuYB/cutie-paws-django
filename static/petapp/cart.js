<script>
    document.addEventListener("DOMContentLoaded", function() {
        // Get all elements with class "addtocart"
        var addToCartButtons = document.querySelectorAll('.addtocart');

        // Add click event listener to each button
        addToCartButtons.forEach(function(button) {
            button.addEventListener('click', function() {
                // Extract the product ID from the button's ID attribute
                var productId = button.id.split('_')[1];

                // Send a POST request to the server with the product ID
                fetch('/add-to-cart/' + productId, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': '{{ csrf_token }}', // Add CSRF token for security
                        'Content-Type': 'application/json'
                    }
                }).then(function(response) {
                    if (response.ok) {
                        // Product successfully added to cart, update UI accordingly
                        alert('Product added to cart!');
                        // You can add more UI update logic here if needed
                    } else {
                        // Handle error response from server
                        alert('Error adding product to cart');
                    }
                }).catch(function(error) {
                    console.error('Error:', error);
                });
            });
        });
    });
</script>
