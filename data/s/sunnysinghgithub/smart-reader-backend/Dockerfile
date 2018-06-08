FROM python:2.7  
RUN pip install -U nltk  
  
RUN pip install Flask  
  
RUN apt-get update && \  
apt-get install -y libzmq-dev && \  
apt-get install -y libevent-dev  
  
RUN pip install pyzmq && \  
pip install zerorpc  
  
ENV CORPORA brown  
  
RUN python -m nltk.downloader $CORPORA  
  
RUN python -m nltk.downloader punkt  
  
RUN python -m nltk.downloader maxent_treebank_pos_tagger  
  
RUN pip install -U numpy  
  
RUN python -m nltk.downloader stopwords  
  
RUN pip install beautifulsoup4  
  
RUN pip install requests  

