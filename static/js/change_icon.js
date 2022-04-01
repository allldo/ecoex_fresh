    function change_icon() {
            const div_changing = document.getElementById("changing_img");
            const div_block = document.getElementById("Panel")
            div_changing.style.animation = "smooth 0.4s"
            if (div_changing.title === '1') {
                            div_changing.style.backgroundImage = "url(/static/img/header_img/black_icon.png)";
                            div_changing.title = '3';
                            div_changing.style.transform = "rotate(45deg)"
                div_block.style.display = 'flex';
                return
              }
            if (div_changing.title === '3'){
               div_changing.style.backgroundImage = "url(/static/img/header_img/white_icon.png)";
               div_changing.title = '1';
               div_changing.style.transform = "rotate(180deg)"
                div_block.style.display = 'none'

            }
        }