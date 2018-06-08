# grynn/speedtest https://github.com/Grynn/docker-speedtest  
# VERSION 0.0.1  
FROM debian:jessie  
MAINTAINER Vishal Doshi (vishal.doshi@gmail.com)  
  
# Don't want to pollute the env with DEBIAN_FRONTEND  
RUN apt-get update && apt-get install -y apache2 php5 git  
RUN rm -rf /var/www/html  
ADD app /var/www/html  
ADD run.sh /run.sh  
EXPOSE 80  
CMD /run.sh  

