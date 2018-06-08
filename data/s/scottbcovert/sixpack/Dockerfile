FROM ubuntu:14.04  
MAINTAINER Naoki AINOYA <ainonic@gmail.com>  
MAINTAINER Scott Covert <scottbcovert@gmail.com>  
  
# setup Python, build tools and environment  
RUN apt-get update && apt-get dist-upgrade -y  
RUN apt-get install -y wget tar  
RUN apt-get install -y python-setuptools python-dev git build-essential  
RUN apt-get install -y libyaml-dev  
# PyYAML version must be kept up to date with requirement in  
# https://github.com/seatgeek/sixpack/blob/master/requirements.txt  
RUN easy_install pip pyyaml==3.10  
RUN echo 'root:sixpack' | chpasswd  
  
# setup redis  
ENV REDIS_RELEASE 2.8.9  
RUN mkdir -p /etc/redis  
RUN mkdir -p /var/log/redis  
RUN mkdir -p /var/lib/redis/6379  
RUN wget http://download.redis.io/releases/redis-$REDIS_RELEASE.tar.gz  
RUN tar -zxf redis-$REDIS_RELEASE.tar.gz  
RUN \  
cd redis-$REDIS_RELEASE && \  
make install && \  
cp utils/redis_init_script /etc/init.d/redis && \  
cd .. && \  
rm -rf redis-$REDIS_RELEASE  
  
ADD template/redis.conf /etc/redis/6379.conf  
  
# setup td-agent  
RUN apt-get install -y sudo  
RUN apt-get install -y curl tar  
ADD scripts/install-ubuntu.sh ./install-ubuntu.sh  
RUN sh ./install-ubuntu.sh  
RUN /opt/td-agent/embedded/bin/fluent-gem install fluent-plugin-sixpack  
  
ADD template/td-agent.conf /etc/td-agent/td-agent.conf  
  
# setup supervisord  
RUN pip install supervisor  
RUN mkdir -p /etc/supervisord.d/  
RUN mkdir -p /var/log/supervisor  
ADD template/supervisord.conf /etc/supervisord.conf  
ADD template/supervisord.d/sixpack-web.ini /etc/supervisord.d/sixpack-web.ini  
ADD template/supervisord.d/sixpack.ini /etc/supervisord.d/sixpack.ini  
  
# setup sixpack  
RUN mkdir -p /home/sixpack  
WORKDIR /home/sixpack  
RUN git clone https://github.com/seatgeek/sixpack  
  
WORKDIR /home/sixpack/sixpack  
RUN pip install -r requirements.txt  
  
ADD scripts/init_service.sh /home/sixpack/init_service.sh  
  
# start server  
EXPOSE 5000 5001 24224  
WORKDIR /home/sixpack  
CMD sh ./init_service.sh

