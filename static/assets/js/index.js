$(document).ready(function () {
    $("#get-year").html(new Date().getFullYear())

    $(".item").click(chooseQuantity)

    $(".add-to-cart").click(addToCart)
});

const chooseQuantity = (e) => {
    const idProduct = $(e.target).closest('div').data("id")
    const title = $(e.target).closest('div').find(".name")[0]
    const modelTitle = $(".modal-title")[0]
    $(modelTitle).html($(title).text())
    $("#id-product").val(idProduct)
    $("#product-modal").modal('show')
}

const addToCart = () => {
    console.log("adding to cart...")
    const param = {
        id: $("#id-product").val(),
        quantity: $("#quantity").val(),
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
    }
    $.ajax({
        type: "POST",
        url: "../cart/add",
        data: param,
        dataType: "json",
        success: function (response) {
            console.log(response.message)
            $("#product-modal").modal('hide')
        }
    });
}