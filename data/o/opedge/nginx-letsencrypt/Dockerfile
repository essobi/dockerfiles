FROM ubuntu:14.04  
MAINTAINER Oleg Poyaganov <oleg@poyaganov.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD https://releases.hashicorp.com/consul-template/0.14.0/consul-
template_0.14.0_linux_amd64.zip /tmp/consul-template.zip  
COPY supervisord.conf /supervisord.conf  
COPY error503.html /usr/share/nginx/html/error503.html  
  
RUN apt-get -y update && \  
apt-get install -y nginx python-pip unzip git cron && \  
pip install supervisor && \  
cd /tmp && \  
unzip consul-template.zip && \  
mv consul-template /bin/ && \  
rm -rf consul-template.zip && \  
git clone \--depth 1 https://github.com/letsencrypt/letsencrypt
/opt/letsencrypt && \  
/opt/letsencrypt/letsencrypt-auto -h > /dev/null && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/ && \  
mkdir -p /data/cache && \  
mkdir -p /data/static && \  
mkdir -p /templates && \  
mkdir -p /webroot  
  
RUN (crontab -l 2>/dev/null; echo "30 2 * * 1 /opt/letsencrypt/letsencrypt-
auto renew --webroot -w /webroot && nginx -s reload") | crontab -  
  
VOLUME ["/data/static", "/data/cache", "/templates", "/etc/letsencrypt",
"/var/lib/letsencrypt"]  
  
EXPOSE 80  
EXPOSE 443  
ENV CONSUL_ADDRESS consul:8500  
ENV LETSENCRYPT_ENTRYPOINT_ARGS certonly --non-interactive --agree-tos --text
--email admin@example.com --standalone --standalone-supported-challenges
http-01 \--http-01-port 80 -d example.com -d www.example.com  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["supervisord", "-c", "supervisord.conf"]  

