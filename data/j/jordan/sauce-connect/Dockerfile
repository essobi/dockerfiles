# Dockerfile for sauce-connect  
# https://github.com/jjethwa/sauce-connect  
FROM java:8-jre  
  
MAINTAINER Jordan Jethwa  
  
ENV SAUCE_VERSION 4.4.12  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /usr/local/sauce-connect  
  
RUN apt-get update -qqy \  
&& apt-get install -qqy wget \  
&& apt-get clean  
  
RUN wget https://saucelabs.com/downloads/sc-$SAUCE_VERSION-linux.tar.gz -O - |
tar -xz --strip 1  
  
WORKDIR /usr/local/sauce-connect  
  
ENTRYPOINT ["/usr/local/sauce-connect/bin/sc"]  
  
CMD ["--version"]  

