FROM java:openjdk-7-jre  
  
ENV HIBISCUS_VERSION 2.6.19  
ENV HIBISCUS_DOWNLOAD_SHA256 4d236cedb391bb69a5799c7bf9cb513f816eae57  
  
RUN curl -fsSL https://www.willuhn.de/products/hibiscus-
server/releases/hibiscus-server-$HIBISCUS_VERSION.zip -o hibiscus-server.zip  
RUN echo "$HIBISCUS_DOWNLOAD_SHA256 hibiscus-server.zip" | sha1sum -c -  
RUN unzip hibiscus-server.zip -d /  
RUN rm hibiscus-server.zip  
  
RUN echo "Europe/Berlin" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 8080  

