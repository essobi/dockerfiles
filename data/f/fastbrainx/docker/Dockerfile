FROM docker:latest  
RUN mkdir -p /etc/docker/certs.d/registry.bestplayers.ru  
COPY ca.crt /etc/docker/certs.d/registry.bestplayers.ru/ca.crt  
VOLUME /var/lib/docker  
EXPOSE 2375

