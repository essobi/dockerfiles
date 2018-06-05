FROM alpine:3.4  
MAINTAINER a504082002 <a504082002@gmail.com>  
  
# Install dependencies  
RUN apk add --update --no-cache python curl  
  
# Install ncbi-blast+  
RUN mkdir -p /opt/blast && \  
curl ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.6.0/ncbi-
blast-2.6.0+-x64-linux.tar.gz \  
| tar -zxC /opt/blast  
ENV PATH /opt/blast/bin:$PATH  
  
WORKDIR /data  
CMD ["bash"]  

