FROM debian:jessie  
  
MAINTAINER Michał Brzuchalski <m.brzuchalski@madkom.pl>  
  
RUN apt-get update -qq && \  
apt-get install -qq -y rinetd php5-cli --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
ADD entrypoint.sh entrypoint.sh  
ADD configure.php configure.php  
CMD ./entrypoint.sh  

