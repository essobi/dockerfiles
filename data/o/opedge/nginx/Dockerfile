FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
  
ADD https://releases.hashicorp.com/consul-template/0.14.0/consul-
template_0.14.0_linux_amd64.zip /tmp/consul-template.zip  
COPY supervisord.conf /supervisord.conf  
COPY error503.html /usr/share/nginx/html/error503.html  
  
RUN apt-get -y update && \  
apt-get install -y nginx python-pip unzip && \  
pip install supervisor && \  
cd /tmp && \  
unzip consul-template.zip && \  
mv consul-template /bin/ && \  
rm -rf consul-template.zip && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
mkdir -p /data/cache && \  
mkdir -p /data/static && \  
mkdir -p /certs && \  
mkdir -p /templates  
  
VOLUME ["/data/static", "/data/cache", "/templates", "/certs"]  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["supervisord"]  
CMD ["-c", "supervisord.conf"]  

