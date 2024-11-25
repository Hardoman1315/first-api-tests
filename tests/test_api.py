from tests_class import TestCase


class TestID:

    def test_first(self):
        test_case = TestCase()
        id_new_animal = test_case.create_animal('Orlock')
        id_find_animal = test_case.find_animal(id_new_animal)['id']
        assert id_new_animal == id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(id_new_animal, id_find_animal)
        )
        test_case.remove_animal(id_find_animal)
        received_message = test_case.find_animal(id_find_animal)
        expected_message = 1
        assert received_message['code'] == expected_message, (
            "[Failed]: The server did not return the expected code"
            )
