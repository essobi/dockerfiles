FROM withinboredom/consul-agent  
  
MAINTAINER Robert Landers <landers.robert@gmail.com>  
  
RUN curl -sSLO
http://build.syncthing.net/job/discosrv/lastSuccessfulBuild/artifact/discosrv-
linux-amd64.tar.gz && \  
tar -xvf discosrv-linux-amd64.tar.gz && \  
cd discosrv-linux-amd64 && \  
mv discosrv /usr/local/bin/discosrv  
  
ADD root /  
  
EXPOSE 22026

