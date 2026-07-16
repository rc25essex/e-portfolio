from device_bridge import TV, Radio, BasicRemote, AdvancedRemote


def test_tv_power(capsys):
    tv = TV()
    remote = BasicRemote(tv)

    remote.power()

    captured = capsys.readouterr()
    assert captured.out.strip() == "TV on"


def test_radio_power(capsys):
    radio = Radio()
    remote = AdvancedRemote(radio)

    remote.power()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Radio on"


def test_advanced_remote_mute(capsys):
    radio = Radio()
    remote = AdvancedRemote(radio)

    remote.mute()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Device muted"


def test_advanced_remote_power_and_mute(capsys):
    radio = Radio()
    remote = AdvancedRemote(radio)

    remote.power()
    remote.mute()

    captured = capsys.readouterr()

    assert captured.out.splitlines() == [
        "Radio on",
        "Device muted"
    ]
