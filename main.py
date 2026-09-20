#Business Website
from pyscript import document


def create_order(e):
    prod1 = document.getElementById("prod1")
    prod2 = document.getElementById("prod2")
    prod3 = document.getElementById("prod3")

    subtotal = (float(prod1.value) * prod1.checked +float(prod2.value) * prod2.checked +float(prod3.value) * prod3.checked)

    tax = subtotal * 0.12
    total = subtotal + tax

    document.getElementById("show").innerHTML = f"""
        <p>--------------------</p>
        <p><b>Subtotal:</b> ₱{subtotal}</p>
        <p><b>VAT (12%):</b> ₱{tax}</p>
        <p><b>Total:</b> ₱{total}</p>
    """