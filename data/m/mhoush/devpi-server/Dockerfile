FROM mhoush/py3  
MAINTAINER https://github.com/m-housh  
  
ARG DEVPI_VERSION=4.0.0  
ENV DEVPI_VERSION $DEVPI_VERSION  
  
RUN pip install --no-cache-dir --upgrade --ignore-installed \  
"devpi-server==$DEVPI_VERSION" &&\  
rm -rf /root/.cache  
  
COPY entrypoint.sh /  
  
VOLUME /data  
  
WORKDIR /data  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["devpi"]  

