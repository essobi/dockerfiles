FROM anapsix/alpine-java:jre8  
MAINTAINER Shuky Dvir <shuky@devops.co.il>  
  
RUN mkdir -p /s3proxy  
WORKDIR /s3proxy  
  
RUN wget
https://github.com/andrewgaul/s3proxy/releases/download/s3proxy-1.4.0/s3proxy
\  
&& chmod +x s3proxy  
  
COPY s3proxy.conf /s3proxy/s3proxy.conf  
  
RUN mkdir -p /s3proxy_data  
  
EXPOSE 4567  
VOLUME ["/s3proxy_data"]  
  
CMD [ "/s3proxy/s3proxy", "--properties", "/s3proxy/s3proxy.conf" ]

