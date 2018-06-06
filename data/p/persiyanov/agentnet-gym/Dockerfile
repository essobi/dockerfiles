FROM continuumio/anaconda  
  
MAINTAINER Dmitry Persiyanov <dmitry.persiyanov@gmail.com>  
  
RUN sed -i "s/httpredir.debian.org/`curl -s -D -
http://httpredir.debian.org/demo/debian/ | awk '/^Link:/ { print $2 }' | sed
-e 's@<http://\\(.*\\)/debian/>;@\1@g'`/" /etc/apt/sources.list  
  
# Install build-essential, cmake and other dependencies  
RUN apt-get clean && apt-get update && apt-get install -y \  
build-essential \  
cmake \  
libopenblas-dev \  
zlib1g-dev \  
libjpeg-dev \  
libboost-all-dev \  
libsdl2-dev  
  
RUN apt-get install -y \  
xvfb libav-tools xorg-dev python-opengl swig  
  
RUN pip install --upgrade pip  
  
# Install bleeding-edge Theano  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
  
RUN pip install --upgrade
https://github.com/Lasagne/Lasagne/archive/master.zip  
  
# Install AgentNet  
RUN git clone https://github.com/yandexdataschool/AgentNet.git ~/AgentNet \  
&& cd ~/AgentNet \  
&& pip install -r requirements.txt \  
&& pip install -e .  
  
# Install OpenAI Gym  
RUN git clone https://github.com/openai/gym ~/gym \  
&& cd ~/gym \  
&& pip install -e .[all]  
RUN pip install --upgrade gym  
  
# Some fancy packages  
RUN pip install tqdm seaborn  
  
WORKDIR /root  

