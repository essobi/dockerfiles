FROM debian:8.7  
MAINTAINER Sergey Izgiyaev <sergo27@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
RECURSOR_VERSION=3.6.2-2+deb8u3  
  
RUN apt-get update && apt-get install -y curl host && \  
curl https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - && \  
echo "deb [arch=amd64] http://repo.powerdns.com/debian jessie-auth-40 main" >
/etc/apt/sources.list.d/pdns.list && \  
apt-get update && apt-get install -y pdns-recursor=${RECURSOR_VERSION} && \  
apt-get autoremove -y -qq && \  
apt-get clean -qq && \  
rm -rf /var/lib/apt/lists/*  
  
STOPSIGNAL SIGTERM  
  
COPY ./entrypoint.sh /bin/  
  
RUN chmod +x /bin/entrypoint.sh  
  
ENTRYPOINT ["entrypoint.sh"]

