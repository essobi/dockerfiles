FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
  
RUN apt-get -y update && \  
apt-get install -y --force-yes \  
python \  
python-dev \  
python-pip \  
python-all-dev \  
libblas-dev \  
liblapack-dev \  
gfortran \  
libjpeg8-dev \  
libfreetype6-dev \  
libxft-dev \  
libpng12-dev \  
libagg-dev \  
&& apt-get clean all && \  
pip install \  
ipython[all] \  
numpy \  
scipy \  
pandas \  
scikit-learn \  
matplotlib \  
nltk \  
pymystem3 \  
gensim \  
beautifulsoup4 \  
requests \  
&& python -m nltk.downloader -d /usr/share/nltk_data all  
  
RUN mkdir /data  
WORKDIR /data  
VOLUME ["/data"]  
  
EXPOSE 8888  
  
ENTRYPOINT ["sh", "-c", "ipython notebook --no-browser --ip='*'"]  

