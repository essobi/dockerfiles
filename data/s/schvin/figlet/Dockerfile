FROM debian:jessie  
MAINTAINER George Lewis <schvin@schvin.net>  
ENV REFRESHED_AT 2015-04-24  
# install  
RUN apt-get update -y && apt-get install -y figlet curl  
  
# extra fonts  
WORKDIR /tmp  
RUN curl -O ftp://ftp.figlet.org/pub/figlet/fonts/contributed.tar.gz  
RUN tar xfvz /tmp/contributed.tar.gz && cd contributed && cp -R *
/usr/share/figlet && chmod -R g+rX,o+rX /usr/share/figlet  
  
# drop privs  
RUN groupadd s-figlet  
RUN useradd s-figlet -g s-figlet -d /home/s-figlet  
RUN mkdir /home/s-figlet  
RUN chown -R s-figlet:s-figlet /home/s-figlet  
ENV HOME /home/s-figlet  
USER s-figlet  
WORKDIR /home/s-figlet  
  
# run  
ENTRYPOINT [ "/usr/bin/figlet" ]  

