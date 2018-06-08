FROM ubuntu:trusty  
  
MAINTAINER Sandro Salles sandro@snippet.com.br  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y apt-transport-https  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9  
RUN sh -c "echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list"  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y openssh-server python-setuptools lxc-docker-1.5.0 &&
/usr/bin/easy_install supervisor  
  
ADD supervisord.conf /etc/supervisord.conf  
  
ENV DOCKER_GEN_VERSION 0.4.0  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY . /app/  
WORKDIR /app/  
  
ENV AUTHORIZED_KEYS **None**  
ENV DOCKER_HOST unix:///tmp/docker.sock  
  
RUN chmod +x /app/*.sh  
  
EXPOSE 22  
CMD ["/app/run.sh"]  

