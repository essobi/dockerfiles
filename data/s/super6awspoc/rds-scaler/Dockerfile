FROM super6awspoc/php-base:1.18.0  
RUN mkdir /process && \  
apk add --no-cache python py-pip mysql-client && \  
pip install boto3 awscli  
  
COPY process/ /process/  
  
RUN chmod +x /process/run.sh  
  
CMD ["/process/run.sh"]  

