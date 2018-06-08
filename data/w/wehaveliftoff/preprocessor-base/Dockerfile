FROM python:2-alpine  
MAINTAINER Lukas Batteau "lukas@lift.cards"  
RUN apk update && apk upgrade  
RUN apk add \--no-cache curl gcc g++ libffi libffi-dev openssl openssl-dev
gfortran bash git openssh docker  
RUN apk add \--no-cache \--repository=http://dl-
cdn.alpinelinux.org/alpine/edge/community lapack-dev  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN pip install Cython==0.27.3 numpy==1.14.0; \  
pip install scipy==1.0.0; \  
pip install nltk==3.2.5 scikit-learn==0.19.1 gensim==3.2.0 pandas==0.20.1  
  
# Download NLTK required corpora  
RUN python -m nltk.downloader stopwords  
RUN python -m nltk.downloader punkt

