FROM jenkinsci/jenkins:lts  
  
USER root  
  
COPY user.sh /user.sh  
RUN chmod +x /user.sh && cp /usr/local/bin/jenkins.sh /jenkins.sh  
  
USER ${user}  
  
ENTRYPOINT ["/user.sh"]  

