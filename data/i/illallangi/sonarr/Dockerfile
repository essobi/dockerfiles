FROM illallangi/ansible:latest as image  
ENV SONARR_VERSION 2.0.0.5085  
ENV SONARR_SHA256
bf51182f581d81aa8aa9881aa42a60d938bfa0ff065b4edc04a585d9f56bcfd4  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=sonarr  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/sonarr-entrypoint.sh"]  

