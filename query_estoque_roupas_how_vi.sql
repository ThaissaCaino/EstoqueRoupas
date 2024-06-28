-- -----------------------------------------------------
-- Schema estoque_roupas_how_vi
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `estoque_roupas_how_vi` DEFAULT CHARACTER SET utf8;
USE `estoque_roupas_how_vi`;

-- -----------------------------------------------------
-- Table `estoque_roupas_how_vi`.`roupas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_roupas_how_vi`.`roupas` (
  `id_roupas` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nome` VARCHAR(45) NOT NULL,
  `tamanho` VARCHAR(5) NOT NULL,
  `preco` Decimal(10,2) NOT NULL);

-- -----------------------------------------------------
-- Table `estoque_roupas_how_vi`.`fornecedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `estoque_roupas_how_vi`.`fornecedor` (
  `id_fornecedor` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nome` VARCHAR(45) NOT NULL,
  `endereco` VARCHAR(80) NOT NULL,
  `telefone` VARCHAR(15) NOT NULL);


-- -----------------------------------------------------
-- Table `estoque_roupas_how_vi`.`roupas_fornecedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS estoque_roupas_how_vi.roupas_fornecedor (
    id_roupas INT NOT NULL,
    id_fornecedor INT NOT NULL,
    PRIMARY KEY (id_roupas, id_fornecedor),
    FOREIGN KEY (id_roupas) REFERENCES estoque_roupas_how_vi.roupas (id_roupas),
    FOREIGN KEY (id_fornecedor) REFERENCES estoque_roupas_how_vi.fornecedor (id_fornecedor)
);