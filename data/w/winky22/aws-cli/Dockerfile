FROM alpine:3.7  
MAINTAINER winky  
  
# Install packages  
RUN apk --update add \  
python \  
py-pip  
  
# Install awscli  
RUN pip install awscli  
  
ENV PAGER="less"  
ENTRYPOINT ["/usr/bin/aws"]  
CMD ["help"]  

