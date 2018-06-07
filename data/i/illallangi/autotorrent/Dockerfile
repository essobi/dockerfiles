FROM illallangi/ansible:latest as image  
  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
COPY container/* /etc/ansible.d/container/  
  
ENV AUTOTORRENT_COMPLETE_PATH=/complete  
ENV AUTOTORRENT_CONFIG_PATH=/var/lib/autotorrent/.config/autotorrent  
ENV AUTOTORRENT_DISK_PATH=/disk  
ENV AUTOTORRENT_MATCH_PATH=/match  
ENV AUTOTORRENT_ADD_LIMIT_SIZE=64000000  
ENV AUTOTORRENT_ADD_LIMIT_PERCENT=1  
ENV AUTOTORRENT_LINK_TYPE=soft  
ENV AUTOTORRENT_SCAN_MODE=unsplitable,normal  
  
ENV USER=autotorrent  
ENV UID=1024  
CMD ["/usr/local/bin/autotorrent-entrypoint.sh"]  

