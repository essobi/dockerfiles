FROM illallangi/ansible:latest as image  
  
#COPY image/* /etc/ansible.d/image/  
#RUN /usr/local/bin/ansible-runner.sh image  
COPY container/* /etc/ansible.d/container/  
  
ENV HARDEN_PATH=/harden  
ENV USER=harden  
ENV UID=1024  
CMD ["/usr/local/bin/harden-entrypoint.sh"]  

