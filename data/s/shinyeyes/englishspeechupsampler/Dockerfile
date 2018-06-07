FROM tensorflow/tensorflow:1.5.1-gpu-py3  
  
WORKDIR /app  
  
ADD . /app  
  
RUN apt update  
  
RUN apt install -y sox  
  
RUN pip install librosa==0.5.0 tqdm==4.11.2 sox==1.2.7 --user  
  
RUN echo 'test'  

