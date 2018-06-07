FROM redis:3.0  
COPY entrypoint.sh /entrypoint.sh  
RUN echo 'echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled' >>
/etc/rc.local \  
&& chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

