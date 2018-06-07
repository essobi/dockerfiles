FROM ubuntu:trusty  
MAINTAINER Josh Benner <josh@bennerweb.com>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y
openssh-client rsync && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["rsync"]

