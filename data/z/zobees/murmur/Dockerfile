FROM anapsix/alpine-java:8  
MAINTAINER cliffrowley@gmail.com  
  
RUN apk --update add icu-libs murmur  
  
RUN mkdir -p /murmur/data  
  
COPY murmur.ini /etc/murmur.ini  
  
WORKDIR /murmur/data  
  
VOLUME /murmur/data  
  
EXPOSE 64738 64738/udp  
  
CMD ["murmurd", "-fg"]  

