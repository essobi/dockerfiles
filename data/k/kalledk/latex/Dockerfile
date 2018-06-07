FROM debian:jessie  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN \  
apt-get update --quiet --yes \  
&& apt-get install --quiet --yes \  
texlive-full \  
biber \  
latexmk \  
make  

