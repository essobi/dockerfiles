FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN apk --no-cache add py-pip  
RUN pip install grip  
RUN mkdir /.grip && mkdir /data  
  
USER 1000  
WORKDIR /data  
ENTRYPOINT ["grip"]  
CMD ["--help"]  

