FROM ubuntu:latest  
  
MAINTAINER geert.van.bastelaere@gmail.com  
  
RUN \  
apt-get update && \  
apt-get install -y apt-transport-https && \  
echo deb https://get.docker.com/ubuntu docker main >
/etc/apt/sources.list.d/docker.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
apt-get update && \  
apt-get install -y curl lxc-docker && \  
apt-get autoremove -y -q && \  
apt-get clean -y -q  
  
RUN \  
curl -L https://github.com/docker/fig/releases/download/1.0.0/fig-`uname
-s`-`uname -m` > /usr/local/bin/fig && \  
chmod +x /usr/local/bin/fig  
  
WORKDIR /app  
  
VOLUME ["/app"]  
  
ENTRYPOINT ["/usr/local/bin/fig"]  
  
CMD ["--version"]  

