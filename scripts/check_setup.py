import psycopg

from ml_engine.config import settings


def main() -> None:
    with psycopg.connect(settings.database_url) as conn:
        conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
        row = conn.execute(
            "SELECT extversion FROM pg_extension WHERE extname = 'vector'"
        ).fetchone()
    print(f"Connected. pgvector version: {row[0]}")


if __name__ == "__main__":
    main()