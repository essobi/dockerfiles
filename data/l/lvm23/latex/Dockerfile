FROM debian:jessie  
MAINTAINER Mauro <mauro@sdf.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -yq texlive-full \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /docs  
WORKDIR /docs  
  

