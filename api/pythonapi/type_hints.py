from typing import TypeAlias

stats_table_type: TypeAlias = list[dict[str, float | int | str | list[str]]]
colony_stats_type: TypeAlias = dict[str, float | str | stats_table_type]