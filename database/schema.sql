
CREATE TABLE IF NOT EXISTS  users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_full_name TEXT NOT NULL,
    user_email TEXT NOT NULL,
    user_city TEXT NOT NULL
);
