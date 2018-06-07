FROM illallangi/ansible:latest as image  
  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/bin/rtorrent"]  
  
USER rtorrent  
WORKDIR /var/lib/rtorrent  
  
ENV RTORRENT_COMPLETE_PATH=/complete  
ENV RTORRENT_DOWNLOAD_PATH=/downloading  
ENV RTORRENT_WATCH_PATH=/watch  
ENV TERM=xterm  

