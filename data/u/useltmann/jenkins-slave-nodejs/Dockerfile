FROM node:latest  
MAINTAINER seltmann@ub.uni-leipzig.de  
VOLUME [ "/home/node", "/jenkins" ]  
CMD ["/start.sh"]  
ADD start.sh slave.jar /  
RUN echo "deb http://ftp.debian.org/debian jessie-backports
main">/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -y -t jessie-backports openjdk-8-jre-headless \  
&& chmod a+x /start.sh \  
&& chmod 644 /slave.jar  

