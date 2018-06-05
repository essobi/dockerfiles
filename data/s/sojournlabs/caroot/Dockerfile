# Root certificate authority container.  
# Creates certificates of different types and signs files.  
# Use wrapper scripts from https://github.com/SojournLabs/vapr.  
FROM debian  
MAINTAINER jonathan lung <vapr@sojournlabs.com>  
RUN apt-get update  
RUN apt-get install -y \  
openssl  
WORKDIR /etc/ssl  
ADD openssl.cnf openssl.cnf  
ENV PATH /vapr:$PATH  
ADD ca /bin/ca  
WORKDIR /vapr  
ENTRYPOINT ["/bin/ca"]

