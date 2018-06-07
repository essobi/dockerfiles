FROM python:2.7-slim  
  
RUN groupadd -r limn && useradd -r -g limn limn  
  
ADD requirements.txt /tmp/  
  
RUN buildDeps=' \  
build-essential \  
libssl-dev \  
python-dev \  
' \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install -U pip \  
&& pip install -r /tmp/requirements.txt \  
&& rm /tmp/requirements.txt \  
&& apt-get purge -y --auto-remove \  
-o APT::AutoRemove::RecommendsImportant=false \  
-o APT::AutoRemove::SuggestsImportant=false \  
$buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
USER limn  
  
ADD . /app  
WORKDIR /app  
  
EXPOSE 8080  
CMD ["python", "limn.py"]  

