FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
git-core \  
python-dev \  
python-pip \  
python-virtualenv \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/oisinmulvihill/nozama-cloudsearch.git \  
&& pip install pymongo==2.7.2 \  
&& pip install -e nozama-cloudsearch/nozama-cloudsearch-data \  
&& pip install -e nozama-cloudsearch/nozama-cloudsearch-client \  
&& pip install -e nozama-cloudsearch/nozama-cloudsearch-service  
  
ADD development.ini development.ini  
  
EXPOSE 15808  
CMD ["pserve", "development.ini"]  
  

