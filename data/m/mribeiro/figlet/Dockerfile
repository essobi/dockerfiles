FROM debian:jessie  
MAINTAINER Marcio Ribeiro <binary@b1n.org>  
RUN apt-get -y update && apt-get -y install figlet lolcat  
ENV TERM ansi  
COPY run.sh /usr/bin/  
ENTRYPOINT ["run.sh"]  

