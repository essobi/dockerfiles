FROM homeassistant/home-assistant:latest  
MAINTAINER Rolf Larsen  
  
RUN apt-get update \  
&& apt-get install -y git \  
&& cd /tmp && git clone https://github.com/tobiasgraf/open-zwave.git && cd
open-zwave && git checkout c610dfb4fb1ec4467fea6f00430febeb8fd5be17 \  
&& make && make install \  
&& ln -s /usr/local/lib64/libopenzwave.so /usr/lib/ \  
&& ln -s /usr/local/lib64/libopenzwave.so.1.4 /usr/lib/ \  
&& pip3 install --upgrade rflink \  
&& pip3 install --no-cache-dir python_openzwave==0.4.3 \--upgrade --no-deps
--force-reinstall --install-option="--flavor=shared"  

