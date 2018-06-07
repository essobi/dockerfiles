FROM python:3.6-slim-stretch  
  
COPY requirements.txt /tmp/requirements.txt  
RUN apt-get -qq update \  
&& apt-get install -y --no-install-recommends \  
gcc g++ build-essential \  
libsqlite3-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& cat /tmp/requirements.txt | xargs -n1 -t pip install -U \  
&& python -m nltk.downloader punkt wordnet averaged_perceptron_tagger  

