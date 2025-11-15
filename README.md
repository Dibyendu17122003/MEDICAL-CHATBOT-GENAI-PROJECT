# 🏥 MedNova AI - Medical Vision Chatbot

<div align="center">

<!-- Banner -->
<img src="https://via.placeholder.com/1200x400/1e40af/ffffff?text=MedNova+AI+🏥+Medical+Vision+Chatbot" alt="MedNova Banner" style="border-radius: 15px; margin: 20px 0;">

<!-- Badges -->
<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-000000?style=for-the-badge&logo=openai&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![AI](https://img.shields.io/badge/🤖_AI_Powered-10B981?style=for-the-badge)
![Medical](https://img.shields.io/badge/🏥_Medical_Tech-EF4444?style=for-the-badge)

</div>

**An intelligent medical vision AI assistant for educational image analysis and healthcare guidance**

<div align="center">

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-1E40AF?style=for-the-badge&logo=streamlit&logoColor=white)](https://medical-chatbot-genai-project-dibyendu.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/💻_GitHub_Repo-Click_Here-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dibyendu17122003/MEDICAL-CHATBOT-GENAI-PROJECT)
[![LinkedIn](https://img.shields.io/badge/👨‍💻_LinkedIn-Connect_Now-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dibyendu-karmahapatra-17d2004/)

</div>

</div>

## 📋 Table of Contents

<!-- TOC -->
- [🌟 Overview](#-overview)
- [🚀 Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [⚙️ Installation](#️-installation)
- [🎯 Usage](#-usage)
- [🔧 Tech Stack](#-tech-stack)
- [📊 Workflow](#-workflow)
- [🛡️ Disclaimer](#️-disclaimer)
- [🤝 Contributing](#-contributing)
- [👨‍💻 Developer](#-developer)

## 🌟 Overview

<div align="center">

**MedNova AI** represents the next generation of medical AI assistants, combining cutting-edge vision models with an intuitive interface to revolutionize medical image analysis and healthcare education.

</div>

### 🎯 What is MedNova?

MedNova AI is an **advanced medical vision chatbot** that leverages state-of-the-art AI technology to provide:
- 🔬 **Educational medical image analysis**
- 💡 **Intelligent healthcare guidance**
- 📊 **Visual analytics and insights**
- 🎓 **Learning resources for medical education**

### ✨ Key Innovations

| Feature | Innovation | Impact |
|---------|------------|--------|
| **Multi-format Support** | DICOM, PNG, JPG, JPEG | Comprehensive medical imaging |
| **Real-time Streaming** | Live AI response generation | Enhanced user experience |
| **Smart Analytics** | Automated severity assessment | Data-driven insights |
| **Educational Focus** | Patient-friendly explanations | Better health literacy |

## 🚀 Features

### 🎯 Core Capabilities

<div align="center">

| Feature Category | Capabilities | Technologies Used |
|------------------|--------------|-------------------|
| **🖼️ Image Analysis** | Multi-format support, DICOM processing, Thumbnail preview | Pillow, OpenRouter Vision |
| **💬 Intelligent Chat** | Real-time streaming, Context-aware responses, History management | Streamlit, OpenRouter API |
| **📊 Analytics Dashboard** | Severity distribution, Historical analysis, Visual insights | Plotly, Session State |
| **🎨 User Experience** | Modern UI, Mobile responsive, Error handling | Custom CSS, Streamlit Components |

</div>

### 🎨 User Experience Features

```mermaid
graph TD
    A[Modern UI/UX] --> B[Real-time Streaming]
    A --> C[Error Handling]
    A --> D[Mobile Responsive]
    
    B --> E[Live Responses]
    B --> F[Progress Indicators]
    
    C --> G[Graceful Failures]
    C --> H[User Notifications]
    
    D --> I[Cross-device Compatibility]
    D --> J[Touch-friendly Interface]
    
    style A fill:#3b82f6,color:white
    style B fill:#8b5cf6,color:white
    style C fill:#ef4444,color:white
    style D fill:#10b981,color:white
```

### 🔧 Advanced Functionalities

- **🔄 Session Management**: Persistent chat history and analysis records
- **📈 Progress Tracking**: Real-time response streaming with visual indicators
- **🛡️ Error Resilience**: Comprehensive error handling and user notifications
- **🎯 Smart Routing**: Multi-page navigation with state persistence
- **📱 Responsive Design**: Optimized for desktop and mobile devices

## 🏗️ Architecture

### System Architecture Overview

```mermaid
graph TB
    subgraph "Frontend Layer"
        A[Streamlit UI<br>User Interface]
        B[Session Management<br>State Handling]
        C[Real-time Updates<br>Streaming Responses]
    end
    
    subgraph "Application Layer"
        D[MedicalVisionBot<br>Core Logic]
        E[Image Processing<br>Pillow Library]
        F[Error Handling<br>Exception Management]
    end
    
    subgraph "AI Service Layer"
        G[OpenRouter API<br>Vision Models]
        H[Stream Processing<br>Chunked Responses]
        I[Rate Limit Management<br>Error Recovery]
    end
    
    subgraph "Data Layer"
        J[Session Storage<br>Temporary Data]
        K[Analysis Records<br>Historical Data]
        L[Visualization Data<br>Plotly Charts]
    end
    
    A --> B --> D
    D --> E --> G
    G --> H --> D
    D --> F --> A
    D --> J --> K --> L --> A
    
    style A fill:#1e40af,color:white
    style D fill:#3b82f6,color:white
    style G fill:#8b5cf6,color:white
    style J fill:#10b981,color:white
```

### Component Interaction Flow

```mermaid
sequenceDiagram
    participant U as User
    participant FE as Frontend (Streamlit)
    participant MB as MedicalVisionBot
    participant OR as OpenRouter API
    participant DB as Data Storage
    
    U->>FE: Upload Image + Question
    FE->>MB: Process Request with Image Data
    MB->>OR: Send Vision API Request
    OR-->>MB: Stream Response Chunks
    MB->>FE: Update UI in Real-time
    FE->>DB: Store Analysis Results
    FE->>U: Display Final Analysis
    FE->>U: Update Analytics Dashboard
```

## 📁 Project Structure

### Complete File Architecture

```
medical-chatbot-genai-project/
├── 📁 .streamlit/
│   ├── config.toml
│   └── secrets.toml
├── 📁 src/
│   ├── 📁 medical_bot/
│   │   ├── __init__.py
│   │   ├── medical_vision_bot.py
│   │   └── models.py
│   ├── 📁 error_handling/
│   │   ├── __init__.py
│   │   ├── error_utils.py
│   │   └── exceptions.py
│   └── 📁 utils/
│       ├── __init__.py
│       ├── image_processing.py
│       └── session_utils.py
├── 📁 assets/
│   ├── images/
│   └── styles/
├── 📁 tests/
│   ├── test_medical_bot.py
│   ├── test_image_processing.py
│   └── test_error_handling.py
├── 📄 app.py
├── 📄 requirements.txt
├── 📄 setup.py
├── 📄 .gitignore
├── 📄 README.md
└── 📄 LICENSE
```

### Detailed File Descriptions

| File/Folder | Purpose | Key Components |
|-------------|---------|----------------|
| **`app.py`** | Main application entry point | UI components, routing, session management |
| **`src/medical_bot/`** | Core AI logic | API integration, model definitions |
| **`src/error_handling/`** | Error management | Custom exceptions, error utilities |
| **`src/utils/`** | Utility functions | Image processing, session helpers |
| **`.streamlit/config.toml`** | Streamlit configuration | Theme, server settings |
| **`requirements.txt`** | Dependencies | All required Python packages |

## ⚙️ Installation

### 🛠️ Prerequisites

<div align="center">

| Requirement | Version | Purpose |
|-------------|---------|---------|
| **Python** | 3.8+ | Core programming language |
| **OpenRouter API Key** | - | AI model access |
| **Git** | Latest | Version control |
| **pip** | 21.0+ | Package management |

</div>

### 🚀 Quick Start Guide

```bash
# 1. Clone the repository
git clone https://github.com/Dibyendu17122003/MEDICAL-CHATBOT-GENAI-PROJECT.git
cd MEDICAL-CHATBOT-GENAI-PROJECT

# 2. Create and activate virtual environment
python -m venv mednova_env

# Windows
mednova_env\Scripts\activate

# macOS/Linux
source mednova_env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
# Create .streamlit/secrets.toml and add:
echo 'OPENROUTER_API_KEY = "your_api_key_here"' > .streamlit/secrets.toml

# 5. Launch the application
streamlit run app.py
```

### 📋 Complete Requirements

```txt
# Core Framework
streamlit>=1.28.0
Pillow>=10.0.0

# Data & Visualization
plotly>=5.15.0
numpy>=1.24.0
pandas>=2.0.0

# AI & API Integration
openai>=1.0.0
nest_asyncio>=1.5.0
httpx>=0.24.0

# Development & Testing
pytest>=7.0.0
black>=23.0.0
mypy>=1.0.0

# Utilities
python-dotenv>=1.0.0
typing-extensions>=4.0.0
```

### 🔧 Configuration

Create `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#1e40af"
backgroundColor = "#f3f8ff"
secondaryBackgroundColor = "#ffffff"
textColor = "#262730"
font = "sans serif"

[server]
port = 8501
address = "0.0.0.0"
```

## 🎯 Usage

### 📖 Comprehensive User Guide

```mermaid
journey
    title User Interaction Journey
    section Image Upload
      Access Application: 5: User
      Upload Medical Images: 5: User
      Preview Thumbnails: 4: System
    section Chat Interaction
      Ask Medical Questions: 5: User
      Real-time AI Processing: 5: System
      Receive Analysis: 5: System
    section Analysis & Insights
      View Severity Assessment: 4: User
      Check Analytics Dashboard: 4: User
      Review Historical Data: 3: User
    section Health Education
      Browse Health Tips: 4: User
      Learn Prevention: 4: User
      Export Findings: 3: User
```

### 🎮 Step-by-Step Usage

#### 1. **🖼️ Image Upload Process**
```python
# Supported formats
formats = ["png", "jpg", "jpeg", "dcm"]
max_size = "10MB per image"
features = ["Multi-file upload", "Thumbnail preview", "Format validation"]
```

#### 2. **💬 Chat Interaction**
- **Input**: Type medical questions in the chat interface
- **Processing**: Real-time AI analysis with streaming responses
- **Output**: Comprehensive medical insights and explanations

#### 3. **📊 Analytics Dashboard**
- **Severity Distribution**: Pie charts showing condition severity
- **Historical Analysis**: Review past consultations
- **Trend Visualization**: Plotly-powered interactive charts

#### 4. **❤️ Health Tips Section**
- **Preventive Care**: 25+ health recommendations
- **Lifestyle Guidance**: Diet, exercise, mental health tips
- **Educational Content**: Patient-friendly medical information

## 🔧 Tech Stack

### Technology Architecture

```mermaid
pie title Technology Stack Distribution
    "Frontend (Streamlit)" : 35
    "AI Backend (OpenRouter)" : 30
    "Data Visualization (Plotly)" : 15
    "Image Processing (Pillow)" : 12
    "Async Handling & Utilities" : 8
```

### Detailed Technology Breakdown

<div align="center">

| Technology | Version | Purpose | Key Features |
|------------|---------|---------|--------------|
| **Streamlit** | ≥1.28.0 | Frontend Framework | Real-time updates, Session state, Custom components |
| **OpenRouter** | Latest | AI Model Gateway | Vision models, Streaming API, Rate limiting |
| **Plotly** | ≥5.15.0 | Visualization | Interactive charts, Real-time updates, Export capabilities |
| **Pillow** | ≥10.0.0 | Image Processing | Multi-format support, Thumbnail generation, DICOM handling |
| **nest_asyncio** | ≥1.5.0 | Async Support | Event loop management, Async operation handling |

</div>

### 🛠️ Development Tools

- **Code Quality**: Black, MyPy, Pytest
- **Version Control**: Git, GitHub
- **Deployment**: Streamlit Cloud
- **Monitoring**: Streamlit analytics, Error tracking

## 📊 Workflow

### Complete Application Workflow

```mermaid
graph TD
    A[User Access] --> B[Upload Images]
    B --> C[Image Processing]
    C --> D[AI Analysis]
    D --> E{Analysis Success?}
    E -->|Yes| F[Generate Report]
    E -->|No| G[Error Handling]
    F --> H[Update Dashboard]
    G --> I[User Notification]
    H --> J[Store Results]
    J --> K[Display Insights]
    K --> L[User Review]
    L --> M{New Query?}
    M -->|Yes| B
    M -->|No| N[Session End]
    
    style A fill:#3b82f6,color:white
    style D fill:#8b5cf6,color:white
    style F fill:#10b981,color:white
    style G fill:#ef4444,color:white
    style H fill:#f59e0b,color:white
```

### Error Handling Workflow

```mermaid
graph LR
    A[User Action] --> B{API Call}
    B -->|Success| C[Process Response]
    B -->|Error| D{Error Type}
    D -->|429 Rate Limit| E[Show Limit Message]
    D -->|API Error| F[Show API Error]
    D -->|Network Error| G[Show Network Message]
    D -->|Unexpected Error| H[Show Generic Error]
    E --> I[User Notification]
    F --> I
    G --> I
    H --> I
    C --> J[Success Response]
    
    style A fill:#3b82f6,color:white
    style B fill:#f59e0b,color:white
    style C fill:#10b981,color:white
    style D fill:#ef4444,color:white
```

## 🛡️ Disclaimer

<div align="center">

⚠️ **CRITICAL MEDICAL DISCLAIMER**

</div>

### 🚨 Important Safety Information

> **This application is designed for EDUCATIONAL AND INFORMATIONAL PURPOSES ONLY. It is NOT a substitute for professional medical advice, diagnosis, or treatment.**

### 🔒 Key Limitations

| Aspect | Limitation | Recommendation |
|--------|------------|----------------|
| **Accuracy** | AI models can make errors | Always verify with healthcare professionals |
| **Diagnosis** | Not for clinical diagnosis | Consult qualified medical practitioners |
| **Emergency** | Not for emergency situations | Contact emergency services for urgent care |
| **Treatment** | No treatment recommendations | Follow prescribed medical treatments |

### 📜 Compliance Notes

- 🔍 **Educational Tool**: For learning and understanding only
- 🩺 **Professional Consultation**: Always seek expert medical advice
- 📊 **Data Privacy**: Your data is handled securely but avoid sharing sensitive information
- 🔬 **Research Purpose**: Intended for medical education and research

## 🤝 Contributing

### 🎯 Contribution Guidelines

We welcome contributions from the community! Here's how you can help:

### 📝 How to Contribute

```mermaid
graph TD
    A[Fork Repository] --> B[Create Branch]
    B --> C[Make Changes]
    C --> D[Run Tests]
    D --> E[Submit PR]
    E --> F[Code Review]
    F --> G{Merge?}
    G -->|Yes| H[Merge to Main]
    G -->|No| I[Request Changes]
    I --> C
    
    style A fill:#3b82f6,color:white
    style E fill:#f59e0b,color:white
    style H fill:#10b981,color:white
```

### 🛠️ Development Setup

```bash
# 1. Fork and clone
git clone https://github.com/your-username/MEDICAL-CHATBOT-GENAI-PROJECT.git

# 2. Set up development environment
pip install -r requirements-dev.txt

# 3. Run tests
pytest tests/ -v

# 4. Code formatting
black src/ app.py tests/

# 5. Type checking
mypy src/

# 6. Create pull request
git checkout -b feature/your-feature-name
```

### 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test module
pytest tests/test_medical_bot.py

# Run with coverage
pytest --cov=src tests/

# Run integration tests
pytest tests/integration/ -v
```

## 👨‍💻 Developer

<div align="center">

### **Dibyendu Karmahapatra**

[![GitHub](https://img.shields.io/badge/💻_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Dibyendu17122003)
[![LinkedIn](https://img.shields.io/badge/👨‍💻_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dibyendu-karmahapatra-17d2004/)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-8B5CF6?style=for-the-badge&logo=google-chrome&logoColor=white)](https://your-portfolio-link.com)

**AI & Machine Learning Enthusiast | Full Stack Developer | Medical Tech Innovator**

</div>

### 🔧 Technical Skills

- **AI/ML**: Python, TensorFlow, PyTorch, Computer Vision
- **Web Development**: Streamlit, React, FastAPI, Node.js
- **Cloud & DevOps**: AWS, Docker, CI/CD, MLOps
- **Data Science**: Pandas, NumPy, Plotly, Data Visualization

### 📫 Connect With Me

<div align="center">

[![Email](https://img.shields.io/badge/📧_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:your.email@example.com)
[![Twitter](https://img.shields.io/badge/🐦_Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/your-handle)
[![Medium](https://img.shields.io/badge/📝_Medium-000000?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@your-handle)

</div>

---

<div align="center">

## 🏆 Acknowledgments

**Special thanks to the open-source community and all contributors who make projects like this possible.**

[![Open Source](https://img.shields.io/badge/💙_Open_Source-22C55E?style=for-the-badge&logo=opensourceinitiative&logoColor=white)]()
[![MIT License](https://img.shields.io/badge/📜_MIT_License-3DA639?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)

**⭐ Star this repo if you find it helpful!**

[![Star](https://img.shields.io/github/stars/Dibyendu17122003/MEDICAL-CHATBOT-GENAI-PROJECT?style=social)](https://github.com/Dibyendu17122003/MEDICAL-CHATBOT-GENAI-PROJECT)

</div>
