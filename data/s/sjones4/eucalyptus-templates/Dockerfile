FROM sjones4/euca2ools:3.4  
ENV PATH=/root/bin:$PATH  
  
ADD [ "bin", "/root/bin/" ]  
ADD [ "templates", "/root/templates/" ]  
  
RUN chown --recursive root:root /root/bin/* \  
&& chmod 755 /root/bin/*  
  
WORKDIR /root/templates  

