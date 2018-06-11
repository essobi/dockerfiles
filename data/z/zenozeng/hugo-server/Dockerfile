FROM debian:sid  
RUN sed -i "s/httpredir.debian.org/ftp.cn.debian.org/" /etc/apt/sources.list  
RUN apt-get update && apt-get \--yes install hugo  
WORKDIR /srv/blog  
CMD ls -l && hugo server \--verbose --bind 0.0.0.0 --port 80  

