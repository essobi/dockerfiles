FROM stilliard/pure-ftpd  
LABEL \  
nl.thinkbright.ftpserver.author = "jacco@thinkbright.nl" \  
nl.thinkbright.ftpserver.version = "1.0"  
  
# Each line of this file contains: username,password  
ENV FTP_SERVER_PASSWORDS_FILE /path/to/file.csv  
  
# Override original run.sh, this creates users and then calls the original
run.sh  
RUN mv /run.sh /run-original.sh  
COPY ./run-override.sh /run.sh  

