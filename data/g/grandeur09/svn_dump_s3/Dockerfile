FROM alpine:latest  
MAINTAINER Nakano Masatoshi "nakano.masatoshi@stf.nifty.co.jp"  
RUN apk --update add subversion && rm -rf /var/cache/apk/*  
  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
ENV S3_ACCESS_KEY_ID **None**  
ENV S3_SECRET_ACCESS_KEY **None**  
ENV S3_BUCKET **None**  
ENV S3_ENDPOINT **None**  
ENV S3_PREFIX 'backup'  
ENV S3_REGION us-west-1  
ENV S3_S3V4 no  
ENV MULTI_FILES no  
ENV SCHEDULE **None**  
  
ADD run.sh run.sh  
ADD backup.sh backup.sh  
  
CMD ["sh", "run.sh"]  

