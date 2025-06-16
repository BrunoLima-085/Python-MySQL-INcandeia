CREATE DATABASE INcandeia;
USE INcandeia;

CREATE TABLE produto (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    quantidade_disponivel INT NOT NULL DEFAULT 0,
    preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE venda (
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_produto INT NOT NULL,
    quantidade_vendida INT NOT NULL,
    data_venda DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);

DELIMITER //
CREATE TRIGGER atualizar_estoque
AFTER INSERT ON venda
FOR EACH ROW
BEGIN
	UPDATE produto
    SET quantidade_disponivel = quantidade_disponivel - NEW.quantidade_vendida
    WHERE id = NEW.id_produto;
END;
// DELIMITER ;

