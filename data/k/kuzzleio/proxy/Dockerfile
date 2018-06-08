FROM kuzzleio/base  
MAINTAINER Kuzzle <support@kuzzle.io>  
  
COPY ./ /var/app/  
COPY ./docker-compose/scripts/run.sh /run.sh  
COPY ./docker-compose/scripts/install-plugins.sh /var/app/install-plugins.sh  
  
WORKDIR /var/app  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
g++ \  
python \  
&& npm install --unsafe \  
&& ./install-plugins.sh \  
&& apt-get clean \  
&& apt-get remove -y \  
build-essential \  
g++ \  
python \  
&& apt-get autoremove -y \  
&& chmod 755 /run.sh \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/run.sh"]  

