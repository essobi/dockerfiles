FROM python:2.7  
EXPOSE 8888  
VOLUME ["/srv/thumbor/storage"]  
  
RUN apt-get update  
RUN apt-get install --no-install-recommends -y libgraphicsmagick++-dev
libboost-python-dev  
RUN pip install graphicsmagick-engine thumbor boto tc_aws envtpl  
COPY thumbor.conf.tpl /etc/thumbor.conf.tpl  
COPY start /start  
  
ENTRYPOINT ["/start"]  

