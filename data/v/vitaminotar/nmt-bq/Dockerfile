  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
cmake \  
git \  
python \  
python3 \  
vim \  
nano \  
python-dev \  
python-pip \  
python-pygraphviz \  
xml-twig-tools \  
wget \  
sed  
  
RUN pip install --upgrade pip  
  
RUN mkdir -p /path  
WORKDIR /path/  
  
# Install mosesdecoder  
RUN git clone https://github.com/moses-smt/mosesdecoder  
  
RUN wget -O nmt-model.tar.gz
'http://download1640.mediafire.com/kjyvnnsn6k2g/jop13yp6kuq2bc1/nmt-
model.tar.gz'  
RUN chmod 777 nmt-model.tar.gz  
  
RUN tar -zxvf nmt-model.tar.gz  
  
WORKDIR ./nmt-babel/  
  
RUN wget -O translate2.sh
https://gist.githubusercontent.com/Khakhulin/8861e0d02a3ee5aeebdcfa1b0a9f990d/raw/461311fae139d871723e909a50bbbf32423f086e/translate.sh  
  
RUN chmod a+x translate2.sh  
  
RUN mkdir /data  
RUN mkdir /output  
  
CMD ["translate2.sh"]

