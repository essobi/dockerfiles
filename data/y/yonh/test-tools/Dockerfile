# build  
# sudo docker build -t yonh/test-tools  
# run  
# sudo docker run -it --rm yonh/test-tools  
FROM ubuntu:14.04  
MAINTAINER yonh "azssjli@163.com"  
ENV REFERSHED_AT 2016-05-23  
#replace default sources.list  
#ADD sources.list /etc/apt/sources.list  
ADD ./* /opt/  
  
WORKDIR /opt/  
  
RUN bash compile.sh  
  
CMD ["/bin/bash"]  

