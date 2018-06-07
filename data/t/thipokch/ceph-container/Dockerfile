FROM ceph/daemon  
  
# For testing the  
# RUN export MON_IP=$(hostname -I) && echo "TEST: ${MON_IP}"  
COPY run.sh /  
RUN chmod +x /run.sh  
  
WORKDIR /  
ENTRYPOINT ["/run.sh"]

