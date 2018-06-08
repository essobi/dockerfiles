FROM continuumio/miniconda3  
  
MAINTAINER Dmitry Ustalov <dmitry.ustalov@gmail.com>  
  
EXPOSE 9090  
COPY requirements.txt /usr/src/app/  
  
RUN \  
conda install gensim && \  
pip install --no-cache-dir -r /usr/src/app/requirements.txt && \  
conda clean -a  
  
WORKDIR /usr/src/app  
  
COPY server.py .  
  
USER nobody  
  
CMD ["python", "server.py", "/usr/src/app/w2v.bin"]  

