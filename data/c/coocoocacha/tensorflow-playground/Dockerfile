FROM python:3.5  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.9.0-cp35-cp35m-linux_x86_64.whl  
ENV KERAS_BACKEND tensorflow  
  
RUN apt-get update && \  
apt-get install -y libhdf5-dev  
  
RUN pip install --upgrade pip Cython  
RUN pip install --upgrade $TF_BINARY_URL  
RUN pip install --upgrade numpy keras scipy matplotlib pillow pandas retrying
scikit-learn h5py notebook gensim spacy flask  
  
RUN python3 -m spacy.en.download  
  
RUN mkdir -p /app/notebooks  
WORKDIR /app  
  
EXPOSE 8888  
CMD jupyter notebook --no-browser --ip=0.0.0.0 --port 8888 --notebook-
dir=/app/notebooks  

