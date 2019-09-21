from vabbat.main import cmd_entry


def test_cmd(shared_datadir):
    cmd_entry([..., str(shared_datadir / "trafficVideo.mp4")])
