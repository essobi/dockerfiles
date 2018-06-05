FROM node:latest  
MAINTAINER Nossas <tech@nossas.org>  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends git  
  
WORKDIR /code  
COPY . .  
EXPOSE 5001  
CMD ["yarn", "start:prod"]  

