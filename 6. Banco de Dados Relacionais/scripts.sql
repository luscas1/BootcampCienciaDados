INSERT INTO reservas (id, id_usuario, id_destino, data, status) VALUES (2, 2, 2, "2026-01-12", "Confirmada"), (3, 3, 3, "2026-01-16", "Pendente");

SELECT * FROM usuarios WHERE id = 1;

SELECT * FROM `usuarios`
WHERE nome LIKE "%Lucas%" AND id = 1;

SELECT * FROM `usuarios`
WHERE nome LIKE "%Lucas%" OR id = 1;

UPDATE usuarios
SET email = "lucas.motta09@gmail.com"

WHERE email = "teste@gmail.com";

INSERT INTO destinos (id, nome, descricao) VALUES (1, "RJ","AHHWU");

DELETE FROM destinos
WHERE nome = "RJ";

CREATE TABLE usuarios_nova (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
  data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário',
  endereco VARCHAR(100) NOT NULL COMMENT 'Endereço do Cliente'
);

INSERT INTO usuarios_nova (id, nome, email, data_nascimento, endereco)
SELECT id, nome, email, data_nascimento, endereco FROM usuarios;

DROP TABLE usuarios;

ALTER TABLE usuarios_nova RENAME usuarios;

ALTER TABLE usuarios MODIFY COLUMN endereco VARCHAR(150);

ALTER TABLE usuarios MODIFY COLUMN id INT AUTO_INCREMENT, ADD PRIMARY KEY (id);

ALTER TABLE destinos 
MODIFY COLUMN id INT
AUTO_INCREMENT,
ADD PRIMARY KEY (id);

ALTER TABLE reservas 
MODIFY COLUMN id INT
AUTO_INCREMENT,
ADD PRIMARY KEY (id);

ALTER TABLE reservas
ADD CONSTRAINT fk_reserva_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id);

ALTER TABLE reservas
ADD CONSTRAINT fk_reserva_destinos
FOREIGN KEY (id_destino) REFERENCES destinos(id);

ALTER TABLE reservas DROP CONSTRAINT fk_reserva_usuarioS;

ALTER TABLE reservas
ADD CONSTRAINT fk_reserva_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE;

DELETE FROM usuarios
WHERE id = 1;

ALTER TABLE usuarios
ADD rua VARCHAR(100),
ADD numero VARCHAR(10),
ADD bairro VARCHAR(20),
ADD cidade VARCHAR(50);

UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
    numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
    bairro = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
    cidade = SUBSTRING_INDEX(endereco, ',', -1);
 
ALTER TABLE usuarios 
DROP COLUMN endereco;