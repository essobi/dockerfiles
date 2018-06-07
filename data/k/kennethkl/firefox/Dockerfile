FROM dockerfile/ubuntu  
  
RUN \  
apt-get update && \  
apt-get install -y firefox && \  
rm -rf /var/lib/apt/lists/*  
  
RUN adduser firefox  
  
USER firefox  
ENV HOME /home/firefox  
  
CMD []  
ENTRYPOINT ["/usr/bin/firefox"]  

