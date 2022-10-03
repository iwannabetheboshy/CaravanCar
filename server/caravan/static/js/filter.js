
        function checkBatteryLife(name) {
            if (name == 'Гибриды') {
                document.getElementById('filter-active').innerHTML =
                    "{% for item in cars_major %}" +
                        "{% if item.body == 'Гибриды' %}" +
                            "<div class='custom-col px-1'>" +
                                "<img src='{{path}}{{item.image}}' alt='Los Angeles' class='d-block w-100'>" +
                                "<div class='row info'>" +
                                    "<p class='col-6 car-name'>{{ item.car_model }}</p>" +
                                    "<p class='col-6 price'>от {{ item.price }} ₽</p>" +
                                    "<div class='prop car-name'>" +
                                        "<span class='col-2'>{{ item.year }}&nbsp&nbsp</span>" +
                                        "<span class='col-2'>&nbsp{{ item.engine }}L&nbsp&nbsp</span>" +
                                        "<span class='col-2 border-0'>&nbsp{{ item.wheel }}&nbsp&nbsp</span>" +
                                        "<p class='col-6 pay border-0'>" +
                                            "<a href=''>Купить!</a>" +
                                        "</p>" +
                                    "</div>" +
                                "</div>" +
                            "</div>" +
                        "{% endif %}" +
                    "{% endfor %}";

                document.getElementById('filter').innerHTML =
                    "{% for item in cars_minor %}" +
                        "{% if item.body == 'Гибриды' %}" +
                            "<div class='custom-col px-1'>" +
                                "<img src='{{path}}{{item.image}}' alt='Los Angeles' class='d-block w-100'>" +
                                "<div class='row info'>" +
                                    "<p class='col-6 car-name'>{{ item.car_model }}</p>" +
                                    "<p class='col-6 price'>от {{ item.price }} ₽</p>" +
                                    "<div class='prop car-name'>" +
                                        "<span class='col-2'>{{ item.year }}&nbsp&nbsp</span>" +
                                        "<span class='col-2'>&nbsp{{ item.engine }}L&nbsp&nbsp</span>" +
                                        "<span class='col-2 border-0'>&nbsp{{ item.wheel }}&nbsp&nbsp</span>" +
                                        "<p class='col-6 pay border-0'>" +
                                            "<a href=''>Купить!</a>" +
                                        "</p>" +
                                    "</div>" +
                                "</div>" +
                            "</div>" +
                        "{% endif %}" +
                    "{% endfor %}";
            }

            else if (name == 'Кроссоверы') {
                document.getElementById('filter-active').innerHTML =
                    "{% for item in cars_major %}" +
                        "{% if item.body == 'Кроссоверы' %}" +
                            "<div class='custom-col px-1'>" +
                                "<img src='{{path}}{{item.image}}' alt='Los Angeles' class='d-block w-100'>" +
                                "<div class='row info'>" +
                                    "<p class='col-6 car-name'>{{ item.car_model }}</p>" +
                                    "<p class='col-6 price'>от {{ item.price }} ₽</p>" +
                                    "<div class='prop car-name'>" +
                                        "<span class='col-2'>{{ item.year }}&nbsp&nbsp</span>" +
                                        "<span class='col-2'>&nbsp{{ item.engine }}L&nbsp&nbsp</span>" +
                                        "<span class='col-2 border-0'>&nbsp{{ item.wheel }}&nbsp&nbsp</span>" +
                                        "<p class='col-6 pay border-0'>" +
                                            "<a href=''>Купить!</a>" +
                                        "</p>" +
                                    "</div>" +
                                "</div>" +
                            "</div>" +
                        "{% endif %}" +
                    "{% endfor %}";

                document.getElementById('filter').innerHTML =
                    "{% for item in cars_minor %}" +
                        "{% if item.body == 'Кроссоверы' %}" +
                            "<div class='custom-col px-1'>" +
                                "<img src='{{path}}{{item.image}}' alt='Los Angeles' class='d-block w-100'>" +
                                "<div class='row info'>" +
                                    "<p class='col-6 car-name'>{{ item.car_model }}</p>" +
                                    "<p class='col-6 price'>от {{ item.price }} ₽</p>" +
                                    "<div class='prop car-name'>" +
                                        "<span class='col-2'>{{ item.year }}&nbsp&nbsp</span>" +
                                        "<span class='col-2'>&nbsp{{ item.engine }}L&nbsp&nbsp</span>" +
                                        "<span class='col-2 border-0'>&nbsp{{ item.wheel }}&nbsp&nbsp</span>" +
                                        "<p class='col-6 pay border-0'>" +
                                            "<a href=''>Купить!</a>" +
                                        "</p>" +
                                    "</div>" +
                                "</div>" +
                            "</div>" +
                        "{% endif %}" +
                    "{% endfor %}";
            }
        }
