# LangGraph - Build Stateful, Agentic AI Graphs
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/krunalp1908/Langggraph---Build-Stateful-Agentic-AI-Graph.git)

This project provides a framework for building stateful, multi-agent AI systems using LangGraph. It leverages the power of Groq for high-speed language model inference and provides an interactive user interface built with Streamlit. The architecture is designed to be modular, allowing for easy extension with different LLMs, tools, and agentic workflows.

## Features

*   **Stateful Agentic Architecture:** Utilizes LangGraph to create and manage stateful agent graphs.
*   **High-Speed LLM Integration:** Powered by the `langchain-groq` integration for fast and efficient LLM responses.
*   **Interactive UI:** A user-friendly interface built with Streamlit allows for real-time interaction and configuration.
*   **Modular Design:** Code is organized into distinct modules for LLMs, graphs, nodes, and UI, facilitating easy maintenance and expansion.
*   **Example Use Case:** Includes a "Basic Chatbot" to demonstrate the core functionality. The framework is prepared for more complex use cases like "Chatbot with Tool", "AI News", and "Blog Generator".

## Project Structure

The repository is organized to separate concerns, making it easy to understand and extend.

```
.
├── app.py                  # Main entry point to run the Streamlit application
├── requirements.txt        # Project dependencies
└── src/
    └── langgraphagenticai/
        ├── LLMs/           # Language Model configurations (e.g., Groq)
        │   └── groqllm.py
        ├── graph/          # Graph building and compilation logic
        │   └── graph_builder.py
        ├── nodes/          # Individual nodes for the agent graph
        │   └── basic_chatbot_node.py
        ├── state/          # Defines the state structure for the graph
        │   └── state.py
        └── ui/             # User interface components
            ├── uiconfigfile.ini
            └── streamlitui/
                ├── loadui.py
                └── display_result.py
```

## Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites

*   Python 3.13 or higher

### Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/krunalp1908/langggraph---build-stateful-agentic-ai-graph.git
    ```

2.  Navigate to the project directory:
    ```bash
    cd langggraph---build-stateful-agentic-ai-graph
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

This application requires a Groq API key to function. You can obtain a free key from the [Groq Console](https://console.groq.com/keys). The API key is entered directly into the application's sidebar UI when you run it.

### Running the Application

Launch the Streamlit application by running the following command in your terminal:

```bash
streamlit run app.py
```

## Usage

1.  After running the command above, open the local URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.
2.  In the sidebar on the left:
    *   The "Selected LLM" will be pre-selected to "Groq".
    *   Choose your preferred Groq model from the "Select Model" dropdown.
    *   Enter your Groq API key into the "API Key" password field.
    *   Select a use case from the "Select Usecases" dropdown (e.g., "Basic Chatbot").
3.  Type your message into the chat input at the bottom of the main page and press Enter.
4.  The agent will process your request, and the response will be streamed back into the chat interface.