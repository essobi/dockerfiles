FROM tomcat:8.0  
COPY scripts /scripts  
  
RUN /scripts/setup.sh  
  
# geoserver  
COPY geoserver /build/geoserver  
RUN /build/geoserver/docker.sh  
  
# github-proxy  
COPY github-proxy /build/github-proxy  
RUN /build/github-proxy/docker.sh  
  
# webhooks  
COPY webhooks /build/webhooks  
RUN /build/webhooks/docker.sh  
  
# CONFIG webhooks  
COPY configs/webhooks.conf /etc/mapseries/webhooks.conf  
COPY configs/polygon.sld /data/geoserver/polygon.sld  
ENV ENABLE_JSONP true  
  
# view  
COPY view /build/view  
RUN /build/view/docker.sh  
  
# edit  
COPY edit /build/edit  
RUN /build/edit/docker.sh  
  
RUN rm -rf /scripts /build  

