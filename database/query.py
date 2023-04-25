
USERS_QUERY = """
        CREATE TABLE IF NOT EXISTS users (
            id VARCHAR(50) PRIMARY KEY,
            created_at TIMESTAMP NOT NULL DEFAULT NOW(),
            nom VARCHAR(50) NOT NULL,
            prenom VARCHAR(50) NOT NULL,
            age INT
        );
    """
