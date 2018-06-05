  
FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
cmake \  
git \  
python3 \  
vim \  
nano \  
python-dev \  
python-pip \  
python-pygraphviz \  
xml-twig-tools \  
wget \  
sed  
  
RUN pip3 install --upgrade pip  
RUN pip3 install
http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install torchvision numpy argparse tqdm  
  
RUN wget -O entrypoint.sh
https://gist.githubusercontent.com/Khakhulin/e022713896591f844090ce42e9637952/raw/2ebc277f18962a74475e59e0aa6c6a4d79367ca1/entrypoint.sh  
RUN chmod 777 entrypoint.sh  
  
RUN mkdir -p /path  
WORKDIR /path/  
  
# Install mosesdecoder  
RUN git clone https://github.com/moses-smt/mosesdecoder  
  
RUN wget -O nmt-model.tar.gz
'http://download1640.mediafire.com/20jjj7j1qcfg/jop13yp6kuq2bc1/nmt-
model.tar.gz'  
RUN chmod 777 nmt-model.tar.gz  
  
RUN tar -zxvf nmt-model.tar.gz  
  
WORKDIR ./nmt-babel/  
  
RUN wget -O translate2.sh
https://gist.githubusercontent.com/Khakhulin/8861e0d02a3ee5aeebdcfa1b0a9f990d/raw/7ec8de66ea5d4695e71fa5b1968010b6437d7c2d/translate.sh  
  
RUN chmod a+x translate2.sh  
  
RUN mkdir /data  
RUN mkdir /output  
  
CMD ["./translate2.sh"]

