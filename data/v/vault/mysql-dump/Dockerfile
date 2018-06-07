FROM ubuntu:xenial  
MAINTAINER Christoph Dwertmann <christoph.dwertmann@vaultsystems.com.au>  
RUN apt-get update && apt-get install -y mysql-client python-swiftclient --no-
install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*  
ADD *.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

