FROM python:slim-bullseye
RUN apt-get update && apt-get install -y vim openssh-server
RUN apt install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0
RUN pip install requests
RUN pip install matplotlib
RUN pip install nltk
RUN pip install textdistance
RUN pip install numpy
RUN pip install pandas
RUN pip install gensim
RUN pip install spacy transformers
RUN pip install torch 
RUN pip install transforms
RUN pip install timm
RUN pip install opencv-python 
RUN pip install diffusers
RUN pip install accelerate
RUN pip install SentencePiece
