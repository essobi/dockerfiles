FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
default-jre-headless \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/local/s3proxy  
ENV PATH /usr/local/s3proxy:$PATH  
  
ADD
https://github.com/andrewgaul/s3proxy/releases/download/s3proxy-1.4.0/s3proxy
/usr/local/s3proxy  
ADD s3proxy.conf /usr/local/s3proxy/s3proxy.conf  
RUN chmod +x /usr/local/s3proxy/s3proxy  
  
RUN mkdir -p /data  
WORKDIR /data  
  
EXPOSE 8080  
CMD ["s3proxy", "--properties", "/usr/local/s3proxy/s3proxy.conf"]  

