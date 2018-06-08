FROM ubuntu:15.10  
MAINTAINER takeshi.hirosue@bigtreetc.com  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 \  
&& add-apt-repository "deb http://dl.hhvm.com/ubuntu $(lsb_release -sc) main"  
RUN apt-get update \  
&& apt-get install -y hhvm  
  
ADD scripts/ /scripts/  
ADD .hhconfig /app/  
RUN chmod 755 /scripts/*.sh \  
&& chmod 755 /app/  
  
EXPOSE 9000  
CMD ["/scripts/start.sh"]  

