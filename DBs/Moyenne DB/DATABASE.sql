CREATE DATABASE etudiants_db;

USE etudiants_db;

CREATE TABLE etudiants (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    prenom VARCHAR(100)
);

CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    etudiant_id INT,
    matiere VARCHAR(100),
    note DECIMAL(5,2),
    FOREIGN KEY (etudiant_id) REFERENCES etudiants(id)
);
