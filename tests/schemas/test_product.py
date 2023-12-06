from uuid import UUID
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = ProductIn.model_validate(data)

    assert isinstance(product.id, UUID)
    assert isinstance(product.name, str)
    assert isinstance(product.quantity, int)
    assert isinstance(product.price, float)
    assert isinstance(product.status, bool)


def test_schemas_return_raise():
    data = {
        "name": "Iphone 14",
        "quantity": 10,
        "price": 8.500,
        # "status": True
    }
    with pytest.raises(ValueError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Iphone 14", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydantic.dev/2.5/v/missing",
    }
