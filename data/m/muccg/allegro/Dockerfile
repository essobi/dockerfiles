#  
FROM muccg/base:ubuntu14.04  
MAINTAINER ccg <ccgdevops@googlegroups.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Project specific deps  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
wget \  
supervisor \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN env --unset=DEBIAN_FRONTEND  
  
WORKDIR /tmp  
RUN \  
wget
http://franz.com/ftp/pri/acl/ag/ag4.14.1/linuxamd64.64/agraph-4.14.1-linuxamd64.64.tar.gz
\  
&& tar zxvf agraph-4.14.1-linuxamd64.64.tar.gz \  
&& cd agraph-4.14.1 \  
&& ./install-agraph /app/allegrograph --non-interactive --runas-user ccg-user
--super-password ignored \  
&& mkdir /app/allegrograph/etc \  
&& chown -R ccg-user:ccg-user /app \  
&& rm -rf /tmp/*  
  
COPY agraph.cfg /app/allegrograph/etc/agraph.cfg  
EXPOSE 10035  
VOLUME ["/app", "/data"]  
  
# Drop privileges, set home for ccg-user  
USER ccg-user  
ENV HOME /data  
WORKDIR /data  
  
CMD /app/allegrograph/bin/agraph-control --config
/app/allegrograph/etc/agraph.cfg start \  
&& tail -f /data/log/agraph.log  

