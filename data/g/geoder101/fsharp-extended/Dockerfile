FROM geoder101/fsharp  
MAINTAINER George Dernikos <geoder101@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -yq \  
git \  
make \  
uuid-runtime \  
curl \  
wget \  
build-essential  
  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -  
  
RUN apt-get update \  
&& apt-get install -yq \  
httpie \  
nodejs  
  
RUN apt-get clean  
  
RUN npm install -g bower  

