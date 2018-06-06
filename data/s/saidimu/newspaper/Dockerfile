FROM python:3.5.1-alpine  
  
MAINTAINER Srinath Sankar <srinath@iambot.net>  
  
RUN apk add --no-cache \  
build-base \  
gcc \  
bash \  
python-dev \  
libxml2-dev \  
libxslt-dev \  
libjpeg-turbo-dev \  
zlib \  
zlib-dev \  
libpng-dev \  
jpeg-dev \  
ca-certificates  
  
# https://github.com/python-pillow/Pillow/issues/1763  
ENV LIBRARY_PATH=/lib:/usr/lib  
  
RUN pip install newspaper3k  
  
# Download corpora  
RUN python -m nltk.downloader brown punkt maxent_treebank_pos_tagger
movie_reviews wordnet stopwords averaged_perceptron_tagger  

