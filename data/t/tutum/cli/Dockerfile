FROM alpine  
MAINTAINER support@tutum.co  
  
RUN apk --update add python py-pip && \  
pip install tutum && \  
tutum -v  
WORKDIR /root  
  
ENTRYPOINT ["tutum"]  

