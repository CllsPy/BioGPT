<div align="center">

# BioGPT-Lab
<img width="931" height="382" alt="image" src="https://github.com/user-attachments/assets/fc1d609e-3dbd-4f89-9ee0-5e8842da2363" />

Pre-trained language models have attracted increasing attention in the biomedical domain, inspired by their great success in the general natural language domain. Among the two main branches of pre-trained language models in the general language domain, i.e. BERT (and its variants) and GPT (and its variants), the first one has been extensively studied in the biomedical domain, such as BioBERT and PubMedBERT. While they have achieved great success on a variety of discriminative downstream biomedical tasks, the lack of generation ability constrains their application scope. In this paper, we propose BioGPT, a domain-specific generative Transformer language model pre-trained on large-scale biomedical literature. We evaluate BioGPT on six biomedical natural language processing tasks and demonstrate that our model outperforms previous models on most tasks. Especially, we get 44.98%, 38.42% and 40.76% F1 score on BC5CDR, KD-DTI and DDI end-to-end relation extraction tasks, respectively, and 78.2% accuracy on PubMedQA, creating a new record. Our case study on text generation further demonstrates the advantage of BioGPT on biomedical literature to generate fluent descriptions for biomedical terms.

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
- **BioGPT** for domain-specific, accurate biomedical responses  
- **FastAPI** backend for robust, scalable inference  
- **Streamlit** frontend for a clean, responsive user experience  

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
conda env create -f environment.yml
conda activate biogpt-chatbot
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
