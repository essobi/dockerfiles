FROM ubuntu:16.04  
LABEL Louis Paret <perso@louisparet.fr>  
  
## Install packages  
RUN apt-get update \  
&& apt-get -y install \  
software-properties-common \  
&& add-apt-repository ppa:certbot/certbot \  
&& apt-get update \  
&& apt-get install -y certbot \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
## Open ports  
EXPOSE 80 443  
CMD ["sleep", "infinity"]

