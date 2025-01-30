import re
import csv

# Ruta del archivo HTML de Instant Gaming
html_file_path = "Compra tus videojuegos más baratos para PC y consolas - Instant Gaming.html"
csv_output_path = "imagenes_instant_gaming2.csv"

# Función para cargar el HTML
def cargar_html(archivo):
    with open(archivo, 'r', encoding="utf-8") as f:
        return f.read()

# Función para extraer las imágenes y los nombres de productos
def extraer_productos(html):
    # Expresión regular para encontrar las imágenes dentro de <a> con data-src y alt
    regex = r'<a[^>]*>.*?<img[^>]*data-src="(https://gaming-cdn\.com/images/products/[^"]+)"[^>]*alt="([^"]+)"'
    
    # Buscar todas las coincidencias en el HTML
    productos = re.findall(regex, html, re.DOTALL)
    
    return productos  # Devuelve una lista de tuplas (URL de imagen, Nombre del producto)

# Función para exportar a CSV
def exportar_csv(productos, archivo_salida):
    with open(archivo_salida, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["URL de la imagen", "Nombre del producto"])
        writer.writerows(productos)

# Cargar el HTML
html_content = cargar_html(html_file_path)

# Extraer productos
productos_extraidos = extraer_productos(html_content)

# Exportar a CSV
exportar_csv(productos_extraidos, csv_output_path)

print(f"Se encontraron {len(productos_extraidos)} productos. El archivo '{csv_output_path}' ha sido generado.")
