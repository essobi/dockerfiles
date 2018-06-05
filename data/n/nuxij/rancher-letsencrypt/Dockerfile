FROM golang  
  
WORKDIR /opt  
  
RUN apt install make  
  
RUN go version  
  
COPY ./ src/rancher-letsencrypt  
RUN chmod +x ./src/rancher-letsencrypt/scripts/*.sh && sync && \  
./src/rancher-letsencrypt/scripts/build.sh && \  
mv /opt/src/rancher-letsencrypt/build/rancher-letsencrypt-linux-amd64
/usr/bin/rancher-letsencrypt  
  
ENTRYPOINT ["/opt/src/rancher-letsencrypt/scripts/entrypoint.sh"]  
CMD ["/usr/bin/rancher-letsencrypt"]  
EXPOSE 80  

