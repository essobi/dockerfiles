FROM ubuntu:14.04.3  
MAINTAINER Dmitry Mozzherin  
ENV LAST_FULL_REBUILD 2016-02-25  
RUN mkdir app  
COPY . app  
  
WORKDIR /app  
  
CMD ["perl", "server.pl"]  

