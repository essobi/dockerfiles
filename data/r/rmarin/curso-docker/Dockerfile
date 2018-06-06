FROM library/debian:wheezy  
MAINTAINER r.marin@desigual.com  
RUN apt-get -y update && \  
apt-get -y install man && \  
apt-get -y install funny-manpages  
  
  
ENTRYPOINT ["/usr/bin/man"]  

