## BioGPT: Transforming Biomedical Research with AI

BioGPT is a pre-trained language model developed by Microsoft, specialized in generating and mining biomedical text. It is based on the GPT-2 architecture and trained on millions of scientific articles to perform tasks like question answering, data extraction, and generating relevant biomedical literature.
[GitHub Repository](https://github.com/microsoft/BioGPT?utm_source=chatgpt.com)


## Description

This repository contains the BioGPT implementation, including pre-trained and fine-tuned checkpoints for specific tasks such as question answering on PubMedQA.
Developed by Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, and Tie-Yan Liu.
[GitHub Repository](https://github.com/microsoft/BioGPT?utm_source=chatgpt.com)


## Requirements and Installation

To use BioGPT, install the following dependencies:

* **PyTorch** version 1.12.0
* **Python** version 3.10
* **fairseq** version 0.12.0
* **Moses** for tokenization
* **fastBPE** for BPE encoding
* **sacremoses**
* **scikit-learn**

Follow the repository instructions for detailed setup.
[Installation Guide](https://github.com/microsoft/BioGPT?utm_source=chatgpt.com)


## Usage Example

Load the pre-trained BioGPT model with the following Python code:

```python
import torch
from fairseq.models.transformer_lm import TransformerLanguageModel

model = TransformerLanguageModel.from_pretrained(
    'checkpoints/Pre-trained-BioGPT',
    checkpoint_file='checkpoint.pt',
    data_dir='data',
    tokenizer='moses',
    bpe='biogpt-large-fastbpe',
    bpe_codes='data/biogpt_large_bpecodes'
)

model.cuda()
src_tokens = model.encode('COVID-19 is')
generated = model.generate([src_tokens], beam=5)[0]
output = model.decode(generated[0]['tokens'])
print(output)
```

[Example Reference](https://github.com/microsoft/BioGPT/issues/36?utm_source=chatgpt.com)


## Badges

Add badges to highlight key info in your README:

```markdown
![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)
![PyTorch 1.12.0](https://img.shields.io/badge/PyTorch-1.12.0-red.svg)
```

Badges quickly convey license, Python, and PyTorch versions used.

## References

* [BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining](https://pubmed.ncbi.nlm.nih.gov/36156661/)
* [GitHub Implementation](https://github.com/microsoft/BioGPT)
* [Hugging Face Model Hub](https://huggingface.co/microsoft/biogpt)
