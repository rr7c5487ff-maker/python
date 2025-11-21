import pytest
from television import Television

def test_init():
    tv = Television()
    result = str(tv)
    assert "Power = off" in result
    assert "Channel = 0" in result
    assert "Volume = 0" in result

def test_power():
    tv = Television()
    tv.power()
    assert "Power = on" in str(tv)
    tv.power()
    assert "Power = off" in str(tv)

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._muted is True
    tv.mute()
    assert tv._muted is False

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)
    tv.channel_down()
    assert "Channel = 2" in str(tv)

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)
    tv.mute()
    tv.volume_up()
    assert "Volume = 2" in str(tv)
    tv.volume_up()
    assert "Volume = 2" in str(tv)

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert "Volume = 1" in str(tv)
    tv.mute()
    tv.volume_down()
    assert "Volume = 0" in str(tv)
    tv.volume_down()
    assert "Volume = 0" in str(tv)

def __str__(self):
    status = "on" if self._status else "off"
    muted = " (muted)" if self._muted else ""
    return f"Power = {status}, Channel = {self._channel}, Volume = {self._volume}{muted}"
