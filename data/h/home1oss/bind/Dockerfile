  
FROM sameersbn/bind:9.9.5-20170626  
COPY docker/custom/etc/* /data/bind/etc/  
RUN chown -R bind:bind /data/bind/etc && chmod 775 /data/bind/etc/*  
  
COPY docker/bin/* /bin/  
RUN chown -R root:root /bin && chmod 755 /bin/*  
  
COPY docker/entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/named"]  

