import os

DB_NAME = os.getenv('DB_NAME', os.path.join('../data', 'grupo3.db'))

esquema = {
    "Provincia": {
        'ID': 'INTEGER PRIMARY KEY',
        'Nombre_provincia': 'TEXT UNIQUE NOT NULL'
    },
    "Regimen_Tributario": {
        'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'Nombre_regimen': 'TEXT UNIQUE NOT NULL'
    },
    "Categoria": {
        'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'Nombre_categoria': 'TEXT UNIQUE NOT NULL'
    },
    "Sector": {
        'ID': 'INTEGER PRIMARY KEY AUTOINCREMENT',
        'Nombre_sector': 'TEXT UNIQUE NOT NULL'
    },
    "Certificados_MiPyME": {
        'ID': 'INTEGER PRIMARY KEY',
        'Regimen_Tributario_ID': 'INTEGER',
        'Emision_certificado': 'DATE NOT NULL',
        'Vencimiento_certificado': 'DATE NOT NULL',
        'Categoria_ID': 'INTEGER',
        'Sector_ID': 'INTEGER',
        'Provincia_ID': 'INTEGER',
        'CLAE6': 'INTEGER NOT NULL',
        'Vigente': 'INTEGER NOT NULL',
        'FOREIGN_KEYS': {
                'Regimen_Tributario_ID': 'REFERENCES Regimen_Tributario(ID)',
                'Categoria_ID': 'REFERENCES Categoria(ID)',
                'Sector_ID': 'REFERENCES Sector(ID)',
                'Provincia_ID': 'REFERENCES Provincia(ID)'
        }
    }
}
