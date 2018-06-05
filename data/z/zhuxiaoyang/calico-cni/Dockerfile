FROM alpine:3.5  
ENV PATH /z  
ENV PATH /bin:/usr/local/bin:/opt/cni/bin:$PATH  
  
ADD install-cni.sh /install-cni.sh  
  
RUN chmod 777 /install-cni.sh  

