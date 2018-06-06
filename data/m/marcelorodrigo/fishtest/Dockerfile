FROM ubuntu:16.04  
MAINTAINER Marcelo Rodrigo <mrodrigow@gmail.com>  
  
ENV concurrency 1  
ENV username yourusername  
ENV password yourpassword  
WORKDIR /  
ADD https://github.com/glinscott/fishtest/archive/master.zip /  
RUN apt-get update && \  
apt-get install -y --no-install-recommends python build-essential libqtcore4
unzip && \  
unzip /master.zip -d / && \  
apt-get purge -y unzip && \  
rm -rf /master.zip && \  
rm -rf /var/lib/apt/lists/*  
CMD python /fishtest-master/worker/worker.py --concurrency $concurrency
$username $password  

