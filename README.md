# django-scian

El Sistema de Clasificación Industrial de América del Norte (SCIAN) es un sistema de clasificación de actividades económicas que permite la comparabilidad estadística entre los tres países de América del Norte: Canadá, México y Estados Unidos. El SCIAN es el resultado de la cooperación entre el Instituto Nacional de Estadística y Geografía (INEGI) de México, Statistics Canada y la Oficina de Administración y Presupuesto de los Estados Unidos de América.

## Instalación

```
pip install git+https://github.com/SIGAMty/django-scian@main
```

## Descripción

El SCIAN 2023 es la versión más reciente del sistema de clasificación, y es la base para la clasificación de las actividades económicas en las estadísticas oficiales de los tres países.

## Estructura

El SCIAN (2023) se compone de Sector, Subsector, Rama, Subrama, Clase. Cada uno de estos niveles se compone de un código y una descripción. El código es un número de 2 dígitos para el Sector, 3 dígitos para el Subsector, 4 dígitos para la Rama, 5 dígitos para la Subrama y 6 dígitos para la Clase.

```

Sector
|
|--- Subsector
|    |
|    |--- Rama
|    |    |
|    |    |--- Subrama
|    |    |    |
|    |    |    |--- Clase

```

## Fuentes

- [SCIAN](https://www.inegi.org.mx/scian/)

## API REST

https://api.monterrey.gob.mx/rest/v1/scian/

### Niveles

El SCIAN por lo tanto es un sistema jerárquico que puede ser representado por un árbol. El arbol por lo tanto puede ser consultado por nivel o por código. Por ejemplo, para obtener el Subsector de un Sector se puede hacer una consulta de la siguiente manera:

```
GET 

https://api.monterrey.gob.mx/rest/v1/scian/?nivel=subsector

```

### Consulta por código

Para obtener el Sector con código 11 se puede hacer una consulta de la siguiente manera:

```

GET

https://api.monterrey.gob.mx/rest/v1/scian/11

```

### Búsqueda por texto

La API también permite hacer búsquedas por texto. Por ejemplo, para buscar todas las clases que contengan la palabra "cine" se puede hacer una consulta de la siguiente manera:

```

GET

https://api.monterrey.gob.mx/rest/v1/scian/?search=cine

```

# Recorrer el árbol

El árbol puede ser recorrido consultando los siguientes campos:

* tn_ancestors_pks: Códigos de los ancestros
* tn_ancestors_count: Cantidad de ancestros
* tn_children_pks: Códigos de los hijos
* tn_children_count: Cantidad de hijos
* tn_depth: Profundidad
* tn_descendants_pks: Códigos de los descendientes
* tn_descendants_count: Cantidad de descendientes
* "tn_level": Nivel
* "tn_priority": Prioridad
* "tn_order": Orden
* "tn_siblings_pks": Códigos de los hermanos
* "tn_siblings_count": Cantidad de hermanos  
* "nivel": Nivel (Texto)

```

{
    "id": 46,
    "tn_ancestors_pks": "",
    "tn_ancestors_count": 0,
    "tn_children_pks": "461,462,463,464,465,466,467,468,469",
    "tn_children_count": 9,
    "tn_depth": 4,
    "tn_descendants_pks": "461,4611,46111,461110,46112,461121,461122,461123,46113,461130,46114,461140,46115,461150,46116,461160,46117,461170,46119,461190,4612,46121,461211,461212,461213,46122,461220,462,4621,46211,462111,462112,4622,46221,462210,463,4631,46311,463111,463112,463113,4632,46321,463211,463212,463213,463214,463215,463216,463217,463218,4633,46331,463310,464,4641,46411,464111,464112,464113,46412,464121,464122,465,4651,46511,465111,465112,4652,46521,465211,465212,465213,465214,465215,465216,4653,46531,465311,465312,465313,4659,46591,465911,465912,465913,465914,465915,465919,466,4661,46611,466111,466112,466113,466114,4662,46621,466211,466212,4663,46631,466311,466312,466313,466314,466319,4664,46641,466410,467,4671,46711,467111,467112,467113,467114,467115,467116,467117,468,4681,46811,468111,468112,4682,46821,468211,468212,468213,4683,46831,468311,468319,4684,46841,468411,468412,468413,468414,468419,46842,468420,469,4691,46911,469110",
    "tn_descendants_count": 147,
    "tn_index": 8,
    "tn_level": 1,
    "tn_priority": 0,
    "tn_order": 1030,
    "tn_siblings_pks": "11,21,22,23,31,32,33,43,48,49,51,52,53,54,55,56,61,62,71,72,81,93",
    "tn_siblings_count": 22,
    "nivel": "sector",
    "titulo": "Comercio al por menor",
    "descripcion": "Este sector comprende unidades económicas dedicadas principalmente a la compraventa (sin transformación) de bienes para el uso personal o para el hogar que son vendidos a personas y hogares, ya sea a través de métodos tradicionales o a través de internet (mediante páginas propias o mediante plataformas de internet provistas por terceros), u otros medios electrónicos.\n\nTambién se clasifican en este sector las unidades económicas dedicadas principalmente a actuar como intermediarias de negocios a consumidores, y entre consumidores, en la compra o venta de productos, es decir, aquellas que promueven la compra o la venta de bienes propiedad de terceros a cambio de una comisión; a la venta por televisión, y al comercio al por menor mediante la utilización de alguno de los siguientes métodos:\n\n• Comercio de productos a través de máquinas expendedoras; \n• Comercio puerta por puerta; \n• Comercio por catálogo; \n• Comercio multinivel; \n• Comercio con demostración de productos en hogares; \n• Telemercadeo con ventas vía telefónica.\n\nLas unidades económicas dedicadas al comercio se clasifican en Comercio al por menor cuando venden a personas y hogares bienes para el uso personal o para el hogar. Generalmente cuentan con acceso al público en general (ubicados y diseñados para atraer clientes) y exhibición de mercancías para facilitar a los clientes la selección de las mismas (mercancías disponibles a través de dependientes, mercancías presentadas en aparadores, salas de exhibición, unidades económicas con pasillos que permiten al cliente transitar para elegir su mercancía), y hacen publicidad masiva por medio de volantes, en medios de comunicación, etcétera.\n\nAunque, en general, el comercio al por menor realiza ventas principalmente a personas y hogares, en algunas ocasiones los bienes también se comercializan a negocios, como el comercio de automóviles o de gasolina en gasolinerías, que siempre son considerados como comercio al por menor.\n\nLas unidades económicas dedicadas al comercio al por menor pueden proporcionar servicios adicionales a la venta de los bienes, como empacado, envasado y entrega a domicilio.",
    "incluye": "Incluye también: u. e. d. p. al comercio al por menor especializado, a través de métodos tradicionales o por internet, de una gran variedad de productos, como muebles, línea blanca, artículos deportivos, combinado con la preparación y servicio de alimentos y bebidas para el consumo inmediato; de cocinas integrales prefabricadas nuevas; de alfombras, losetas vinílicas, linóleos, pisos de madera, tapices y similares combinado con su instalación; de vidrios y espejos combinado con el armado de canceles, marcos y corte de vidrio a petición del cliente; de automóviles y sus partes combinado con los servicios de reparación e instalación de accesorios, y al tostado y molienda de café para venta directa al público.",
    "excluye": "Excluye: u. e. d. p. al cultivo de frutas, verduras, semillas y granos alimenticios y su comercialización en la misma unidad económica; a la explotación de animales, como peces y aves de ornato, perros, gatos y su comercialización en la misma unidad económica; a la explotación de bovinos, ovinos y caprinos y la comercialización de leche bronca en la misma unidad económica; al cultivo de plantas y flores y su comercialización en la misma unidad económica (11, Agricultura, cría y explotación de animales, aprovechamiento forestal, pesca y caza); al suministro de gas natural por ductos al consumidor final (22, Generación, transmisión, distribución y comercialización de energía eléctrica, suministro de agua y de gas natural por ductos al consumidor final); a la instalación de sistemas centrales de aire acondicionado y de calefacción; a la colocación de pisos flexibles como alfombras, linóleos, vinilos y similares, y pisos de madera, y a la instalación de cancelería de aluminio (23, Construcción); a la molienda de semillas y granos alimenticios, chiles secos y especias; a la elaboración de helados y paletas; a la selección, corte, deshuesado, empacado y congelación de carne de ganado y aves; a la preparación, conservación y envasado de pescados y mariscos; a la molienda de nixtamal; a la elaboración y venta directa al público en general de una gran variedad de productos frescos de panadería; a la elaboración de café tostado en grano y molido; de alimentos frescos para consumo inmediato destinados a unidades que los comercializan; a la reproducción masiva de discos compactos (CD), de video digital (DVD) y videocasetes grabados (31-33, Industrias manufactureras); al comercio al por mayor de huevo; pan y pasteles; botanas y frituras; frutas deshidratadas o secas; miel; gelatinas, flanes y budines; de fibras, hilos y telas para la confección, cierres, pasamanería; de pedacería de metales preciosos; de electrodomésticos menores y aparatos de línea blanca; de semillas mejoradas para siembra; de ganado y aves en pie, de medicamentos y alimentos para animales, excepto para mascotas; de equipo y material eléctrico; de cemento, tabique, grava, cal, yeso, láminas de cartón, asbesto o acrílico, aislantes térmicos; de pisos y recubrimientos cerámicos, y muebles y accesorios para baño; de materiales metálicos para la construcción y la manufactura; de colorantes y tintas para impresión; de herrajes y chapas; de combustibles, como gas LP, gasolina, combustóleo, diésel, gasavión, biocombustibles, entre otros, y de aceites y grasas lubricantes, aditivos, anticongelantes y similares para vehículos de motor; de cámaras profesionales y semiprofesionales de captación de imágenes, instrumentos y accesorios fotográficos y cinematográficos, equipo de grabación, artículos para dibujo técnico y artístico, equipo tipográfico y artículos para serigrafía; de aparatos de telefonía y fax; de camiones y carrocerías nuevas o usadas; de casetas, campers y otras partes, refacciones y accesorios nuevos para automóviles, camionetas y camiones; a actuar como intermediarias entre negocios en la compra o venta de productos agropecuarios, para la industria, el comercio y los servicios, y productos de uso doméstico y personal; a fungir como subastadores de productos agropecuarios, para la industria, el comercio y los servicios, y productos de uso doméstico y personal, ofertados entre negocios (43, Comercio al por mayor); a la exhibición de películas que en la misma ubicación física venden dulces y otros alimentos bajo la misma razón social; a la venta de tarjetas telefónicas; a la producción de material discográfico, como discos compactos (CD) y de video digital (DVD) o casetes musicales, y a la producción de este material integrada con su reproducción o con su distribución, y estudios de grabación (51, Información en medios masivos); u. e. d. p. a la planeación, diseño y decoración de espacios interiores de edificaciones residenciales y no residenciales (54, Servicios profesionales, científicos y técnicos); a la promoción por teléfono de productos; a los servicios de instalación y mantenimiento de áreas verdes; a la limpieza de pescado a petición de terceros; a la organización de subastas (56, Servicios de apoyo a los negocios y manejo de residuos, y servicios de remediación); a la preparación de chicharrón, carnitas, barbacoa, pollos rostizados, pescados y mariscos para consumo inmediato en las instalaciones de la unidad económica o para llevar; a preparar y servir paletas de hielo, helados y nieves para su consumo inmediato; a preparar y servir bebidas alcohólicas y no alcohólicas; a la preparación de café para llevar o de autoservicio; a la preparación de bebidas no alcohólicas (café, té, chocolate) para su consumo inmediato en combinación con la elaboración de pan; a preparar y servir café para consumo inmediato en combinación con el tostado y la molienda del mismo; a la preparación y entrega de alimentos para consumo inmediato por contrato para industrias, oficinas, hospitales, medios de transporte e instituciones; para ocasiones especiales, y en unidades móviles (72, Servicios de alojamiento temporal y de preparación de alimentos y bebidas); a proporcionar servicios de revelado e impresión de fotografías en combinación con el comercio de artículos fotográficos; a ofrecer servicios funerarios en combinación con el comercio de ataúdes; a la reparación y mantenimiento de artículos para el hogar y personales; a la reparación menor de llantas y cámaras de automóviles y camiones; a la instalación de autoestéreos; a los servicios de polarizado de cristales, alineación y balanceo, y servicios de cambio de aceite de automóviles y camiones (81, Otros servicios excepto actividades gubernamentales); montepíos y casas de empeño (52, Servicios financieros y de seguros); consultorios de optometría (62, Servicios de salud y de asistencia social), y galerías de arte que solo exhiben las obras (71, Servicios de esparcimiento culturales y deportivos, y otros servicios recreativos).",
    "indice": "",
    "tn_parent": null
},

```

