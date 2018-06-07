FROM nginx  
# Get dashboard  
RUN apt-get update && apt-get install -y wget  
RUN apt-get install -y sed  
RUN wget https://github.com/lonelycode/tyk/releases/download/v1.8.3.2/tyk-
dashboard-amd64-v0.9.6.5.tar.gz  
RUN tar -xvzf tyk-dashboard-amd64-v0.9.6.5.tar.gz -C /opt  
RUN mv /opt/tyk-analytics-v0.9.6.5 /opt/tyk-dashboard  
  
# Set up link to hosts files  
RUN rm -rf /etc/nginx/conf.d  
RUN ln -s /opt/tyk-dashboard/host-manager/nginx_confs /etc/nginx/conf.d  
  
# Copy safe docker-enabled configuration and templates  
COPY _upstream.conf /opt/tyk-dashboard/host-manager/nginx_confs/  
COPY host_manager.json /opt/tyk-dashboard/host-manager/  
COPY entrypoint.sh /opt/tyk-dashboard/host-manager/  
RUN chmod +x /opt/tyk-dashboard/host-manager/entrypoint.sh  
COPY templates /opt/tyk-dashboard/host-manager/templates  
  
VOLUME ["/opt/tyk-dashboard/host-manager"]  
  
WORKDIR /opt/host-manager  
  
# Start the host manager  
CMD ["/opt/tyk-dashboard/host-manager/entrypoint.sh"]  

