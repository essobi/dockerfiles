FROM ubuntu:17.10  
  
RUN apt-get update \  
&& apt-get install -y git inkscape make texlive-full \  
&& apt-get purge -y '.*-doc$' \  
&& apt-get clean -y  

