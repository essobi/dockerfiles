FROM ubuntu:14.04  
MAINTAINER "Hiroki Arai <hiroara62@gmail.com>"  
RUN apt-get update && apt-get -yq install autoconf libtool build-essential
wget  
  
RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -O /tmp/Miniconda3.sh && \  
chmod +x /tmp/Miniconda3.sh && /tmp/Miniconda3.sh -b  
  
ENV PATH=$PATH:/root/miniconda3/bin  
  
RUN conda install -y pip  
RUN conda run pip install chainer==1.3.0  
RUN conda install -y scipy pillow scikit-learn  
  
ENTRYPOINT ["python"]  

