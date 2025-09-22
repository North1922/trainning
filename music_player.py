# 9) Музыкальный проигрыватель
#
# Классы: Track, Playlist, Player.
# Методы: play(), pause(), next(), prev().
# Усложнение (паттерны): режимы воспроизведения как PlaybackMode (Normal/Repeat/Shuffle) — через Strategy или State.
# Проверки: переходы между пустыми/крайними состояниями.

# 9) Музыкальный плеер
#
# Сущности: Track, Playlist, Player, PlaybackMode (Strategy/State).
#
# Атрибуты:
#
# Track: title, artist, duration_sec.
#
# Playlist: список треков, текущий индекс.
#
# Player: состояние (playing/paused/stopped), активная плейлист/текущий трек.
#
# PlaybackMode: Normal, RepeatOne, RepeatAll, Shuffle.
#
# Методы (обязательные):
#
# Player.play() / pause() / stop().
#
# Player.next() / prev() — с учётом режима.
#
# Playlist.add(track) / remove(track) / clear().
#
# PlaybackMode.next_index(current, playlist_len) — правило перехода.
#
# Проверки/ошибки: next()/prev() на пустой плейлист; выход за границы; Shuffle не должен сразу повторять текущий (по возможности).
#
# Инварианты: индекс валиден, когда есть треки; состояние согласовано с наличием трека.
#
# Усложнения: история прослушивания; позиция внутри трека; события (hooks) для UI.