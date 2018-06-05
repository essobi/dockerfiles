FROM illallangi/ansible:latest as image  
ENV BEETS_VERSION 1.4.6  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=beets  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/beets-entrypoint.sh"]  

