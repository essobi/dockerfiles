FROM ubuntu:trusty  
  
MAINTAINER sekia556 <sekia556 [at] yahoo.co.jp>  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget make gcc && \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN wget http://www.hping.org/visitors/visitors-0.7.tar.gz  
RUN tar xvzf visitors-0.7.tar.gz  
WORKDIR visitors_0.7  
  
RUN make  
RUN cp visitors /usr/bin/  
  
CMD ["visitors"]  
  

