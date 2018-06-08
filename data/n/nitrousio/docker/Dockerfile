FROM nitrousio/golang:latest  
MAINTAINER Nitrous.IO <hello@nitrous.io>  
  
RUN \  
apt-get update && \  
apt-get install -yq apt-transport-https  
  
RUN \  
touch /etc/init.d/cgroup-lite && \  
touch /etc/init.d/cgmanager && \  
touch /etc/init.d/cgproxy && \  
touch /etc/init.d/lxc && \  
touch /etc/init.d/lxc-net && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
echo deb https://get.docker.io/ubuntu docker main >
/etc/apt/sources.list.d/docker.list && \  
apt-get update && \  
apt-get install -y lxc-docker-1.4.1 && \  
apt-get install -y --no-install-recommends lxc=1.0.* cgmanager libcgmanager0
&& \  
rm /etc/init.d/cgroup-lite && \  
rm /etc/init.d/cgmanager && \  
rm /etc/init.d/cgproxy && \  
rm /etc/init.d/lxc && \  
rm /etc/init.d/lxc-net && \  
apt-get clean  
  
ADD files/dind /nitrous/dind  
ADD files/emit-net-device-event.conf /etc/init/emit-net-device-event.conf  
RUN chmod +x /nitrous/dind && chmod 644 /etc/init/emit-net-device-event.conf  
RUN /bin/bash -c 'adduser $NITROUS_USERNAME docker'  
  
ENV NITROUS_REQUIRES_PRIVILEGED true  
  
VOLUME /var/lib/docker  
  
CMD ["/nitrous/dind", "/sbin/init", "--default-console", "none"]  

