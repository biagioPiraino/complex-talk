CREATE DATABASE complex_talk;

\c complex_talk;

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    category TEXT NULL,
    title TEXT NULL,
    content TEXT NULL
);

CREATE OR REPLACE FUNCTION create_article(
    category TEXT,
    title TEXT,
    content TEXT
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO articles (category, title, content)
    VALUES (
      category,
      title,
      content
    );
END;
$$ LANGUAGE plpgsql;