CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    summary,
    description,
    
)