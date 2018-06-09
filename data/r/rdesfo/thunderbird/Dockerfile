FROM ubuntu:14.04  
LABEL maintainer "Ryan Desfosses <ryan@desfo.org>"  
  
RUN apt-get update \  
&& apt-get install -y \  
gnupg2 \  
thunderbird \  
libcanberra-gtk-module \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -g 1000 user \  
&& useradd \--create-home -d /home/user -g user -u 1000 user  
USER user  
ENV HOME /home/user  
ENTRYPOINT [ "thunderbird" ]  

