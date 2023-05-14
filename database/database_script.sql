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

CREATE OR REPLACE FUNCTION get_latest_article()
RETURNS TABLE (
  id INT,
  created_at TIMESTAMP,
  category TEXT,
  title TEXT,
  content TEXT
)
AS $$
BEGIN
  RETURN QUERY SELECT * FROM articles ORDER BY created_at DESC LIMIT 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_latest_article_by_category(
    category_filter TEXT
)
RETURNS TABLE (
  id INT,
  created_at TIMESTAMP,
  category TEXT,
  title TEXT,
  content TEXT
)
AS $$
BEGIN
  RETURN QUERY 
    SELECT * FROM articles 
    WHERE articles.category=category_filter 
    ORDER BY created_at DESC LIMIT 1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_articles_by_category(
    category_filter TEXT
)
RETURNS TABLE (
  id INT,
  created_at TIMESTAMP,
  category TEXT,
  title TEXT,
  content TEXT
)
AS $$
BEGIN
  RETURN QUERY 
    SELECT * FROM articles 
    WHERE articles.category=category_filter 
    ORDER BY created_at DESC;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_article_by_id(
    id_filter INT
)
RETURNS TABLE (
  id INT,
  created_at TIMESTAMP,
  category TEXT,
  title TEXT,
  content TEXT
)
AS $$
BEGIN
  RETURN QUERY 
    SELECT * FROM articles 
    WHERE articles.id=id_filter;
END;
$$ LANGUAGE plpgsql;