FROM illallangi/ansible:latest as image  
ENV RADARR_VERSION 0.2.0.935  
ENV RADARR_SHA256
f6c2b4092fdba8789043824f21a33ff83b402a1011f2189e06195863dd70d1e0  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=radarr  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/radarr-entrypoint.sh"]  

