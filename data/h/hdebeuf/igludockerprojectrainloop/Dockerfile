FROM hardware/rainloop  
  
ENV PROJECT_NAME_WITH_SPACES Le projet \  
PROJECT_DOMAIN newproject.iglu.com \  
MAILSERVER newproject_mailserver \  
WEBMASTER_LOGIN webmaster \  
WEBMASTER_PASSWORD Tigrou007  
  
ADD _default_/* /rainloop/data/_data_/_default_/  
ADD rainloopinit.sh /rainloopinit.sh  
RUN chmod +x /rainloopinit.sh  
  
VOLUME /rainloop/data  
  
EXPOSE 8888  
ENTRYPOINT ["/rainloopinit.sh"]  

