FROM ubuntu  
  
RUN apt-get update -y \  
&& apt-get install -y \  
git \  
python-pip \  
python-numpy \  
python-dev cmake \  
zlib1g-dev \  
libjpeg-dev \  
xvfb \  
libav-tools \  
xorg-dev \  
python-opengl \  
libboost-all-dev \  
libsdl2-dev \  
swig  
  
RUN cd /usr/src \  
&& git clone https://github.com/openai/gym.git \  
&& cd gym \  
&& pip install -e .  

