USE kec6oj1sn5kdspby;

CREATE TABLE veterinarios (
    tarjeta_profesional INT PRIMARY KEY,
    id_veterinario INT,
    nombre_veterinario VARCHAR(45),
    direccion_veterinario VARCHAR(45),
    telefono_veterinario VARCHAR(45),
    correo_veterinario VARCHAR(45)
    );

CREATE TABLE dueños (
    id_dueño INT PRIMARY KEY,
    nombre_dueño VARCHAR(45),
    direccion_dueño VARCHAR(45),
    telefono_dueño VARCHAR(45),
    correo_dueño VARCHAR(45)
    );

CREATE TABLE mascotas (
    id_mascota INT PRIMARY KEY,
    nombre VARCHAR(50),
    especie VARCHAR(50),
    raza VARCHAR(50)
    color VARCHAR(50),
    cantidad_visitas INT,
    id_dueño INT,
    tarjeta_profesional INT,

    FOREIGN KEY (id_dueño)
    REFERENCES dueños(id_dueño),

    FOREIGN KEY (tarjeta_profesional)
    REFERENCES veterinarios(tarjeta_profesional)
);

CREATE TABLE visita (
    id_visita INT PRIMARY KEY AUTO_INCREMENT,
    id_mascota INT,
    temperatura DECIMAL(4,2),
    peso DECIMAL(5,2),
    frecuencia_respiratoria INT,
    frecuencia_cardiaca INT,
    estado_animo VARCHAR(45),
    fecha DATE,
    observaciones VARCHAR(50),

    FOREIGN KEY (id_mascota)
    REFERENCES mascotas(id_mascota)
);
