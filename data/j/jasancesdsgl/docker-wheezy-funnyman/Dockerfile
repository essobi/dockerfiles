FROM library/debian:wheezy  
MAINTAINER ja.sances@desigual.com  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get install -y man-db funny-manpages && \  
rm -rf /var/lib/apt/lists/*  
ENTRYPOINT ["/usr/bin/man"]

