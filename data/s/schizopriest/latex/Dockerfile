FROM debian:jessie  
MAINTAINER Pascal Reeb <pascal at reeb dot io>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN printf "deb http://ftp.de.debian.org/debian jessie main\ndeb-src
http://ftp.de.debian.org/debian jessie main\n\ndeb
http://ftp.de.debian.org/debian/ jessie-updates main\ndeb-src
http://ftp.de.debian.org/debian/ jessie-updates main\n\ndeb
http://security.debian.org/ jessie/updates main\ndeb-src
http://security.debian.org/ jessie/updates main\n\ndeb
http://ftp.de.debian.org/debian/ sid main\ndeb-src
http://ftp.de.debian.org/debian/ sid main" > /etc/apt/sources.list  
RUN apt-get update -q  
RUN apt-get install -qy make  
RUN apt-get install -qy texlive-full  
RUN apt-get install -qy biber  

