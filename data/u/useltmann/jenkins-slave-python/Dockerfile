FROM python:latest  
MAINTAINER seltmann@ub.uni-leipzig.de  
VOLUME [ "/home/dev", "/jenkins" ]  
EXPOSE 3000  
CMD ["/start.sh"]  
ADD slave.jar /  
ADD start.sh /  
RUN echo "deb http://ftp.debian.org/debian jessie-backports
main">/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -y -t jessie-backports openjdk-8-jre-headless \  
&& useradd dev \  
&& chmod a+x /start.sh \  
&& chmod 644 /slave.jar  

