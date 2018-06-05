FROM google/cloud-sdk  
COPY entrypoint.sh /  
RUN mkdir /tmp/config/ && \  
chmod --recursive 0777 /tmp/config/  
ENV HOME=/tmp/config/  
VOLUME /service-account.json  
ENTRYPOINT ["/entrypoint.sh"]  

