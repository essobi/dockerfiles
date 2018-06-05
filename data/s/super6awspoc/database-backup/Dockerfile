FROM super6awspoc/php-base:1.14.0  
RUN mkdir /process  
COPY process/ /process/  
  
RUN chmod +x /process/run  
  
RUN apk add --no-cache python py-pip mysql-client  
RUN pip install boto3 awscli  
  
CMD ["/process/run"]  
#CMD ["crond", "-f", "-d", "8"]  

