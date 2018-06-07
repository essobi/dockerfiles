FROM illallangi/ansible:latest as image  
  
  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=deluge  
ENV DELUGE_COMPLETE_PATH=/data/complete  
ENV DELUGE_DOWNLOAD_PATH=/data/downloading  
ENV DELUGE_WATCH_PATH=/data/watch  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/deluge-entrypoint.sh"]  

