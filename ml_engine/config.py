from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Store connection (required: no defaults, so a missing .env fails loudly)
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5433

    # Embedding
    embedding_model: str = "BAAI/bge-base-en-v1.5"
    embedding_dim: int = 768
    chunk_size: int = 400            # words per chunk (starting guess)

    # Routing
    descend_threshold: float = 0.5
    link_margin: float = 0.05

    # Cold start
    cold_start_size: int = 30
    cold_start_cut: float = 0.5      # clustering cut (meaning decided in Step 5)

    # No-Match promotion
    promote_size: int = 10
    promote_cohesion_threshold: float = 0.6

    # Leaf splitting
    leaf_split_size: int = 15
    split_silhouette_threshold: float = 0.25

    # Upward restructuring
    max_children: int = 8
    restructure_silhouette_threshold: float = 0.25
    restructure_retry_after: int = 4

    # Labeling
    llm_provider: str = "ollama"
    llm_model: str = ""              # chosen in Step 10
    llm_base_url: str = "http://localhost:11434"
    relabel_growth_fraction: float = 0.5

    @property
    def database_url(self) -> str:
        return (
            f"postgresql://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


settings = Settings()