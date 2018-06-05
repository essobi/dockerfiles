FROM nginx:mainline-alpine  
  
ENV CONSUL_TEMPLATE_VERSION 0.19.4  
RUN apk add --no-cache wget ca-certificates supervisor coreutils curl  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS /opt/  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /opt/  
  
RUN cd /opt && \  
sha256sum -c consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS 2>&1 | grep
OK && \  
unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
ln -s /opt/consul-template /bin/consul-template && \  
rm -f /opt/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
apk --update add curl bash  
  
COPY app /app/  
COPY nginx_common.conf /etc/nginx/conf.d/default.conf  
#COPY nginx.conf /etc/nginx/nginx.conf  
ENTRYPOINT ["/app/docker-entrypoint.sh"]  
CMD ["supervisord", "-c", "/app/supervisord.conf"]  
  

