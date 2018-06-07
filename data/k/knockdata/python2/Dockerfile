FROM debian:stretch  
  
ENV LANG C.UTF-8  
ENV LC_ALL C.UTF-8  
RUN apt-get update \  
&& apt-get install -y bzip2 build-essential curl gcc g++ git grep net-tools
locales sed tar unzip vim wget  
  
RUN echo "LC_ALL=\"en_US.UTF-8\"" >> /etc/default/locale  
  
ENV ANACONDA_VERSION 5.0.0.1  
RUN curl -o ~/anaconda2.sh
https://repo.continuum.io/archive/Anaconda2-${ANACONDA_VERSION}-Linux-x86_64.sh  
  
RUN /bin/bash ~/anaconda2.sh -b -p /opt/conda2 \  
&& rm ~/anaconda2.sh  
  
ENV PATH /opt/conda2/bin:$PATH  
  
RUN conda install -y tensorflow spacy gensim  
  
RUN apt-get clean autoclean \  
&& apt-get autoremove -y --force-yes \  
&& rm -rf /tmp/* \  
&& rm -rf ~/.m2 ~/.npm ~/.cache \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
## The default sh has some issue e.g. with source  
## so explicityly change it to bash as the default  
##  
RUN ls -al /bin/sh \  
&& rm /bin/sh \  
&& ln -sf /bin/bash /bin/sh  
  
CMD ["jupyter", "notebook"]  

