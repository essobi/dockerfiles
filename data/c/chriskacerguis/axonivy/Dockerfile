FROM ubuntu:16.04  
LABEL maintainer="Chris Kacerguis <chriskacerguis@gmail.com>"  
  
# Install wget, unzip and jre since the downloaded engine does not include jre  
RUN apt-get update && apt-get install -y \  
wget \  
curl \  
unzip \  
openjdk-8-jre-headless  
  
ENV DB_HOST localhost  
ENV DB_NAME database  
ENV DB_USER root  
ENV DB_PASS password  
ENV DB_PORT 3306  
ENV AXON_USER admin  
ENV AXON_PASS password  
ENV AXON_EMAIL tony@starkindustries.com  
  
RUN mkdir -p /opt/ivy/engine  
  
# AxonIvyEngine7.0.5.58420_All_x64.zip  
# AxonIvyEngine7.1.0.58200_All_x64.zip  
RUN wget https://developer.axonivy.com/permalink/ivy/stable/AxonIvyEngine-
latest_All_x64.zip -O AxonIvyEngine7.zip && \  
unzip AxonIvyEngine7.zip -d /opt/ivy/engine/latest && \  
rm -f AxonIvyEngine7.zip  
  
EXPOSE 8081:8081  
VOLUME /data  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
CMD ["/bin/sh", "/usr/local/bin/entrypoint.sh"]  

