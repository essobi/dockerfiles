FROM siriuslabs/alpine:py3-dev  
  
ENV LIGHTNING_SOCKET_PATH /tmp/lightning-rpc  
  
RUN pip install lightning-rest  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8000  
VOLUME ["/home/lightning/.lightning"]  
  
CMD ["8000", "/tmp/lightning-rpc"]  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

