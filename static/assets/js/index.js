$(document).ready(function () {
    $("#get-year").html(new Date().getFullYear())

    // MODAL
    $(".item").click(chooseQuantity)

    // CART ACTION
    $(".add-to-cart").click(addToCart)

    // CART QUANTITY
    disabledButton()

    $(".decrease").click((e) => {
        quantityChange(e)
    });

    $(".increase").click((e) => {
        quantityChange(e, true)
    });
});

const chooseQuantity = (e) => {
    e.preventDefault();
    const idProduct = $(e.target).closest('div').data("id")
    const title = $(e.target).closest('div').find(".name")[0]
    const modelTitle = $(".modal-title")[0]
    $(modelTitle).html($(title).text())
    $("#id-product").val(idProduct)
    $("#product-modal").modal('show')
}

const addToCart = () => {
    const params = {
        id: $("#id-product").val(),
        quantity: $("#quantity").val(),
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
    }

    const result = xhrRequest("../cart/add", params, "post")
    if (result) $("#product-modal").modal('hide')
}

const disabledButton = () => {
    let quantity = $('.quantity')

    quantity.each((index, element) => {
        let decrease = $(element).parent("td").find('.decrease')
        let increase = $(element).parent("td").find('.increase')

        if ($(element).text() <= 1) {
            $(decrease).attr("disabled", true)
        } else {
            $(decrease).removeAttr("disabled")
        }
        if ($(element).text() >= 10) {
            $(increase).attr("disabled", true)
        } else {
            $(increase).removeAttr("disabled")
        }
    })
}

const quantityChange = (e, isIncrease = false) => {
    e.preventDefault();
    const quantity = $(e.target).closest("td").find(".quantity")
    const price = $(e.target).closest("tr").find(".td-price")
    const totalPrice = $(e.target).closest("tr").find(".total-price")
    const item = $(e.target).parents("tr")
    const idProduct = $(item).data("id")

    let quantityValue = parseInt($(quantity).text())
    if (isIncrease) {
        quantityValue += 1;
        $(quantity).html(quantityValue)
    } else {
        quantityValue -= 1;
        $(quantity).html(quantityValue)
    }

    const params = {
        id: idProduct,
        quantity: quantityValue,
        update_quantity: true,
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
    }

    const result = xhrRequest("add", params, "post")
    if (result) {
        const totalPriceProduct = parseInt($(price).text()) * quantityValue
        $(totalPrice).html(`${totalPriceProduct}.000₫`)
        disabledButton()
    }
}


function xhrRequest(url, params = {}, method = "get", type = "json") {
    let result = false;
    const ajaxData = {
        url: url,
        data: params,
        method: method,
        dataType: type,
        async: false
    }

    $.ajax(ajaxData).done(function (res) {
        result = res;
    }).fail(function () {
        result = false;
    });
    return result;
}