<div align="center">

# BioGPT-Lab
<img width="931" height="382" alt="image" src="https://github.com/user-attachments/assets/fc1d609e-3dbd-4f89-9ee0-5e8842da2363" />

### An interactive biomedical AI assistant powered by BioGPT  
*Ask questions about biology, medicine, and scientific literature—right from your browser.*

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.20%2B-FF4B4B)](https://streamlit.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-009688)](https://fastapi.tiangolo.com/)
[![HuggingFace](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-BioGPT-orange)](https://huggingface.co/microsoft/BioGPT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)]()

</div>

## Overview

**BioGPT-Lab** brings the power of [Microsoft’s BioGPT](https://huggingface.co/microsoft/BioGPT)—a large language model fine-tuned on biomedical literature—into an easy-to-use web interface.  

Built with:
- 🧠 **BioGPT** for domain-specific, accurate biomedical responses  
- ⚡ **FastAPI** backend for robust, scalable inference  
- 🖥️ **Streamlit** frontend for a clean, responsive user experience  

Perfect for researchers, students, and clinicians who want to explore scientific knowledge without leaving their browser.

## Quick Start

### Prerequisites
- Python 3.9+
- GPU (recommended for faster inference; CPU works but slower)

### 1. Clone the repo
```bash
git clone https://github.com/CllsPy/BioGPT.git
cd BioGPT
```

### 2. Install dependencies
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install packages
pip install -r requirements.txt
```

> **Note**: The first run will download the BioGPT model (~1.5 GB) from Hugging Face.

### 3. Launch the backend
```bash
uvicorn api.main:app --reload --port 8000
```

### 4. Launch the frontend
In a **new terminal**:
```bash
streamlit run app.py --server.port=8501
```

### 5. Open your browser
Go to: http://localhost:8501  
Start asking biomedical questions like:
> _"What are the symptoms of Parkinson's disease?"_  
> _"Explain CRISPR-Cas9 gene editing."_


## 🛠️ API Usage (Standalone)

You can also use the FastAPI backend directly:

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is mRNA vaccine mechanism?"}'
```

Response:
```json
{"response": "mRNA vaccines work by..."}
```

## Contributing

Contributions are welcome! Whether it’s:
- Adding new biomedical evaluation metrics  
- Supporting additional models (e.g., BioGPT-2, PubMedBERT)  
- Improving UI/UX  
- Writing documentation  

Feel free to open an issue or submit a PR!



## License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.

> ⚠️ **Disclaimer**: BioGPT-Lab is for **research and educational purposes only**. It is not a medical diagnostic tool. Always consult a healthcare professional for medical advice.



<div align="center">

✨ **Empowering biomedical discovery through accessible AI** ✨

</div>

### Assets Recommendation

- Add a real screenshot of your Streamlit app to `assets/screenshot.png` (you can take one after running locally).
- If you have a logo or diagram (e.g., architecture flow), include it!


### Next Steps for You

1. **Add the screenshot** to your repo under `/assets`.
2. **Verify port numbers** in the README match your actual setup (currently assumes 8000 for FastAPI, 8501 for Streamlit).
3. **Consider adding a `.env` example** if you plan to support API keys or model variants later.
