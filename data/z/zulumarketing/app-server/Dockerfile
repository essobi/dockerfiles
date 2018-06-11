# Generic Web Application Container  
FROM ubuntu:14.04  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ADD
https://github.com/coreos/etcd/releases/download/v2.0.12/etcd-v2.0.12-linux-
amd64.tar.gz /tmp/etcd.tar.gz  
RUN apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get install -y git nginx python-pip apt-transport-https > /dev/null \  
&& apt-get clean > /dev/null \  
&& pip install "supervisor==3.1.3" > /dev/null \  
&& cd /tmp \  
&& tar xzf etcd.tar.gz \  
&& mv /tmp/etcd-v2.0.12-linux-amd64/etcd /usr/bin/etcd \  
&& mv /tmp/etcd-v2.0.12-linux-amd64/etcdctl /usr/bin/etcdctl \  
&& rm -r /tmp/etcd-v2.0.12-linux-amd64 /tmp/etcd.tar.gz  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY security.conf /etc/nginx/conf.d/security.conf  
COPY cloudflare.conf /etc/nginx/conf.d/cloudflare.conf  
COPY bin/ /usr/bin/  
COPY supervisord.conf /etc/supervisord.conf  
COPY supervisor /etc/supervisor  
  
RUN passwd -u www-data \  
&& adduser --system --no-create-home --disabled-login etcd > /dev/null \  
&& mkdir -p /var/lib/etcd /var/log/supervisor \  
&& chown -R etcd /var/lib/etcd \  
&& ln -s /etc/supervisord.conf /etc/supervisor/supervisord.conf  
  
EXPOSE 8080 2379 2380  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]  

