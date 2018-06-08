# Dockerfile for https://index.docker.io/u/koddsson/xo-docker/  
FROM koddsson/docker-debian-nodejs  
MAINTAINER Kristjan Oddsson, koddsson@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y \  
redis-server \  
ruby \  
git  
  
RUN gem install compass  
RUN git clone http://github.com/vatesfr/xo-server  
RUN git clone http://github.com/vatesfr/xo-web  
RUN cd xo-server && npm install  
  
ADD local.yaml /xo-server/config/local.yaml  
  
RUN cd xo-web && npm install  
RUN cd xo-web && ./gulp --production  
  
CMD /etc/init.d/redis-server start && /xo-server/xo-server  
  
EXPOSE 80  

