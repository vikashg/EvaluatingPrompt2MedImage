import os
import time
import json
import numpy as np
import pandas as pd

import torch
from torch.utils.data import Dataset, DataLoader

from transformers import GPT2Tokenizer, GPT2LMHeadModel, AdamW, GPT2Config
from transformers import get_linear_schedule_with_warmup
import nltk

nltk.download('punkt')
from tqdm import tqdm, trange
import torch
from diffusers import StableDiffusionPipeline
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import BartTokenizer, BartForConditionalGeneration
from transformers import PegasusTokenizer, PegasusForConditionalGeneration


def paraphrase_report(report, name="BART"):
    if name == "BART":
        model_name = 'facebook/bart-base'
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)
    elif name == "pegasus":
        model_name = 'tuner007/pegasus_paraphrase'
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name)
    elif name == 'T5':
        tokenizer = T5Tokenizer.from_pretrained("t5-base", model_max_length=1024)
        model = T5ForConditionalGeneration.from_pretrained("t5-base")

    sentences_list = report.split('.')
    paraphrased_sentence = []
    for sentence in sentences_list:
        input_ids = tokenizer.encode(sentence, return_tensors='pt')
        paraphrase_ids = model.generate(input_ids, num_beams=5,
                                        max_length=100, early_stopping=True)
        paraphrase = tokenizer.decode(paraphrase_ids[0], skip_special_tokens=True)
        paraphrased_sentence.append(paraphrase)
    return paraphrased_sentence


def generate_image(prompt, output_path):
    model_id = "Nihirc/Prompt2MedImage"
    device = "cuda"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.to(device)
    image = pipe(prompt).images[0]
    image.save(output_path)


def convert_sent_to_paragraph(sentence_list):
    """
    Given a list of sentences. Join the elements into a paragraph
    :param sentence_list:
    :return:
    """
    print("Sentence List ", sentence_list)
    paragraph = sentence_list[0]
    for _ in sentence_list[1:]:
        paragraph += _
    return paragraph
