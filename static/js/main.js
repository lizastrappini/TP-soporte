const loginModal = document.querySelector(".login-modal");
const userBtn = document.querySelector(".user-btn");
const closeModalBtn = document.querySelector(".close-modal-btn");
const overlay = document.querySelector(".overlay");
const userDisplayer = userBtn.parentElement;
const viewProductBtnList = document.querySelectorAll(".view-product-btn");
const productosSection = document.querySelector(".productos");
const viewProductOverlayList = productosSection.querySelectorAll(".overlay");

if (!userBtn.classList.contains("logged")) {
    userBtn.addEventListener("click", () => {
        loginModal.classList.add("active");
        overlay.classList.add("d-block");
    });
    userDisplayer.classList.remove("active");
}

closeModalBtn.addEventListener("click", () => {
    loginModal.classList.remove("active");
    overlay.classList.remove("d-block");
});

overlay.addEventListener("click", e => {
    if (e.target === overlay) {
        loginModal.classList.remove("active");
        overlay.classList.remove("d-block");
    }
});

viewProductBtnList.forEach(btn => {

    btn.addEventListener("click", e => {
        const idProducto = e.target.parentElement.id;
        const overlayProducto = document.querySelector(`#o-${idProducto}`);
        const productoModal = overlayProducto.firstElementChild;
        productoModal.classList.add("active");
        overlayProducto.classList.add("d-block");
    });

});

viewProductOverlayList.forEach(ol => {

    const productoModal = ol.firstElementChild;
    const closeBtn = productoModal.querySelector(".close-modal-btn");
    const tallesBtnBox = productoModal.querySelector(".talles-btn-box");
    const tallesRadioBtnList = tallesBtnBox.querySelectorAll("input");
    const addProductBtn = productoModal.querySelector(".add-product-btn");

    tallesRadioBtnList.forEach(rb => {
        rb.addEventListener("change", ()=>{
            addProductBtn.removeAttribute("disabled");
        });
    });

    closeBtn.addEventListener("click", () => {
        productoModal.classList.remove("active");
        ol.classList.remove("d-block");
        tallesRadioBtnList.forEach(rb => rb.checked = false);
        addProductBtn.setAttribute("disabled", "true");
    });

    ol.addEventListener("click", e => {
        if (e.target === ol) {
            productoModal.classList.remove("active");
            ol.classList.remove("d-block");
            tallesRadioBtnList.forEach(rb => rb.checked = false);
            addProductBtn.setAttribute("disabled", "true");
        }
    });

});