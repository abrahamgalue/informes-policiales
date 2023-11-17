CREATE SCHEMA IF NOT EXISTS proyecto DEFAULT CHARACTER SET utf8 ;
USE proyecto;

CREATE TABLE IF NOT EXISTS persona (
  `numero_de_identificacion` VARCHAR(10) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `fecha_de_nacimiento` DATE NOT NULL,
  `sexo` ENUM("Masculino", "Femenino") NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `direccion` VARCHAR(200) NOT NULL,
  `nacionalidad` VARCHAR(45) NOT NULL,
  `alias` VARCHAR(45) NULL,
  PRIMARY KEY (`numero_de_identificacion`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS ocurrencia_de_arresto (
  `id` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `lugar` VARCHAR(60) NOT NULL,
  `delito` VARCHAR(45) NOT NULL,
  `tipo_de_delito` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  `implicado_numero_de_identificacion` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_ocurrencia_de_arresto_implicado1`
    FOREIGN KEY (`implicado_numero_de_identificacion`)
    REFERENCES persona (`numero_de_identificacion`)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS condena (
  `fecha` DATE NOT NULL,
  `sentencia` VARCHAR(128) NOT NULL,
  `ocurrencia_de_arresto_id` INT NOT NULL,
  PRIMARY KEY (`ocurrencia_de_arresto_id`),
  CONSTRAINT `fk_condena_ocurrencia_de_arresto1`
    FOREIGN KEY (`ocurrencia_de_arresto_id`)
    REFERENCES ocurrencia_de_arresto (`id`)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS señas_de_identificacion (
  `peso` DECIMAL(5,2) NOT NULL,
  `altura` DECIMAL(5,2) NOT NULL,
  `color_de_piel` VARCHAR(45) NOT NULL,
  `cabello` VARCHAR(45) NOT NULL,
  `color_de_cabello` VARCHAR(45) NOT NULL,
  `ojos` VARCHAR(45) NOT NULL,
  `otra_caracteristica` VARCHAR(60) NULL,
  `persona_numero_de_identificacion` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`persona_numero_de_identificacion`),
  CONSTRAINT `fk_señas_de_identificacion_implicado`
    FOREIGN KEY (`persona_numero_de_identificacion`)
    REFERENCES persona (`numero_de_identificacion`)
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS complice (
  `persona_numero_de_identificacion` VARCHAR(10) NOT NULL,
  `ocurrencia_de_arresto_id` INT NOT NULL,
  PRIMARY KEY (`persona_numero_de_identificacion`, `ocurrencia_de_arresto_id`),
  CONSTRAINT `fk_persona_has_ocurrencia_de_arresto_complice`
    FOREIGN KEY (`persona_numero_de_identificacion`)
    REFERENCES persona (`numero_de_identificacion`),
  CONSTRAINT `fk_persona_has_ocurrencia_de_arresto_ocurrencia_de_arresto1`
    FOREIGN KEY (`ocurrencia_de_arresto_id`)
    REFERENCES ocurrencia_de_arresto (`id`)
)
ENGINE = InnoDB;

