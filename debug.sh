text_data=/raid/Vikash/Tools/Language/language_data/files
image_data=/raid/Vikash/Tools/Language/chest-x-ray-dataset-with-lung-segmentation-1.0.0
app_dir=/raid/Vikash/Tools/Paraphrase_Prompt/app

docker build -t vikash/nlp:0.1.0 .
NV_GPU=2, nvidia-docker run -it --rm --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -v $image_data:/workspace/data/image -v $text_data:/workspace/data/text -v $app_dir:/workspace/app vikash/nlp:0.1.0 /bin/bash
