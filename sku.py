#Business Website
from pyscript import document

def generate_sku(e):
    category = document.getElementById("category").value
    product_name = document.getElementById("product_name").value
    quantity = document.getElementById("quantity").value

    category_code = category[:3].upper()
    product_code = product_name[:3].upper()
    quantity_code = quantity.zfill(3)

    sku = f"MERCADO-RICEMEALS-{category_code}-{product_code}-{quantity_code}"

    document.getElementById("sku_output").innerHTML = f"""
        <p style="text-align: center;">
            <b>Generated SKU:</b> {sku}
        </p>
    """
