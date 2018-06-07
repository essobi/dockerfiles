FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y openjdk-8-jdk maven x11vnc xvfb && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY run.sh /run.sh  
  
VOLUME ["/tuleap-mylyn-src"]  
ENTRYPOINT ["/run.sh"]  
CMD ["--test"]  

