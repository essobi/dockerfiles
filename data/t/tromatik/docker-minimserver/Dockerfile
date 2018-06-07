FROM java:8-jre  
  
ARG url=http://jminim.com/cada/MinimServer-0.8.4-linux-x64.tar.gz  
  
RUN wget -O /opt/MinimServer.tar.gz ${url} && \  
cd /opt && \  
tar xf MinimServer.tar.gz && \  
rm MinimServer.tar.gz  
  
COPY ./minimserver.config /opt/minimserver/data/minimserver.config  
  
EXPOSE 9790 9791  
ENTRYPOINT [ "/opt/minimserver/bin/startc" ]  

