FROM ubuntu:14.04  
# upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q && \  
apt-get install -y --no-install-recommends python-pip curl nginx-core && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN pip install envtpl  
  
# nginx  
ADD nginx.conf.tpl /etc/nginx/nginx.conf.tpl  
  
# kopf  
ENV KOPF_VERSION 1.5.5  
RUN curl -s -L "https://github.com/lmenezes/elasticsearch-
kopf/archive/v${KOPF_VERSION}.tar.gz" | \  
tar xz -C /tmp && \  
mv "/tmp/elasticsearch-kopf-${KOPF_VERSION}" /kopf && \  
rm -rf /tmp/*  
  
# run script  
ADD ./run.sh ./run.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# logs  
VOLUME ["/var/log/nginx"]  
VOLUME ["/var/cache/nginx"]  
  
# ports  
EXPOSE 80 443  
ENTRYPOINT ["/run.sh"]  

