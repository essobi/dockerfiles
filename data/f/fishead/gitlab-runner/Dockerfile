FROM gitlab/gitlab-runner:v9.1.0  
MAINTAINER zhchuan7@gmail.com  
  
  
COPY custom-entrypoint.sh /  
RUN chmod +x /custom-entrypoint.sh  
  
ENTRYPOINT ["/custom-entrypoint.sh"]  

