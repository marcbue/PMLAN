import src.features.build_features as bfts


def test_print_stuff(capfd):
    test_string = 'hello'
    bfts.print_stuff(test_string)
    out, err = capfd.readouterr()
    assert out == 'hello\n'
