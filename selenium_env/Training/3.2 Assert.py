#assert (catalog_text := self.catalog_link.text) == "Каталог", \
    #f"Wrong language, got {catalog_text} instead of 'Каталог'"

def test_input_text(expected_result, actual_result):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

test_input_text(11,11);