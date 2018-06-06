FROM ubuntu:latest  
MAINTAINER info@chatspace.ai  
  
RUN cd /  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists/*  
RUN wget
https://github.com/prometheus/prometheus/releases/download/v2.0.0-beta.4/prometheus-2.0.0-beta.4.linux-
amd64.tar.gz  
RUN tar -xvf prometheus-2.0.0-beta.4.linux-amd64.tar.gz  
RUN mv prometheus-2.0.0-beta.4.linux-amd64 prometheus  
  
COPY prometheus.yaml /prometheus/prometheus.yml  
EXPOSE 9090  
WORKDIR /prometheus  
ENTRYPOINT [ "/prometheus/prometheus" ]  

