FROM ubuntu:14.04  
RUN apt-get update && apt-get install s3cmd -yqq  
  
ADD .s3cfg /root/  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  
  
CMD ["s3cmd"]  

