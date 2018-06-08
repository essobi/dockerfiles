FROM ubuntu:14.04.2  
WORKDIR /  
COPY install.sh /  
RUN sh /install.sh  
RUN chmod +x /poi_fusion_engine3/ficontent2/docker/start.sh
/poi_fusion_engine3/ficontent2/docker/test.sh  
EXPOSE 8080  
CMD ["/poi_fusion_engine3/ficontent2/docker/start.sh"]  

