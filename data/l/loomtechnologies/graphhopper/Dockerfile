FROM openjdk:8-jdk  
  
WORKDIR /graphhopper  
  
RUN mkdir -p /data && \  
mkdir -p /graphhopper && \  
cd /graphhopper && \  
git clone https://github.com/graphhopper/graphhopper.git . && \  
git checkout c8c5d5c4841ff9bcd2f9fa9d97ec4888b13953d4 && \  
rm -rf .git  
  
COPY assets/config.properties /graphhopper/  
COPY assets/start.sh /graphhopper/  
  
VOLUME ["/data"]  
EXPOSE 8989  

