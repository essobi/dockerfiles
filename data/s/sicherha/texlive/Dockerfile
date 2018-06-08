FROM ubuntu:17.10  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get install -y dia git inkscape libreoffice make python-pygments
texlive-full \  
&& apt-get purge -y '.*-doc$' \  
&& apt-get clean -y  

