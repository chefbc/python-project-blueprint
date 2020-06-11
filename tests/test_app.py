from .context import mytest


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    mytest.Blueprint.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out
