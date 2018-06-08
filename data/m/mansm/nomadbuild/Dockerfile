FROM golang:wheezy  
ENV XC_OS=linux  
ENV XC_ARCH=amd64  
  
RUN apt-get update && apt-get install -y sudo zip && \  
apt-get clean all  
  
COPY build.sh /root/build.sh  
RUN chmod +x /root/build.sh  
  
RUN mkdir /out  
VOLUME ["/out"]  
  
CMD ["/root/build.sh"]

