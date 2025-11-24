class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Create new TV with standard/defailt settings"""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power"""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute if the TV is on"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the channel number or go back around to front"""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decrease the channel number or go to back"""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Raise the volume, unmute if muted"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Lower the volume, unmute if muted"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def get_status(self) -> bool:
        """Get power status."""
        return self.__status

    def get_muted(self) -> bool:
        """Get muted status."""
        return self.__muted

    def get_volume(self) -> int:
        """Get current volume."""
        return self.__volume

    def get_channel(self) -> int:
        """Get current channel."""
        return self.__channel

    def __str__(self) -> str:
        """Get a string that shows the TV's current settings."""
        status = "on" if self.__status else "off"
        return f"Power = {status}, Channel = {self.__channel}, Volume = {self.__volume}"
