$(document).ready(function () {
    $("#get-year").html(new Date().getFullYear())

    // CHOOSE QUANTITY MODAL 
    $(".item").click(chooseQuantity)

    // CART ACTION
    $(".add-to-cart").click(addToCart)

    // CART QUANTITY
    disabledButton()

    $(".decrease").click((e) => {
        quantityChange(e)
    })

    $(".increase").click((e) => {
        quantityChange(e, true)
    })

    // CART DELETE
    $(".delete").click(deleteCart)

    // STAFF INFO 
    getStaffName()

    // CART 
    getCartTotal()

    // ORDER 
    $("#payment").click(createOrder)
    $("#received").change(moneyReturn)
    $(".money").keyup(formatCurrency);
});

const moneyReturn = (e) => {
    let $input = $(e.target),
        received = parseInt($input.val()),
        paid = parseInt($("#paid").val()),
        returns = $("#returns")
    returns.val(received - paid + ".000");

}

const formatCurrency = (e) => {
    let $input = $(e.target),
        number = $input.val()
    number += ''
    number = number.replace(".", "")
    x = number.split('.')
    x1 = x[0]
    x2 = x.length > 1 ? '.' + x[1] : ''
    let rgx = /(\d+)(\d{3})/
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + '.' + '$2')
    }
    $input.val(x1 + x2)
}

const chooseQuantity = (e) => {
    e.preventDefault();
    const idProduct = $(e.target).closest('div').data("id")
    const title = $(e.target).closest('div').find(".name")[0]
    const modelTitle = $(".modal-title")[0]
    $(modelTitle).html($(title).text())
    $("#id-product").val(idProduct)
    $("#product-modal").modal('show')
}

// CART 
const addToCart = () => {
    const params = {
        id: $("#id-product").val(),
        quantity: $("#quantity").val(),
        csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
    }

    const result = xhrRequest("../cart/add", params, "post")
    if (result) {
        $("#product-modal").modal('hide')
        getCartTotal()
    }
}

const getCartTotal = () => {
    const result = xhrRequest("/cart/total-item")
    $("#cart-total").html(result.total)
    result.total != 0 ? $("#payment").removeClass("disabled") : $("#payment").addClass("disabled")
}

const deleteCart = (e) => {
    e.preventDefault();
    const item = $(e.target).closest(".item")[0]
    const id = $(item).data('id')
    const url = `/cart/remove/${id}/`
    const result = xhrRequest(url)
    if (result) {
        item.remove()
    }
    getCartTotal()
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
        getCartTotal()
    }
}
// END CART

const getStaffName = () => {
    const result = xhrRequest("/name")
    if (result) $("#staff-info").html(result.user)
}

const createOrder = (e) => {
    e.preventDefault();
    console.log("Creating new order...")
    const paid = $(e.target).closest(".modal-content").find("input[name='paid']")
    const url = "/order/create/"
    let data = {}
    if (validate(paid)) {
        data = {
            paid: $(paid).val(),
            csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
        }
        const result = xhrRequest(url, data, "post")
        console.log(result)
    }
}

const validate = (selector) => {
    const parent = $(selector).parents('.form-group');
    const requiredError = `<small><span class="text-danger">Bắt buộc điền</span></small>`
    if ($(selector).val() == '') {
        parent.addClass("has-error")
        parent.append(requiredError)
        return false;
    } else {
        parent.removeClass("has-error")
        parent.children('small').last().remove();
        return true;
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