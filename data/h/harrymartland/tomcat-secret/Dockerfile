FROM tomcat:alpine  
  
ENV SECRET_FILE_PATH=/run/secrets/*  
ENV REPLACE_FILE_PATH=/usr/local/tomcat/conf/*.xml  
  
CMD ["./replaceSecretsAndRun.sh"]  
  
COPY replaceSecretsAndRun.sh replaceSecretsAndRun.sh  
RUN chmod +x replaceSecretsAndRun.sh

