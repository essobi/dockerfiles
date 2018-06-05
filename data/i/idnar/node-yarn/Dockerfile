FROM node:latest  
MAINTAINER Tristan Seligmann <mithrandi@mithrandi.net>  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qy apt-
transport-https && rm -rf /var/lib/apt/lists/*  
COPY yarn.gpg /etc/apt/trusted.gpg.d/yarn.gpg  
COPY yarn.list /etc/apt/sources.list.d/yarn.list  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install --no-
install-recommends -qy yarn && rm -rf /var/lib/apt/lists/*  

