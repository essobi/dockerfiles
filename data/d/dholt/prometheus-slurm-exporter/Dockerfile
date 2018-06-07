FROM ubuntu:18.04 as build  
RUN apt-get update && \  
apt-get -y install golang-github-prometheus-client-golang-dev git build-
essential golang && \  
git clone https://github.com/vpenso/prometheus-slurm-exporter.git && \  
cd prometheus-slurm-exporter && \  
make && \  
mv bin/prometheus-slurm-exporter /tmp && \  
cd / && \  
rm -rf /prometheus-slurm-exporter /var/lib/apt/lists/*  
  
FROM ubuntu:18.04  
COPY --from=build /tmp/prometheus-slurm-exporter /usr/bin  
RUN apt-get update && \  
apt-get -y install munge && \  
useradd -M slurm && \  
rm -rf /var/lib/apt/lists/*  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/prometheus-slurm-exporter"]  

