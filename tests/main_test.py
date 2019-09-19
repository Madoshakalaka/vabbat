from vabbat.main import cmd_entry


def test_cmd(capsys):
    # cmd_entry([..., 'arg1', 'arg2'])
    cmd_entry([...])
    captured = capsys.readouterr()
    assert captured.out.strip() == 'reserved command line entry for python package vabbat'
    assert captured.err == ''
