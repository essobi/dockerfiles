FROM anapsix/alpine-java:8_jdk  
  
ENV HOME /home/s101  
  
RUN adduser -D s101 && \  
apk update && \  
apk add libxext libxtst libxrender && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
USER s101  
WORKDIR /home/s101  
  
RUN wget http://structure101.com/binaries/structure101-studio-java-
unix-4.2.10537.tar.gz -O ~/structure101-studio-java-unix-4.2.10537.tar.gz -q
&&\  
tar xvf ~/structure101-studio-java-unix-4.2.10537.tar.gz &&\  
rm ~/structure101-studio-java-unix-4.2.10537.tar.gz  
  
CMD ~/Structure101/java/structure101-studio

