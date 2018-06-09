FROM debian  
RUN apt-get update && \  
apt-get install -y shellcheck && \  
rm -rf /var/lib/apt/lists/*  
ENTRYPOINT [ "shellcheck" ]  

