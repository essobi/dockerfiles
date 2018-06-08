FROM openjdk:8-jre  
ARG url=http://jminim.com/brac/MinimServer-0.8.4-linux-x64.tar.gz  
RUN wget -O /opt/minimserver.tar.gz ${url} && \  
cd /opt && \  
tar -xzf minimserver.tar.gz && \  
rm minimserver.tar.gz  
EXPOSE 9790 9701  
VOLUME /mnt/Musik /opt/minimserver/data  
ENTRYPOINT [ "/opt/minimserver/bin/startc" ]  

