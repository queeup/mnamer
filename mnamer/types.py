"""Enum type definitions."""

from enum import Enum

__all__ = ["MediaType", "MessageType", "ProviderType", "SettingType"]


class MediaType(Enum):
    EPISODE = "episode"
    MOVIE = "movie"


class MessageType(Enum):
    INFO = None
    ALERT = "yellow"
    ERROR = "red"
    SUCCESS = "green"
    HEADING = "bold"


class ProviderType(Enum):
    TVDB = "tvdb"
    TVMAZE = "tvmaze"
    TMDB = "tmdb"
    OMDB = "omdb"


class SettingType(Enum):
    DIRECTIVE = "directive"
    PARAMETER = "parameter"
    POSITIONAL = "positional"
    CONFIGURATION = "configuration"


class Language(Enum):
    # based on http://stephenfollows.com/languages-most-commonly-used-in-movies
    ENGLISH = "en"
    FRENCH = "fr"
    SPANISH = "es"
    GERMAN = "de"
    HINDI = "hi"
    CHINESE = "zh"
    JAPANESE = "ja"
    ITALIAN = "it"
    RUSSIAN = "ru"
    ARABIC = "ar"
    KOREAN = "ko"
    HEBREW = "he"
    PORTUGUESE = "pt"
    SWEDISH = "sv"
    LATIN = "la"
    UKRAINIAN = "uk"
    DANISH = "da"
    PERSIAN = "fa"

    def __str__(self):
        return str(self.value)
