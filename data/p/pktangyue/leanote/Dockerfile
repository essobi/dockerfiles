FROM centos:7  
MAINTAINER pktangyue <tangyue1004@gmail.com>  
  
ENV HOME /root  
ENV GOROOT $HOME/go  
ENV GOPATH $HOME/gopackage  
ENV MONGOPATH $HOME/mongodb  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin:$MONGOPATH/bin  
  
WORKDIR /root/  
COPY install.sh run.sh /root/  
RUN sh install.sh  
  
EXPOSE 9000  
CMD ["sh", "run.sh"]  

