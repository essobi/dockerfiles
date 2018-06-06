FROM python:2-slim  
  
RUN pip install sphinx sphinxcontrib-phpdomain  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends make \  
&& rm -rf /var/lib/apt/lists/* ~/.cache  
  
WORKDIR /var/docs  

