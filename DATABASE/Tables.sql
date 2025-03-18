Use bling_db;
CREATE TABLE chat_rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(100) NOT NULL,
    created_by INT,  -- Référence à l'utilisateur qui a créé la salle
    is_private BOOLEAN DEFAULT FALSE,  -- TRUE pour les salles privées, FALSE pour les publiques
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(user_id)
);

CREATE TABLE messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    room_id INT,  -- Référence à la salle de chat
    user_id INT,  -- Référence à l'utilisateur qui a envoyé le message
    message_content TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (room_id) REFERENCES chat_rooms(room_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE private_groups (
    group_id INT AUTO_INCREMENT PRIMARY KEY,
    group_name VARCHAR(100) NOT NULL,
    created_by INT,  -- Référence à l'utilisateur qui a créé le groupe
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(user_id)
);

CREATE TABLE group_members (
    group_id INT,
    user_id INT,
    PRIMARY KEY (group_id, user_id),  -- Clé composite pour éviter les doublons
    FOREIGN KEY (group_id) REFERENCES private_groups(group_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE todos (
    todo_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- Référence à l'utilisateur qui a créé la tâche
    task TEXT NOT NULL,
    due_date DATETIME,  -- Date d'échéance de la tâche
    priority ENUM('low', 'medium', 'high') DEFAULT 'medium',  -- Priorité de la tâche
    completed BOOLEAN DEFAULT FALSE,  -- TRUE si la tâche est terminée
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE pomodoro_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- Référence à l'utilisateur
    start_time DATETIME NOT NULL,  -- Heure de début de la session
    end_time DATETIME,  -- Heure de fin de la session
    duration INT,  -- Durée de la session en minutes
    is_break BOOLEAN DEFAULT FALSE,  -- TRUE si c'est une pause, FALSE si c'est une session de travail
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE calendar_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- Référence à l'utilisateur
    event_name VARCHAR(100) NOT NULL,
    event_description TEXT,
    event_date DATETIME NOT NULL,  -- Date et heure de l'événement
    event_type ENUM('exam', 'assignment', 'meeting', 'other') DEFAULT 'other',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE calculator_history (
    calculation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- Référence à l'utilisateur
    calculation TEXT NOT NULL,  -- Calcul effectué (ex: "2 + 2")
    result TEXT NOT NULL,  -- Résultat du calcul (ex: "4")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE blingbot_conversations (
    conversation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,  -- Référence à l'utilisateur
    user_message TEXT NOT NULL,  -- Message de l'utilisateur
    bot_response TEXT NOT NULL,  -- Réponse du chatbot
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

