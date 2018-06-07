FROM pstehlik/sdkman:latest  
MAINTAINER Philip Stehlik "p@pstehlik.com"  
# open up some web development ports  
EXPOSE 8080  
EXPOSE 8081  
EXPOSE 8082  
EXPOSE 8083  
EXPOSE 8084  
RUN \  
apt-get update && \  
apt-get install -y maven --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
RUN source "/root/.sdkman/bin/sdkman-init.sh" && \  
sdk install groovy 2.4.7 && \  
sdk install gradle 2.9 && \  
sdk install springboot 1.4.0.RELEASE  
  

