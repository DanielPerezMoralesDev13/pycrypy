<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/DanielPerezMoralesDev13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

<!-- PYTHONPATH=src python3 src/cli/main.py --help -->

# ***pycrypy***

> *`pycrypy` es una herramienta de línea de comandos escrita en Python para configurar fácilmente las opciones de Alacritty desde la terminal. Permite ajustar temas, fuentes, tamaño de fuente, opacidad, padding, forma del cursor, y más, con simples comandos.*

## ***Características***

- [x] **Cambio de Tema:** *Modifica el tema de Alacritty usando una ruta de fichero o un nombre de tema.*
- [x] **Configuración de Fuentes:** *Cambia la fuente y el tamaño de la fuente en Alacritty.*
- [x] **Ajuste de Opacidad:** *Modifica la opacidad de la terminal.*
- [x] **Configuración de Padding:** *Ajusta el padding de la terminal.*
- [x] **Forma del Cursor:** *Cambia la forma y el parpadeo del cursor.*

## ***Instalación***

### ***Instalación mediante PyPI***

**Puedes instalar `pycrypy` fácilmente utilizando `pip`:**

```bash
pip install pycrypy
```

### ***Instalación desde el Código Fuente***

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/DanielPerezMoralesDev13/pycrypy.git --depth=1
   ```

2. **Navegar al Directorio del Proyecto:**

   ```bash
   cd pycrypy
   ```

3. **Instalar Dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar el Paquete:**

   ```bash
   pip install .
   ```

## ***Uso***

> *Para usar `pycrypy`, simplemente ejecuta el comando `pycrypy` seguido de las opciones deseadas. Aquí tienes una descripción de las opciones disponibles:*

### ***Opciones***

```bash
pycrypy [-h] [-t [THEME ...]] [-P [THEMEPATH]] [-f [FONT ...]] [-F [FONTSIZE]] [-s [STYLE ...]]
      [-o OPACITY] [-p X Y] [-S [CURSORSHAPE]] [-B [CURSORBLINKING]] [-T [CURSORTHICKNESS]]
      [-R] [-D] [-L] [-v] [-V]
```

### ***-h, --help***

**Muestra este mensaje de ayuda y sale.**

```bash
usage: pycrypy [-h] [-t [THEME ...]] [-P [THEMEPATH]] [-f [FONT ...]] [-F [FONTSIZE]] [-s [STYLE ...]]
                               [-o OPACITY] [-p X Y] [-S [CURSORSHAPE]] [-B [CURSORBLINKING]] [-T [CURSORTHICKNESS]] [-R]
                               [-D] [-L] [-v] [-V]

pycrypy es una herramienta de línea de comandos diseñada para configurar fácilmente las opciones de Alacritty
desde la terminal utilizando Python.

options:
  -h, --help            show this help message and exit
  -t [THEME ...], --theme [THEME ...]
                        Cambia el tema utilizado por alacritty
  -P [THEMEPATH], --theme-path [THEMEPATH]
                        Ruta absoluta o relativa del tema para aplicarlo en la terminal Alacritty
  -f [FONT ...], --font [FONT ...]
                        Cambia la fuente utilizada por Alacritty
  -F [FONTSIZE], --font-size [FONTSIZE]
                        Cambia el tamaño de la fuente
  -s [STYLE ...], --style [STYLE ...]
                        Cambia el estilo de la fuente: Normal | Bold | Italic | Underline
  -o OPACITY, --opacity OPACITY
                        Cambia la opacidad de la terminal de Alacritty
  -p X Y, --padding X Y
                        Cambia el padding de la terminal de Alacritty
  -S [CURSORSHAPE], --cursor-shape [CURSORSHAPE]
                        shape es una opción que define la forma del cursor y puede tomar uno de estos valores:
                        Block | Underline | Beam
  -B [CURSORBLINKING], --cursor-blinking [CURSORBLINKING]
                        Esta opcion define si el cursor parpadea y puede tener uno de estos valores: Never | Off
                        | On | Always
  -T [CURSORTHICKNESS], --cursor-thickness [CURSORTHICKNESS]
                        Esta opcion define el grosor del cursor
  -R, --theme-recommendations
                        Lista los temas recomendados para alacritty
  -D, --theme-dark      Lista los temas oscuros para alacritty
  -L, --theme-light     Lista los temas claros para alacritty
  -v, --verbose         Activar modo detallado
  -V, --version         Muestra la versión del programa y los datos del Autor

¡Disfruta configurando tu Alacritty con pycrypy!
```

### ***-t [THEME ...], --theme [THEME ...]***

- *Cambia el tema utilizado por Alacritty. Puedes especificar uno o más temas.*

**Ejemplo:**

```bash
pycrypy -t tokyo night
```

*Este comando cambia el tema de Alacritty a tokyo night.*

### ***-P [THEMEPATH], --theme-path [THEMEPATH]***

- *Ruta absoluta o relativa del tema para aplicarlo en la terminal Alacritty.*

**Ejemplo:**

```bash
pycrypy -P "/home/usuario/.config/alacritty/themes/mytheme.toml"
```

*Este comando aplica el tema desde la ruta especificada.*

### ***-f [FONT ...], --font [FONT ...]***

- *Cambia la fuente utilizada por Alacritty. Puedes especificar una o más fuentes.*
**Ejemplo:**

```bash
pycrypy -f Cascadia Code NF
```

*Este comando cambia la fuente de Alacritty a Cascadia Code NF.*

### ***-F [FONTSIZE], --font-size [FONTSIZE]***

- *Cambia el tamaño de la fuente.*

**Ejemplo:**

```bash
pycrypy -F 14
```

*Este comando establece el tamaño de la fuente en 14.*

### ***-s [STYLE ...], --style [STYLE ...]***

- *Cambia el estilo de la fuente: Normal | Bold | Italic | Underline. Puedes especificar uno o más estilos.*

**Ejemplo:**

```bash
pycrypy -s Bold Italic
```

*Este comando aplica los estilos Bold Italic a la fuente en Alacritty.*

### ***-o OPACITY, --opacity OPACITY***

- *Cambia la opacidad de la terminal de Alacritty.*

**Ejemplo:**

```bash
pycrypy -o 0.8
```

*Este comando establece la opacidad de la terminal en 80%.*

### ***-p X Y, --padding X Y***

- *Cambia el padding de la terminal de Alacritty.*

**Ejemplo:**

```bash
pycrypy -p 10 15
```

- *Este comando establece el padding en 10 píxeles verticales y 15 píxeles horizontales.*

### ***-S [CURSORSHAPE], --cursor-shape [CURSORSHAPE]***

- *Define la forma del cursor. Puede tomar uno de estos valores: Block | Underline | Beam.*

**Ejemplo:**

```bash
pycrypy -S Beam
```

*Este comando establece la forma del cursor a Beam.*

### ***-B [CURSORBLINKING], --cursor-blinking [CURSORBLINKING]***

- *Define si el cursor parpadea. Puede tener uno de estos valores: Never | Off | On | Always.*
**Ejemplo:**

```bash
pycrypy -B Always
```

*Este comando establece el parpadeo del cursor a Always.*

### ***-T [CURSORTHICKNESS], --cursor-thickness [CURSORTHICKNESS]***

- *Define el grosor del cursor.*
**Ejemplo:**

```bash
pycrypy -T 2
```

*Este comando establece el grosor del cursor en 2 píxeles.*

### ***-R, --theme-recommendations***

- *Lista los temas recomendados para Alacritty.*
**Ejemplo:**

```bash
pycrypy -R
```

*Este comando muestra una lista de temas recomendados para Alacritty.*

### ***-D, --theme-dark***

- *Lista los temas oscuros para Alacritty.*
**Ejemplo:**

```bash
pycrypy -D
```

*Este comando muestra una lista de temas oscuros para Alacritty.*

### ***-L, --theme-light***

- *Lista los temas claros para Alacritty.*
**Ejemplo:**

```bash
pycrypy -L
```

*Este comando muestra una lista de temas claros para Alacritty.*

### ***-v, --verbose***

- *Activa el modo detallado.*
**Ejemplo:**

```bash
pycrypy -v
```

*Este comando ejecuta `pycrypy` en modo detallado, mostrando información adicional.*

### ***-V, --version***

- *Muestra la versión del programa y los datos del autor.*
**Ejemplo:**

```bash
pycrypy -V
```

*Este comando muestra la versión actual del programa y la información del autor.*

### ***Crear un Ejecutable con PyInstaller***

> *Para convertir el script `cli/main.py` en un ejecutable independiente, utiliza PyInstaller con las siguientes opciones:*

**Aquí está el comando `pyinstaller` equivalente a la configuración que has proporcionado:**

```bash
# Mover al directorio source (fuente)
cd ./src
```

```bash
pyinstaller --onefile \
            --noconfirm \
            --clean \
            --noconsole \
            --name pycrypy \
            --add-data "TemasClaros:TemasClaros" \
            --add-data "TemasOscuros:TemasOscuros" \
            --add-data "TemasRecomendados:TemasRecomendados" \
            --add-data "cli:cli" \
            --add-data "config:config" \
            --add-data "lib:lib" \
            src/cli/main.py
```

### ***Desglose del Comando***

- **`--onefile`:** *Crea un solo fichero ejecutable.*
- **`--noconfirm`:** *No pide confirmación antes de sobrescribir ficheros.*
- **`--clean`:** *Limpia ficheros temporales de compilación.*
- **`--noconsole`:** *No abre una ventana de consola al ejecutar el ejecutable (para aplicaciones GUI).*
- **`--name pycrypy`:** *Define el nombre del fichero ejecutable.*
- **`--add-data "src:dest"`:** *Especifica los ficheros de datos adicionales y sus destinos en el ejecutable. La sintaxis es `"source_path:destination_path"`.*
- **`cli/main.py`:** *El fichero principal del script.*

### ***Ejecución del Comando***

*Ejecuta el comando en la terminal desde el directorio donde se encuentra tu fichero `cli/main.py`. PyInstaller se encargará de empaquetar tu aplicación, incluyendo los directorios y ficheros adicionales especificados.*

*Si necesitas ajustar las rutas de los ficheros de datos, asegúrate de que las rutas sean correctas en relación con el directorio en el que estás ejecutando el comando.*

### ***Solución de Problemas***

- **Error de `objcopy`:** *Si encuentras errores relacionados con `objcopy`, asegúrate de que todos los ficheros de entrada sean correctos y que no haya problemas con los permisos de fichero. Verifica que el fichero especificado en `--name` no esté en uso y que el directorio de trabajo esté limpio.*

- **Dependencias Faltantes:** *Si el ejecutable falla debido a dependencias faltantes, asegúrate de que todas las bibliotecas requeridas estén instaladas y accesibles desde el entorno de Python.*

### ***Contribuir***

**Si deseas contribuir a `pycrypy`, por favor sigue estos pasos:**

1. **Hacer un Fork del Repositorio**.

2. **Crear una Nueva Rama** *para tu funcionalidad o corrección de errores.*

3. **Realizar Cambios** *y hacer commit de tus cambios.*

4. **Enviar un Pull Request** *con una descripción clara de los cambios realizados.*

### ***Licencia***

> *Este repositorio se publica bajo la Licencia MIT. Siéntete libre de utilizar, modificar y distribuir el contenido de acuerdo con los términos de esta licencia.*

### ***Autor***

- **Autor:** *Daniel Benjamin Perez Morales*

- **GitHub:** *[DanielPerezMoralesDev13](https://github.com/DanielPerezMoralesDev13 "https://github.com/DanielPerezMoralesDev13")*

- **Correo electrónico:** *`danielperezdev@proton.me`*
