FROM openjdk:8  
ENV GOCD_VERSION 17.8.0-5277  
ENV GOCD_DISTR go-server.deb  
  
# Install go.cd server  
RUN curl -fSL https://download.gocd.io/binaries/${GOCD_VERSION}/deb/go-
server_${GOCD_VERSION}_all.deb -o $GOCD_DISTR \  
&& dpkg -i $GOCD_DISTR \  
&& rm $GOCD_DISTR  
  
VOLUME /var/lib/go-server  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8153 8154  
CMD ["go-server"]  

