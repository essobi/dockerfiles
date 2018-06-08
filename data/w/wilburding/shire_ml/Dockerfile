FROM wilburding/shire_base  
  
ENV CRFPP_VERSION 0.59  
WORKDIR /usr/src  
RUN git clone https://github.com/taku910/crfpp.git \  
&& cd crfpp \  
&& sed -i '/winmain/d' crf_learn.cpp crf_test.cpp \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& ldconfig \  
&& cd python \  
&& python setup.py install \  
&& rm -rf /usr/src/crfpp  
  
WORKDIR /usr/src  
RUN git clone https://github.com/lzhang10/maxent.git \  
&& cd maxent \  
&& ./configure --prefix=/usr/local \  
&& make \  
&& make install \  
&& ldconfig \  
&& cd python \  
&& python setup.py install \  
&& rm -rf /usr/src/maxent  
  
WORKDIR /usr/src  
RUN apt-get update && apt-get install -y \  
libreoffice-common \  
libreoffice-writer \  
imagemagick \  
openjdk-7-jre-headless  
# libreoffice needs java  
RUN apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
WORKDIR /usr/src/app  

