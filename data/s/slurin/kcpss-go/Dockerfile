FROM busybox:latest  
COPY kcptund ss-server /bin/  
COPY start.sh /start.sh  
RUN chmod +x /start.sh & chmod +x /bin/kcptund & chmod +x /bin/ss-server  
ENTRYPOINT ["/start.sh"]  
EXPOSE 12948 29900/udp

