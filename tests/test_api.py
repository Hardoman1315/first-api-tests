from tests_class import TestCase


class TestID:

    def test_first(self):
        test_case = TestCase()
        id_new_animal = test_case.create_animal('Orlock')
        id_find_animal = test_case.find_animal(id_new_animal)['id']
        test_case.remove_animal(id_find_animal)
        deleted_animal = test_case.find_animal(id_find_animal)
        assert deleted_animal is not id_find_animal, (
            "[FAILED]: Ids doesnt match {} and {}".format(id_new_animal, id_find_animal)
            )
