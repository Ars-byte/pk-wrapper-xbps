# pk — Interfaz simplificada para xbps en Void Linux

`pk` es una interfaz de línea de comandos amigable que envuelve los comandos principales de `xbps` (`install`, `remove`, `query`, `rindex`, `up`) en funciones simples y rápidas. Con autocompletado bash integrado, te permite gestionar paquetes con menos escritura y más eficiencia.

---

## ✨ Funciones disponibles

| Comando | Acción |
|--------|--------|
| `pk install <paquete>` | Instala uno o más paquetes (equivalente a `xbps-install -y`) |
| `pk remove <paquete>` | Elimina uno o más paquetes (equivalente a `xbps-remove -y`) |
| `pk query [patrón]` | Lista paquetes instalados o busca por nombre |
| `pk rindex` | Actualiza el índice local de paquetes (`xbps-rindex -a`) |
| `pk up` | Actualiza todo el sistema (`sudo xbps-install -Syu`) |

> 💡 Todas las funciones muestran la salida en **tiempo real**, como si ejecutaras los comandos originales.

---

## 🚀 Uso rápido

```bash
pk install firefox neofetch
pk remove firefox
pk query vim
pk rindex
pk up
```
