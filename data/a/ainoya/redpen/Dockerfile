FROM quay.io/ainoya/java  
  
WORKDIR /tmp  
RUN wget -q https://github.com/redpen-
cc/redpen/releases/download/v1.3.0/redpen-1.3.0.tar.gz -O - | tar xz && \  
cp -av redpen-distribution-1.3/* /usr/local/ && \  
rm -rf redpen-distribution-1.3  
  
RUN export PATH=$PATH:/usr/local/bin  
WORKDIR /data  
  
CMD ["/usr/local/bin/redpen"]  

