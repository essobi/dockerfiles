FROM busybox  
ADD docker-entrypoint.sh /  
HEALTHCHECK CMD cat /healthy  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

