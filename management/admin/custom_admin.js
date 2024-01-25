// static/admin/custom_admin.js
(function($) {
    $(document).ready(function() {
        const searchInput = $('#searchbar input[type="text"]');
        
        searchInput.on('input', function() {
            const searchText = $(this).val().toLowerCase();
            $('#result_list tbody tr').each(function() {
                const rowText = $(this).text().toLowerCase();
                if (rowText.includes(searchText)) {
                    $(this).show();
                } else {
                    $(this).hide();
                }
            });
        });
    });
})(django.jQuery);
