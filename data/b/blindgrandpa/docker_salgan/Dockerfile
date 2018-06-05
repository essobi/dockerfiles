FROM blindgrandpa/theano_cudnn5.1  
RUN apt-get update && apt-get install -y \  
libjpeg-dev \  
zlib1g-dev \  
libglib2.0-0  
  
RUN pip install -U setuptools  
  
COPY . /opt/app  
  
RUN pip install -r /opt/app/requirements.txt  
  
RUN pip install --upgrade
https://github.com/Lasagne/Lasagne/archive/master.zip

