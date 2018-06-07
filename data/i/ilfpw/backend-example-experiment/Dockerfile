FROM python:3.5  
RUN apt-get update && \  
apt-get install -y libyaml-dev libhunspell-dev libxml2-dev libxslt-dev python-
jinja2 netcat-openbsd && \  
pip3 install jinja2 && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/cache/* && rm -rf
/var/tmp/* && rm -rf /tmp/*  
  
WORKDIR /experiment  
# copy experiment files  
COPY requirements /experiment/requirements  
  
# install requirments  
RUN pip3 install -r requirements/base.txt && \  
pip3 install -r requirements/dev.txt  
  
COPY . /experiment  
  
# run experiment  
ENTRYPOINT ["./scripts/docker_entrypoint.sh"]  
  

