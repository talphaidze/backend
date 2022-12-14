from recipe_api.models import Recipe
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    recipe = Recipe('Tiramisu', 'coffee', 'rating', 'favorite')
    assert recipe.name == 'Tiramisu'
    assert recipe.ingredients == 'coffee'
    assert recipe.rating == 'rating'
    assert recipe.favorite == 'favorite'
 