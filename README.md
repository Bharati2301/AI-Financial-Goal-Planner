# 🏆 **AI Financial Goal Planner**

## 📌 **Overview**
This project is part of the **CSCI-572 - Information Retrieval and Web Search Engines** course at USC. The goal is to build an **AI-powered financial goal planner** that helps users create personalized savings plans based on their income, expenses, and financial goals (e.g., saving for a house, retirement, or paying off debt). The AI uses **LLaMA 3.1**, **ChromaDB**, and **Open Banking APIs** to generate optimized plans.

---

## 🎯 **Project Goals**

- **Build a financial goal planner** to help users create personalized savings plans.
- **Use AI-driven recommendations** to match financial strategies to users' goals.
- **Integrate Open Banking APIs** (Yodlee) to analyze real-time spending patterns.
- **Optimize user savings plans** using a heuristic-based approach to improve financial strategies.

---

## 💡 **Features**

- **Personalized savings plans** generated based on user input (income, expenses, goals).
- **AI-driven recommendations** to optimize strategies for goals like buying a house, retirement, or paying off loans.
- **Real-time progress tracking** with visual indicators (progress bar, suggestions).
- **Integration with Open Banking APIs** (Yodlee) to pull in actual spending and transaction data.
- **Step-by-step savings plans** designed to help users achieve their financial goals faster.

---

## 🛠️ **Implementation Details**

This project uses advanced AI models and databases to help users achieve financial goals by generating personalized plans. The key components are:

- **LLaMA 3.1**: Language model for generating the savings plans.
- **ChromaDB**: Vector database for storing and retrieving financial strategies and plans.
- **Open Banking APIs** (Yodlee): For pulling real-time financial data like transactions and balances.
- **Streamlit**: A web framework for developing an interactive user interface.

---

## 🧠 **Algorithms Used**

1. **Personalized Savings Plan Generation 🤖**  
   LLaMA 3.1 is used to generate tailored savings plans based on user input, including income, expenses, and financial goals.

2. **Recommendation System 🧠**  
   A RAG-based recommendation system uses **ChromaDB** to match users' financial goals with relevant strategies, improving the likelihood of goal achievement.

3. **Heuristic Evaluation 🎯**  
   The evaluation function is designed to assess the best strategies for saving, considering factors such as user spending habits, savings targets, and timeframes.

---

## 📌 **Future Improvements**

- **Implement Monte Carlo Tree Search (MCTS)** to improve probabilistic decision-making.
- **Optimize the heuristic evaluation function** for better accuracy in financial planning.
- **Integrate more data sources** like credit scores and investment plans to offer more holistic financial advice.
