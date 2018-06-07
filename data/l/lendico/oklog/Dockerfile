FROM alpine:3.5  
MAINTAINER Seong-Min Kang <seong-min.kang@lendico.de>  
  
ENTRYPOINT ["/oklog"]  
  
EXPOSE 7659 7651 7653 7650  
RUN mkdir /data \  
&& chown nobody /data  
  
ADD https://github.com/oklog/oklog/releases/download/v0.1.1/oklog-0.1.1-linux-
amd64 /oklog  
RUN ["chmod", "775", "/oklog"]  
  
USER nobody  
  
LABEL vendor=https://github.com/oklog/oklog \  
oklog.version=0.1.1 \  
oklog.release-date=2016-01-17  

