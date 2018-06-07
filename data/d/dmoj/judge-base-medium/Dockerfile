FROM dmoj/judge-base:latest  
  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
ruby xz-utils openjdk-8-jdk ca-certificates-java && \  
apt-get clean  

