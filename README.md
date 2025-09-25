# TelcoX - Plataforma de Autogestión de Telecomunicaciones

Solución de prueba técnica para el módulo de visualización de consumo en tiempo real para clientes de telecomunicaciones.

## 🚀 Características

- **Visualización en tiempo real** del consumo de datos y minutos
- **API RESTful** que simula integración con sistemas BSS
- **Frontend responsivo** con Bootstrap y Angular
- **Actualización automática** cada 30 segundos
- **Manejo de errores** robusto
- **Containerización** con Docker

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.9** con Flask
- **Flask-CORS** para manejo de CORS
- **API RESTful** con datos mockeados

### Frontend
- **Angular** (versión 16+)
- **Bootstrap 5** para estilos
- **Font Awesome** para iconos
- **RxJS** para manejo de observables

### DevOps
- **Docker** y **Docker Compose**
- Containerización completa

## 📋 Prerrequisitos

- Node.js (16+)
- Python 3.9+
- Docker y Docker Compose
- Angular CLI

## 🚀 Instalación y Ejecución

### Opción 1: Con Docker (Recomendada)

1. **Clonar el repositorio**
   ```bash
   git clone <tu-repositorio>
   cd telcox-platform
   ```

2. **Ejecutar con Docker Compose**
   ```bash
   docker-compose up --build
   ```

3. **Acceder a la aplicación**
   - Frontend: http://localhost:4200
   - Backend API: http://localhost:5000

### Opción 2: Instalación Manual

#### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd frontend
npm install
ng serve
```

## 📡 API Endpoints

### GET `/api/health`
Verificación de estado del servicio
```json
{
  "status": "healthy",
  "timestamp": "2025-01-20T10:30:00"
}
```

### GET `/api/customer/{id}/consumption`
Obtener consumo del cliente
```json
{
  "customer_id": "12345",
  "customer_name": "Juan Pérez",
  "plan": "Premium",
  "balance": 45.50,
  "data": {
    "consumed_gb": 32.5,
    "limit_gb": 50,
    "remaining_gb": 17.5,
    "usage_percentage": 65.0
  },
  "minutes": {
    "consumed": 450,
    "limit": 1000,
    "remaining": 550,
    "usage_percentage": 45.0
  },
  "last_updated": "2025-01-20T10:30:00"
}
```

### GET `/api/customers`
Listar clientes disponibles
```json
[
  {
    "id": "12345",
    "name": "Juan Pérez",
    "plan": "Premium"
  }
]
```

## 🧪 Testing

### Tests Backend
```bash
cd backend
python -m pytest test_app.py -v
```

### Tests Frontend
```bash
cd frontend
ng test
```

## 🏗️ Arquitectura

```
┌─────────────────┐    HTTP/REST    ┌─────────────────┐
│                 │◄───────────────►│                 │
│   Frontend      │                 │   Backend       │
│   (Angular)     │                 │   (Flask)       │
│                 │                 │                 │
└─────────────────┘                 └─────────────────┘
        │                                     │
        │                                     │
        ▼                                     ▼
┌─────────────────┐                 ┌─────────────────┐
│   Bootstrap     │                 │   Mock BSS      │
│   Components    │                 │   Data          │
└─────────────────┘                 └─────────────────┘
```

## 💾 Estructura del Proyecto

```
telcox-platform/
├── backend/
│   ├── app.py                 # Aplicación Flask principal
│   ├── test_app.py           # Tests unitarios
│   ├── requirements.txt      # Dependencias Python
│   └── Dockerfile           # Imagen Docker backend
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── consumption/
│   │   │   │   ├── consumption.component.ts
│   │   │   │   ├── consumption.component.html
│   │   │   │   └── consumption.component.css
│   │   │   └── app.module.ts
│   │   └── main.ts
│   ├── package.json
│   └── Dockerfile           # Imagen Docker frontend
├── docker-compose.yml       # Orquestación de contenedores
└── README.md               # Este archivo
```

## ⚡ Funcionalidades Implementadas

### ✅ Módulo de Visualización
- [x] Consumo de datos en tiempo real
- [x] Consumo de minutos de llamadas
- [x] Información del cliente y saldo
- [x] Barras de progreso visuales
- [x] Actualización automática cada 30s

### ✅ Integración Frontend-Backend
- [x] API RESTful funcional
- [x] Manejo de errores HTTP
- [x] Validación de datos
- [x] Mensajes de error amigables
- [x] Loading states

### ✅ Documentación y Pruebas
- [x] Documentación completa del API
- [x] Tests unitarios backend
- [x] README detallado
- [x] Comentarios en código

## 🔧 Configuración

### Variables de Entorno
- `FLASK_ENV`: Entorno de Flask (development/production)
- Backend corre en puerto `5000`
- Frontend corre en puerto `4200`

### Datos de Prueba
El sistema incluye dos usuarios de prueba:
- **Juan Pérez** (ID: 12345) - Plan Premium
- **María García** (ID: 67890) - Plan Basic

## 🐳 Docker

### Construir imágenes
```bash
docker-compose build
```

### Ejecutar en background
```bash
docker-compose up -d
```

### Ver logs
```bash
docker-compose logs -f
```

### Detener servicios
```bash
docker-compose down
```

## 🚨 Notas Importantes

- **Datos mockeados**: El sistema simula un BSS real con datos en memoria
- **CORS habilitado**: Para desarrollo local
- **Actualización automática**: Los datos se actualizan cada 30 segundos
- **Responsive design**: Optimizado para móvil y desktop

## 🔄 Mejoras Futuras

- Integración con base de datos MySQL
- Autenticación y autorización
- Websockets para actualizaciones en tiempo real
- Caching con Redis
- Métricas y monitoring
- Tests de integración más completos

## 📝 Autor

Desarrollado como prueba técnica para TelcoX.

---

**¡La plataforma está lista para liderar la transformación digital en TelcoX!** 🚀