FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y \  
python \  
python-pip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install \  
biopython==1.69  
  
RUN mkdir -p /astralroc  
COPY ./ /astralroc/  
  
ENV PYTHONPATH=$PYTHONPATH:/astralroc  
WORKDIR /astralroc/src/

