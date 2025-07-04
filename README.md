
# 🧪 Mock JSON Server

A simple mock server that serves JSON responses from files, based on the request path and method.  
Designed to quickly prototype APIs or test clients without implementing backend logic.

## 📋 Features

✅ Fully automatic routing — no need to define routes explicitly.  
✅ Supports all HTTP methods (GET, POST, PUT, DELETE, PATCH, OPTIONS).  
✅ Reads responses from `.json` files following a predictable naming convention.  
✅ Returns a 404 if no matching JSON file is found.  
✅ CORS enabled by default — ready for browser-based clients.

## 📄 File Naming Convention

For a request to:
```
METHOD /path/to/resource
```
the server looks for:
```
responses/path-to-resource_METHOD.json
```

### Examples:

| Request                 | JSON file                                |
|-------------------------|------------------------------------------|
| `GET /store/locations`  | `responses/store-locations_GET.json`     |
| `POST /users/login`     | `responses/users-login_POST.json`        |
| `DELETE /inventory/42`  | `responses/inventory-42_DELETE.json`     |

## 🚀 Quick Start

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/mock-json-server.git
cd mock-json-server
```

### 2️⃣ Create and activate a virtual environment (recommended)

#### On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

or manually:
```bash
pip install flask flask-cors
```

### 4️⃣ Add your response files
Create a `responses/` folder (if it doesn’t already exist) and put your `.json` files there, following the naming convention.

Example:
```
responses/store-locations_GET.json
responses/users-login_POST.json
responses/inventory-42_DELETE.json
```

### 5️⃣ Run the server
```bash
python3 app.py
```

The server runs on [http://localhost:5050](http://localhost:5050) by default.

## 🛠 Example `responses/store-locations_GET.json`

```json
[
    {
        "id": "f1",
        "name": "Central Warehouse",
        "type": "warehouse",
        "role": "storage",
        "capacity": 1000,
        "active": true
    },
    {
        "id": "f2",
        "name": "Main Clinic",
        "type": "clinic",
        "role": "healthcare",
        "capacity": 250,
        "active": true
    },
    {
        "id": "f3",
        "name": "Remote Outpost",
        "type": "outpost",
        "role": "distribution",
        "capacity": 60,
        "active": false
    }
]
```

## 🔗 Routes

All requests are handled by a **catch-all route**, which maps the request path & method to the corresponding `.json` file.

If the file is missing, a 404 is returned.

## 📂 Project Structure

```
.
├── app.py
├── responses/
│   ├── store-locations_GET.json
│   └── ...
├── requirements.txt
├── README.md
└── venv/ (optional)
```

## 📝 License

MIT — feel free to use and modify.
