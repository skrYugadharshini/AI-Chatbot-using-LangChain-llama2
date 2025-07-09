# AI-Chatbot-using-LangChain-llama2 / LLaMA 2–7B Chat Fine-Tuning with QLoRA on Colab

LangChain, llama2 from Olama and Streamlit.

We will reformat our instruction dataset to follow Llama 2 template.

1.Orignal Dataset: https://huggingface.co/datasets/timdettmers/openassistant-guanaco

2.Reformat Dataset following the Llama 2 template with 1k sample: https://huggingface.co/datasets/mlabonne/guanaco-llama2-1k

3.Complete Reformat Dataset following the Llama 2 template: https://huggingface.co/datasets/mlabonne/guanaco-llama2

To know how this dataset was created, you can check this notebook.

https://colab.research.google.com/drive/1Ad7a9zMmkxuXTOh1Z7-rNSICA4dybpM2?usp=sharing


This project fine-tunes the LLaMA 2–7B Chat model on the guanaco-llama2-1k dataset using QLoRA, a parameter-efficient fine-tuning method optimized for low-resource GPUs.

![image](https://github.com/user-attachments/assets/5e3495dd-fd3f-4563-99be-8bd334eb4a43)


🧠 Objective
Train a custom instruction-following model using the LLaMA 2–7B Chat model and a cleaned instruction dataset (Guanaco) following the LLaMA 2 prompt template.



📦 Dataset
Original Dataset: timdettmers/openassistant-guanaco

Formatted Dataset (LLaMA 2 template): mlabonne/guanaco-llama2-1k

To understand how this dataset was prepared, refer to the Colab Notebook.
![image](https://github.com/user-attachments/assets/4540d3be-daf9-412f-9520-ed4b86316ba9)




⚙️ Fine-Tuning Approach
Due to Colab’s limited VRAM (~15GB), full fine-tuning isn't feasible. Instead, we use QLoRA, which enables training large models using:

4-bit quantization (NF4)

LoRA adapters (low-rank approximation)

Parameter-efficient fine-tuning (PEFT)

![image](https://github.com/user-attachments/assets/4cd920b4-3229-4253-beaa-5b5177a35d3f)





🔧 Steps to Fine-Tune LLaMA 2–7B Chat Using QLoRA

Choose the base model – Select LLaMA 2–7B Chat from Hugging Face.

Select a dataset – Use or reformat an instruction dataset like openassistant-guanaco.

Reformat the dataset – Follow the LLaMA 2 chat format with user/assistant roles.

Load dataset into Colab – Use the preprocessed dataset (e.g., guanaco-llama2-1k).

Install required libraries – Set up transformers, peft, bitsandbytes, and trl.

Enable 4-bit quantization – Use BitsAndBytes to load the model in 4-bit (NF4) precision.

Configure QLoRA – Set LoRA rank, scaling factor, and dropout for adapter training.

Set training parameters – Define batch size, learning rate, gradient steps, etc.

Start fine-tuning – Train the model using SFTTrainer for 1 epoch.

Save the model – Store the fine-tuned model locally or push to Hugging Face.

Evaluate the model – Test the model’s response quality on new prompts.







