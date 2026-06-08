# 🛒 E-Commerce Product Recommendation Engine

## 📖 Project Overview
This project is an algorithmic backend for an E-Commerce Recommendation Engine. It mimics the logic used by platforms like Amazon and Flipkart to analyze user interactions (views, carts, purchases) and suggest highly relevant products in real-time.

## 🎯 Problem Statement
E-commerce catalogs are massive. Users experience decision fatigue without personalized filtering. This system solves that by transforming raw interaction logs into mathematically ranked product suggestions, increasing platform engagement and potential revenue.

## 🧠 DSA Concepts Used
* **HashMaps (Dictionaries):** Used for O(1) time complexity lookups mapping User IDs to interaction histories and Product IDs to catalog details.
* **Priority Queue (Min-Heap):** Used via Python's `heapq` module to dynamically maintain the Top-N highest-scoring items. This avoids sorting the entire product catalog, reducing ranking complexity to O(K log N).
* **Sets:** Used to track unique user views and cart items, ensuring O(1) deduplication.

## ⚙️ Features
* Custom similarity scoring weighting purchases heavier than views.
* Avoids recommending already purchased items.
* Category-affinity matching.
* CLI interface for easy simulation.

## 📂 Folder Structure
(See structure defined in section 5)

## 🚀 How to Run
```bash
python main.py