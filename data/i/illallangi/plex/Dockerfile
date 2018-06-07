FROM illallangi/ansible:latest  
ENV PLEX_VERSION=1.11.2.4772-3e88ad3ba  
ENV
PLEX_SHA256=a46b4bf190ea9548970614a55d3add8929235a1c4db20c37105d0ceaf2d88930  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
ENV UID=1024  
ENV USER=plex  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/plex-entrypoint.sh"]  

