FROM debian:8.0  
MAINTAINER andystanton  
ENV LANG C.UTF-8  
RUN printf "\n%s" "deb http://ftp.nl.debian.org/debian/ wheezy main contrib
non-free" >> /etc/apt/sources.list && \  
apt-get update -y -qq && \  
apt-get install -y patch clisp && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["/tmp/dexec/image-common/dexec-script.sh", "clisp"]  

