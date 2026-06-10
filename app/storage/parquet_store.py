import polars as pl


class ParquetStore:

    @staticmethod
    def write_rows(
        rows,
        path,
    ):
        (pl.DataFrame(rows).write_parquet(path))
