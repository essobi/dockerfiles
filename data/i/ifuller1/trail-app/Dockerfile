# docker build -t trail-app .  
# docker run --name trail-app -v /Users/abs-path-to/trail-app:/data/trail-app-
src -v /tmp/bundler-cache:/data/bundle-cache -p 3000:3000 -it --rm=true trail-
app  
FROM ubuntu:14.04  
# prefer bash over sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# suppress 'no ui' errors  
ENV DEBIAN_FRONTEND noninteractive  
  
# stop auto start services  
RUN echo exit 101 > /usr/sbin/policy-rc.d  
RUN chmod +x /usr/sbin/policy-rc.d  
  
# packages  
RUN apt-get update  
RUN apt-get -y install wget git  
RUN apt-get -y install postgresql postgresql-contrib #3  
RUN apt-get -y install libpq-dev # for postgres lib build  
RUN apt-get -y install redis-server  
RUN apt-get -y install curl  
RUN apt-get -y install nodejs  
RUN apt-get -y install tmux  
  
# RVM setup  
RUN gpg --keyserver hkp://pgp.mit.edu --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable #2  
  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install 2.1.3"  
  
# Setup environment variables for the mongo connection  
ENV MONGO_DB_SERVER $MONGO_PORT_27017_TCP_ADDR  
ENV PATH /usr/local/bin/:/usr/lib/postgresql/9.3/bin/:$PATH  
  
EXPOSE 6379  
EXPOSE 3000  
WORKDIR /data/trail-app-src  
VOLUME /data/trail-app-src  
VOLUME /data/bundle-cache  
CMD ./docker/init.sh  
  

