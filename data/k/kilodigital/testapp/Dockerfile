FROM alpine  
  
VOLUME /code  
  
ADD code /stage/  
ADD build/deploy.sh /  
  
ADD build/configs /stageConfig/  
ADD build/deploy_config.sh /  
  
CMD /deploy_config.sh && /deploy.sh

