# ***Para distribuir un paquete de Python, necesitarás preparar y subir tu paquete a un repositorio de Python, como PyPI (Python3 Package Index) o TestPyPI (un índice de paquetes de prueba). Aquí tienes una guía detallada sobre los pasos y comandos involucrados***

## ***[https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/ "https://pypi.org/manage/account/token/")***

- **Propósito:** *Esta página te permite gestionar los tokens de API para tu cuenta en PyPI. Los tokens de API son una forma segura de autenticarte al publicar paquetes o interactuar con el repositorio PyPI sin necesidad de usar tu contraseña.*

- **Funcionalidades:**
  - **Crear un nuevo token:** *Puedes generar un nuevo token para usar en lugar de tu contraseña cuando subas paquetes o realices otras operaciones que requieran autenticación.*
  - **Ver tokens existentes:** *Puedes ver una lista de tokens que has creado y sus permisos asociados.*
  - **Revocar tokens:** *Puedes eliminar o revocar tokens que ya no necesitas o que creas que podrían haber sido comprometidos.*

### ***[https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/ "https://test.pypi.org/manage/account/token/")***

- **Propósito:** *Esta página es similar a la de PyPI, pero para TestPyPI. Te permite gestionar tokens de API para tu cuenta en TestPyPI, que es un entorno de prueba para paquetes de Python.*

- **Funcionalidades:**
  - **Crear un nuevo token:** *Generar un token para autenticarte al subir paquetes a TestPyPI.*
  - **Ver tokens existentes:** *Consultar los tokens que has creado para TestPyPI.*
  - **Revocar tokens:** *Eliminar tokens que ya no necesites o que creas que pueden estar comprometidos.*

### ***[https://pypi.org/help/#apitoken](https://pypi.org/help/#apitoken "https://pypi.org/help/#apitoken")***

- **Propósito:** *Esta página proporciona información y ayuda sobre el uso de tokens de API en PyPI. Ofrece detalles sobre cómo crear y utilizar tokens para autenticarte y realizar operaciones en PyPI.*

- **Contenido:**
  - **Introducción a los tokens de API:** *Explica qué son los tokens de API y por qué son útiles.*
  - **Cómo crear un token:** *Instrucciones paso a paso para generar un nuevo token desde tu cuenta en PyPI.*
  - **Uso de tokens de API:** *Información sobre cómo usar tokens para autenticarte en lugar de contraseñas al subir paquetes con herramientas como `twine` o `setuptools`.*

### ***Tokens de API***

**¿Qué son?**

- *Los **tokens de API** son credenciales seguras que reemplazan el uso de contraseñas para interactuar con servicios web. Se utilizan para autenticar peticiones de una manera más segura y conveniente.*

**¿Por qué usarlos?**

- **Seguridad:** *Los tokens pueden ser revocados fácilmente y no exponen tu contraseña. Esto reduce el riesgo si el token es comprometido.*
- **Permisos Granulares:** *Puedes asignar diferentes permisos a cada token, limitando su uso a operaciones específicas.*
- **Control y Gestión:** *Puedes gestionar y auditar tokens fácilmente desde las páginas de administración de tu cuenta.*

### ***Ejemplo de Uso de Tokens***

*Cuando subes un paquete con `twine`, puedes utilizar un token en lugar de una contraseña para la autenticación:*

```bash
twine upload --repository pypi dist/*
```

*En tu archivo de configuración `~/.pypirc`, puedes usar el token en lugar de una contraseña:*

```ini
[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = <token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <token>
```

*Aquí, `__token__` indica que estás usando un token en lugar de una contraseña.*

### ***En Resumen***

- **PyPI Tokens:** *Para gestionar tokens en PyPI, crear, ver, y revocar tokens para la autenticación.*
- **TestPyPI Tokens:** *Similar a PyPI, pero para el entorno de prueba TestPyPI.*
- **Guía de Tokens de API:** *Información general y ayuda sobre el uso de tokens de API en PyPI.*

*Usar tokens de API es una buena práctica para la seguridad y gestión de acceso en la distribución de paquetes de Python.*

## ***Explicación del Archivo `~/.pypirc`***

*El archivo `~/.pypirc` permite que herramientas como `twine` utilicen credenciales y configuraciones para interactuar con repositorios de paquetes. Aquí se especifican dos secciones principales: `pypi` y `testpypi`.*

### ***Estructura del Archivo***

```ini
[distutils]
index-servers =
    pypi
    testpypi
```

- **`[distutils]`:** *Esta sección define los servidores de índice a los que se puede enviar paquetes.*
- **`index-servers`:** *Lista de los servidores de índice que se usarán para las cargas. En este caso, se especifican `pypi` y `testpypi`.*

#### ***Sección `pypi`***

```ini
[pypi]
repository = https://upload.pypi.org/legacy/
username = <user>
password = <token>
```

- **`[pypi]`:** *Configuración específica para el repositorio PyPI.*
- **`repository`:** *URL del repositorio de PyPI donde se suben los paquetes.*
- **`username`:** *Tu nombre de usuario en PyPI.*
- **`password`:** *La contraseña o token de autenticación para PyPI.*

#### ***Sección `testpypi`***

```ini
[testpypi]
repository = https://test.pypi.org/legacy/
username = <user>
password = <token>
```

- **`[testpypi]`:** *Configuración específica para el repositorio TestPyPI.*
- **`repository`:** *URL del repositorio de TestPyPI.*
- **`username`:** *Tu nombre de usuario en TestPyPI.*
- **`password`:** *La contraseña o token de autenticación para TestPyPI.*

### ***Propósito de Cada Sección***

- **`[distutils]`:** *Configura los servidores de índice que `distutils` utilizará para la carga de paquetes. Esto es útil si estás usando comandos de `distutils` o `setuptools` para subir paquetes.*
  
- **`[pypi]`:** *Contiene la configuración para subir paquetes al índice principal de PyPI. Especifica la URL del repositorio, el nombre de usuario y la contraseña para la autenticación.*

- **`[testpypi]`:** *Contiene la configuración para subir paquetes al índice de prueba de TestPyPI. Similar a la sección de `pypi`, pero para el entorno de prueba.*

### ***Dónde Crear el Archivo***

**El archivo `~/.pypirc` debe ser creado en el directorio home del usuario. Esto se hace típicamente mediante:**

1. *Abriendo un editor de texto y creando el archivo `~/.pypirc`.*
2. *Insertando la configuración mencionada.*
3. *Guardando y cerrando el archivo.*

### **Ejemplo de Creación del Archivo**

**En la terminal, puedes crear el archivo usando un editor de texto como `nano`:**

```bash
nano ~/.pypirc
```

*Luego, pega el contenido de configuración en el archivo y guarda los cambios. Para salir de `nano`, presiona `Ctrl + X`, luego `Y` para confirmar los cambios, y `Enter` para guardar.*

### ***Consideraciones de Seguridad***

- **Tokens en lugar de contraseñas:** *Para mayor seguridad, es recomendable usar tokens de autenticación en lugar de contraseñas en texto claro.*
- **Permisos del archivo:** *Asegúrate de que el archivo `~/.pypirc` tenga permisos adecuados para proteger tus credenciales. Puedes ajustar los permisos con:*

  ```bash
  chmod 600 ~/.pypirc
  ```

  *Esto asegurará que solo tu usuario pueda leer y escribir en el archivo.*

**PyPI** *(Python3 Package Index) y **TestPyPI** son servicios utilizados para distribuir y probar paquetes de Python. Aquí está un resumen de cada uno:*

## ***PyPI (Python3 Package Index)***

- **Qué es:** *PyPI es el repositorio oficial y principal para paquetes de Python. Es el lugar donde los desarrolladores publican sus paquetes para que otros puedan encontrarlos, instalarlos y usarlos en sus proyectos.*

- **Uso:**
  - **Distribución:** *Permite que los desarrolladores suban sus paquetes para que estén disponibles para la comunidad de Python.*
  - **Instalación:** *Los usuarios pueden instalar paquetes desde PyPI utilizando `pip`, por ejemplo, `pip install nombre-del-paquete`.*

- **Características:**
  - **Alcance Global:** *Es el repositorio más grande y accesible para la comunidad de Python.*
  - **Estabilidad:** *Los paquetes aquí están destinados para el uso en producción y se espera que sean estables.*

- **Sitio web:** *[PyPI](https://pypi.org/ "https://pypi.org/")*

### ***TestPyPI***

- **Qué es:** *TestPyPI es una versión de prueba de PyPI. Está diseñado para que los desarrolladores puedan probar la distribución de sus paquetes antes de publicarlos en el PyPI oficial.*

- **Uso:**
  - **Pruebas:** *Permite a los desarrolladores probar la carga y la instalación de paquetes en un entorno que simula PyPI, sin afectar el índice principal.*
  - **Validación:** *Ofrece un entorno para verificar cómo se comportará el paquete una vez publicado.*

- **Características:**
  - **Separación de Entornos:** *TestPyPI está separado de PyPI, lo que significa que los paquetes publicados aquí no se mostrarán en el PyPI principal.*
  - **Pruebas de Integración:** *Ideal para asegurarse de que todo el proceso de carga, instalación y funcionamiento del paquete es correcto.*

- **Sitio web:** *[TestPyPI](https://test.pypi.org/ "https://test.pypi.org/")*

### ***Cómo Usar PyPI y TestPyPI***

1. **Subir a TestPyPI:** *Puedes subir tus paquetes a TestPyPI para verificar que todo funcione correctamente antes de hacer la publicación oficial. Esto te permite asegurarte de que el paquete se construye y se instala correctamente sin afectar a los usuarios finales.*

   ```bash
   twine upload --repository testpypi dist/* --verbose
   ```

2. **Subir a PyPI:** *Una vez que hayas verificado que el paquete funciona correctamente en TestPyPI, puedes proceder a subirlo a PyPI para que esté disponible para la comunidad en general.*

   ```bash
   twine upload --repository pypi dist/* --verbose
   ```

### ***Resumen***

- **PyPI:** *El repositorio principal para paquetes de Python; es el lugar donde se publican y distribuyen paquetes para uso general.*
- **TestPyPI:** *Un entorno de prueba para verificar cómo funcionará un paquete antes de su publicación en PyPI.*

*Ambos servicios son importantes en el proceso de distribución de paquetes, con TestPyPI proporcionando un entorno de prueba antes de la publicación final en PyPI.*

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = <user>
password = <token>

[testpypi]
repository = https://test.pypi.org/legacy/
username = <user>
password = <token>
```

## ***Preparar el Paquete***

- **Instalar Herramientas Necesarias**

- *Antes de comenzar, asegúrate de tener instaladas las herramientas necesarias:*

  ```bash
  pip install setuptools wheel twine
  ```

- **`setuptools`:** *Utilidad para empaquetar proyectos en Python.*
- **`wheel`:** *Proporciona un formato de archivo de distribución (`.whl`) para los paquetes de Python.*
- **`twine`:** *Herramienta para subir paquetes a PyPI o TestPyPI.*

- **Actualizar Herramientas**

  *Asegúrate de tener las versiones más recientes de estas herramientas:*

  ```bash
  pip install --upgrade setuptools twine
  ```

- **`--upgrade`:** *Actualiza las herramientas a la última versión disponible.*

- **Crear Distribuciones**

  *Dentro del directorio raíz de tu proyecto, donde está el archivo `setup.py`, ejecuta:*

  ```bash
  python3 setup.py sdist bdist_wheel
  ```

- **`sdist`:** *Crea una distribución fuente (archivo `.tar.gz`).*
- **`bdist_wheel`:** *Crea una distribución en formato wheel (`.whl`).*

  *Esto generará los archivos en el directorio `dist`.*

- **Instalar el Paquete Localmente para Pruebas**

  *Puedes instalar tu paquete localmente en modo editable para pruebas:*

  ```bash
  pip install -e .
  ```

- **`-e`:** *Instala el paquete en modo editable, permitiendo que los cambios en el código fuente se reflejen sin necesidad de reinstalar.*

- **Desinstalar el Paquete**

  *Para desinstalar el paquete de tu entorno:*

  ```bash
  pip uninstall pycrypy
  ```

### ***Subir el Paquete***

- **Subir el Paquete a PyPI**

  *Si estás listo para distribuir tu paquete al público, usa Twine para subirlo a PyPI:*

  ```bash
  twine upload --repository pypi dist/* --verbose
  ```

- **`--repository pypi`:** *Especifica que se debe usar el repositorio PyPI.*
- **`dist/*`:** *Subirá todos los archivos en el directorio `dist`.*
- **`--verbose`:** *Proporciona información detallada sobre el proceso de carga.*

- **Subir el Paquete a TestPyPI**

  *Si deseas probar el paquete en un entorno de prueba antes de subirlo a PyPI, usa TestPyPI:*

  ```bash
  twine upload --repository testpypi dist/* --verbose
  ```

- **`--repository testpypi`:** *Especifica que se debe usar el repositorio TestPyPI.*

### ***Comandos Adicionales***

- **Generar un archivo de distribución**

  ```bash
  python3 setup.py sdist bdist_wheel
  ```

  *Este comando es fundamental para crear los archivos de distribución que se subirán a PyPI o TestPyPI.*

- **Verificar el Paquete**

  *Puedes verificar el contenido del archivo `.whl` con `twine`:*

  ```bash
  twine check dist/*
  ```

  - **`check`:** *Verifica que el archivo de distribución cumple con las normas y especificaciones.*

> [!IMPORTANT]
> *En PyPI, no es posible usar la versión `0.0.0` para un paquete. Según las reglas de versionado y la política de versionado semántico (semver), las versiones deben seguir un formato de `MAJOR.MINOR.PATCH` y `0.0.0` es una versión no válida.*

**Aquí está la razón:**

### ***Razones por las que `0.0.0` no es válida***

1. **Versionado Semántico:** *El versionado semántico establece que la versión mínima para una versión de liberación debe ser `1.0.0`. Las versiones anteriores a `1.0.0` se utilizan para la fase de desarrollo y pre-liberación, y deben seguir un formato que refleje esa etapa, como `0.1.0`, `0.2.0`, etc.*

2. **Restricciones de PyPI:** *PyPI no acepta versiones `0.0.0`. Si intentas subir un paquete con esta versión, PyPI te dará un error de validación.*

### **Versiones Alternativas para Desarrollo**

- **`0.1.0` o `0.0.1`:** *Para paquetes en desarrollo o en etapas iniciales, utiliza versiones como `0.1.0` o `0.0.1` para indicar que es una versión temprana o en desarrollo.*

- **`dev`, `alpha`, `beta`, `rc`:** *Puedes usar etiquetas como `dev`, `alpha`, `beta`, y `rc` para indicar que la versión es una versión de desarrollo o una versión candidata:*

  - *`0.1.0.dev1`*
  - *`0.1.0a1` (alpha)*
  - *`0.1.0b1` (beta)*
  - *`0.1.0rc1` (release candidate)*

> [!NOTE]
> *En el desarrollo de software, especialmente en el contexto de librerías y paquetes de Python, el uso de diferentes versiones ayuda a comunicar el estado y la estabilidad del software a los usuarios y desarrolladores. Las versiones `0.1.0.dev1`, `0.1.0a1`, `0.1.0b1`, y `0.1.0rc1` siguen las prácticas de **versionado semántico** y **versionado de pre-liberación** para indicar el progreso del desarrollo del software. Aquí te explico cada uno de estos:*

### ***`0.1.0.dev1` (Versión de Desarrollo)***

- **Uso:** *Se utiliza para versiones en desarrollo que no están listas para el público general. Estas versiones pueden contener características experimentales y cambios frecuentes.*

- **Objetivo:** *Permitir que los desarrolladores y colaboradores trabajen con una versión temprana del software, recibir retroalimentación y probar características en desarrollo.*

- **Características:**
  - *No es considerada estable ni completamente funcional.*
  - *Puede ser utilizada internamente o por un grupo selecto de usuarios que están probando el software.*
  - *El número `dev1` indica la primera versión de desarrollo. Si hay más versiones de desarrollo, podrían ser `dev2`, `dev3`, etc.*

### ***`0.1.0a1` (Versión Alpha)***

- **Uso:** *Indica una versión temprana del software que está disponible para pruebas internas y para un grupo limitado de usuarios. Los lanzamientos alfa pueden contener muchos errores y características aún no completas.*

- **Objetivo:** *Obtener retroalimentación temprana sobre nuevas características y asegurar que el software está en una dirección correcta antes de llegar a una etapa más estable.*

- **Características:**
  - *La versión `a1` significa la primera versión alfa. Pueden haber más versiones alfa, como `a2`, `a3`, etc., a medida que se realizan cambios y mejoras.*

### ***`0.1.0b1` (Versión Beta)***

- **Uso:** *Representa una versión más madura que la alfa. Está destinada a un público más amplio para pruebas más extensas y para corregir errores significativos antes del lanzamiento final.*

- **Objetivo:** *Recolectar retroalimentación de una base de usuarios más amplia, identificar errores y problemas que no se detectaron en las fases alfa, y realizar ajustes finales.*

- **Características:**
  - *La versión `b1` es la primera versión beta. Pueden haber versiones beta adicionales, como `b2`, `b3`, etc., que reflejan correcciones y mejoras adicionales.*

### ***`0.1.0rc1` (Versión Release Candidate)***

- **Uso:** *Es una versión casi final del software que está destinada a ser la candidata para la liberación oficial. Es la versión final de prueba antes de la versión estable.*

- **Objetivo:** *Confirmar que el software está listo para la liberación final, asegurarse de que todos los problemas importantes han sido resueltos y que la versión está lista para la producción.*

- **Características:**
  - *La versión `rc1` es la primera versión candidata. Puede haber varias versiones candidatas (como `rc2`, `rc3`, etc.) si se encuentran problemas adicionales que necesitan ser corregidos.*

### ***Ejemplo Práctico en el Desarrollo***

**Imagina que estás desarrollando una nueva librería de Python para manejo de datos:**

1. **Desarrollo Inicial:**
   - *Lanzas `0.1.0.dev1` para compartir con tu equipo interno y obtener retroalimentación sobre las características básicas.*

2. **Primera Prueba Externa:**
   - *Publicas `0.1.0a1` para un grupo selecto de testers externos para probar nuevas características y detectar problemas.*

3. **Pruebas Ampliadas:**
   - *Lanzas `0.1.0b1` para una base de usuarios más amplia para pruebas más extensas y corrección de errores.*

4. **Preparación para el Lanzamiento:**
   - *Publicas `0.1.0rc1` para una última ronda de pruebas antes de la liberación final, asegurándote de que todo esté listo y sin errores críticos.*

### ***Conclusión***

*Estas versiones de pre-liberación permiten a los desarrolladores gestionar el ciclo de vida del software, obteniendo retroalimentación, identificando y corrigiendo errores, y asegurando que la versión final sea lo más estable y confiable posible. Al seguir estos patrones de versionado, puedes comunicar claramente el estado de tu software y facilitar un proceso de desarrollo más organizado.*

### ***Ejemplo de Versión Correcta***

**En lugar de `0.0.0`, usa una versión como `0.1.0` para una versión inicial de desarrollo:**

```ini
[metadata]
name = my_package
version = 0.1.0
description = A description of my package.
```

### ***Verificación de Versiones en PyPI***

**Para verificar las versiones de un paquete en PyPI:**

1. **Visita la página del paquete en [PyPI](https://pypi.org/ "https://pypi.org/")**
2. **Consulta la lista de versiones:** *En la página del paquete, busca la sección de versiones para ver qué versiones están disponibles y cuáles han sido publicadas.*

*Si encuentras `0.0.0` en el historial de versiones de un paquete, puede ser un error o un problema de carga y sería recomendable corregirlo para seguir las prácticas estándar.*

### ***Pasos para Eliminar una Versión en PyPI***

*Para eliminar una versión específica de un paquete en PyPI y volver a subirla, sigue estos pasos. Esto es útil si necesitas corregir un error en una versión específica que ya has publicado.*

1. **Inicia sesión en PyPI:**
   - *Ve a [PyPI](https://pypi.org/ "https://pypi.org/") e inicia sesión con tu cuenta.*

2. **Navega a tu paquete:**
   - *Dirígete a la página del paquete del que deseas eliminar una versión específica.*

3. **Accede a la pestaña de versiones:**
   - *En la página del paquete, encontrarás una lista de versiones. Selecciona la versión que deseas eliminar.*

4. **Eliminar la versión:**
   - *Dentro de la vista de la versión específica, busca el botón o enlace para **Eliminar**. Este botón suele estar en la parte superior derecha de la página de la versión o en un menú de opciones.*
   - *Haz clic en **Eliminar** y confirma la acción cuando se te solicite.*

### ***Alternativa: Usando `twine`***

*PyPI no ofrece una interfaz directa para eliminar versiones específicas desde la línea de comandos, pero puedes usar `twine` para realizar algunas acciones, aunque para eliminar versiones tendrás que hacerlo desde la interfaz web de PyPI.*

### ***Reutilización del Nombre del Archivo***

- **PyPI tiene una política que evita la reutilización de nombres de archivos para versiones diferentes. Una vez que una versión ha sido subida, no puedes reutilizar el nombre del archivo para una nueva versión. Sin embargo, puedes actualizar la versión del paquete y subir una nueva versión con el mismo nombre de archivo, pero con un número de versión diferente.**

### ***Importante***

- **No puedes eliminar una versión si tiene dependencias:** *Si otras versiones o paquetes dependen de la versión que deseas eliminar, PyPI podría no permitir la eliminación para evitar romper dependencias.*

- **Política de Nombres de Archivos:** *Recuerda que PyPI no permite la reutilización del nombre del archivo para versiones diferentes. Siempre debes cambiar el número de versión si necesitas subir una nueva versión.*

*Siguiendo estos pasos podrás eliminar una versión específica de tu paquete y volver a subir una versión corregida o actualizada.*

### ***Resumen:***

 **Instalar herramientas:** *`pip install setuptools wheel twine`*
 **Actualizar herramientas:** *`pip install --upgrade setuptools twine`*
 **Crear distribuciones:** *`python3 setup.py sdist bdist_wheel`*
 **Instalar localmente:** *`pip install -e .`*
 **Desinstalar:** *`pip uninstall pycrypy`*
 **Subir a PyPI:** *`twine upload --repository pypi dist/* --verbose`*
 **Subir a TestPyPI:** *`twine upload --repository testpypi dist/* --verbose`*
 **Verificar el paquete:** *`twine check dist/*`*

- *Estos pasos cubren el proceso de empaquetado y distribución de un paquete de Python. Asegúrate de que todo esté bien configurado y probado antes de publicar en PyPI.*
