odoo.define('zts_web_reference_slider.reference', function (require) {
    "use strict";

    console.log("loaded");

    $(document).ready(function() {
            $("#reference_carousel").owlCarousel({
                loop: true,
                center: true,
                items: 5,
                margin: 10,
                autoplay: true,
                dots:true,
                nav:true,
                autoplayTimeout: 8500,
                smartSpeed: 450,
                navText: ['<i class="fa fa-angle-left"></i>','<i class="fa fa-angle-right"></i>'],
                responsive: {
                    0: {
                        items: 1
                    },
                    768: {
                        items: 3
                    },
                    1170: {
                        items: 5
                    }
                }
                });

        });
});
