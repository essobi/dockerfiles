FROM prom/busybox:latest  
MAINTAINER The Prometheus Authors <prometheus-developers@googlegroups.com>  
  
COPY cmd/amtool /bin/amtool  
COPY cmd/alertmanager /bin/alertmanager  
COPY doc/examples/simple.yml /etc/alertmanager/alertmanager.yml  
  
RUN chmod +x /bin/amtool  
RUN chmod +x /bin/alertmanager  
  
EXPOSE 9093  
VOLUME [ "/alertmanager" ]  
WORKDIR /etc/alertmanager  
ENTRYPOINT [ "/bin/alertmanager" ]  
CMD [ "--storage.path=/alertmanager","--
config.file=/etc/alertmanager/alertmanager.yml" ]  

