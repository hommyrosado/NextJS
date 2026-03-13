# Next.js + Bootstrap CRUD App — Getting Started

npx prisma studio

This guide walks you through creating a basic CRUD (Create, Read, Update, Delete) web application using **Next.js** and **Bootstrap**. We will start with the fundamentals and build a clean foundation you can expand later.

---

## 🧱 Prerequisites

Make sure you have the following installed:

- Node.js (v18 or newer recommended)
- npm or yarn
- Git
- A code editor (VS Code recommended)

Verify installations:

```bash
node -v
npm -v
```

---

## 🚀 Step 1 — Create a Next.js App

Create a new Next.js project using the App Router (recommended):

```bash
npx create-next-app@latest nextjs-bootstrap-crud
cd nextjs-bootstrap-crud
```

When prompted, choose:

- ✔ TypeScript: Yes (recommended)
- ✔ ESLint: Yes
- ✔ App Router: Yes
- ✔ Tailwind: No (we are using Bootstrap)
- ✔ src directory: Yes (optional but recommended)

Start the dev server:

```bash
npm run dev
```

Open:

```
http://localhost:3000
```

---

## 🎨 Step 2 — Install Bootstrap

Install Bootstrap:

```bash
npm install bootstrap
```

### Import Bootstrap globally

Open:

```
src/app/layout.tsx
```

Add at the top:

```tsx
import "bootstrap/dist/css/bootstrap.min.css";
```

⚠️ Important: Do **not** import Bootstrap in multiple files.

---

## 📁 Step 3 — Create Basic Project Structure

Inside `src`, create:

```
src/
 ├── app/
 ├── components/
 │    └── ItemForm.tsx
 │    └── ItemList.tsx
 ├── lib/
 │    └── data.ts
 └── types/
      └── item.ts
```

---

## 🧩 Step 4 — Define the Data Type

Create:

```
src/types/item.ts
```

```ts
export interface Item {
  id: number;
  name: string;
  description: string;
}
```

---

## 🗄️ Step 5 — Create Temporary Data Store

For now we'll use in‑memory data (later you can swap for a database).

Create:

```
src/lib/data.ts
```

```ts
import { Item } from "@/types/item";

let items: Item[] = [
  { id: 1, name: "Sample Item", description: "This is a sample" },
];

export function getItems() {
  return items;
}

export function addItem(item: Item) {
  items.push(item);
}

export function deleteItem(id: number) {
  items = items.filter((i) => i.id !== id);
}
```

---

## 🧱 Step 6 — Create Item List Component

Create:

```
src/components/ItemList.tsx
```

```tsx
"use client";

import { Item } from "@/types/item";

interface Props {
  items: Item[];
  onDelete: (id: number) => void;
}

export default function ItemList({ items, onDelete }: Props) {
  return (
    <table className="table table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Description</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        {items.map((item) => (
          <tr key={item.id}>
            <td>{item.name}</td>
            <td>{item.description}</td>
            <td>
              <button
                className="btn btn-danger btn-sm"
                onClick={() => onDelete(item.id)}
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
```

---

## ✏️ Step 7 — Create Item Form Component

Create:

```
src/components/ItemForm.tsx
```

```tsx
"use client";

import { useState } from "react";

interface Props {
  onAdd: (name: string, description: string) => void;
}

export default function ItemForm({ onAdd }: Props) {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onAdd(name, description);
    setName("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="mb-3">
        <input
          className="form-control"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
      </div>

      <div className="mb-3">
        <input
          className="form-control"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
        />
      </div>

      <button className="btn btn-primary">Add Item</button>
    </form>
  );
}
```

---

## 🏠 Step 8 — Wire Everything in Home Page

Edit:

```
src/app/page.tsx
```

```tsx
"use client";

import { useState } from "react";
import ItemForm from "@/components/ItemForm";
import ItemList from "@/components/ItemList";
import { Item } from "@/types/item";

export default function Home() {
  const [items, setItems] = useState<Item[]>([]);

  const handleAdd = (name: string, description: string) => {
    const newItem: Item = {
      id: Date.now(),
      name,
      description,
    };
    setItems((prev) => [...prev, newItem]);
  };

  const handleDelete = (id: number) => {
    setItems((prev) => prev.filter((i) => i.id !== id));
  };

  return (
    <div className="container mt-4">
      <h1 className="mb-4">Next.js Bootstrap CRUD</h1>
      <ItemForm onAdd={handleAdd} />
      <ItemList items={items} onDelete={handleDelete} />
    </div>
  );
}
```

---

## ✅ Step 9 — Run the App

```bash
npm run dev
```

You now have a working **Create + Read + Delete** app.

---

## 🔜 Next Steps (Future Enhancements)

When you're ready, we can add:

- Update/Edit functionality
- API routes
- Database (PostgreSQL, MongoDB, etc.)
- Server Actions
- Form validation
- Authentication
- Docker support

---

**Say the word when you want Phase 2 (real backend + full CRUD).**

AI_Homelab/
├── app/
│ ├── api/
│ │ └── items/
│ │ └── route.ts # Controller
│ └── page.tsx # View
│
├── components/ # View pieces
│
├── lib/
│ ├── db.ts # DB connection
│ └── services/ # Model/business logic
│ └── itemService.ts
│
├── prisma/
│ └── schema.prisma # Model schema
│
└── types/
