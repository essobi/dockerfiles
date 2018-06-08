FROM debian:latest  
  
RUN apt-get update \  
&& apt-get install \--yes \  
curl \  
build-essential \  
clang-3.8 \  
cmake \  
git  
  
RUN curl \--silent \--location \  
https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py \  
&& python /tmp/get-pip.py  
RUN pip install \  
conan \  
pipenv  
  
RUN ln -s /usr/bin/clang-3.8 /usr/local/bin/clang \  
&& ln -s /usr/bin/clang++-3.8 /usr/local/bin/clang++  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /var/tmp/*  

