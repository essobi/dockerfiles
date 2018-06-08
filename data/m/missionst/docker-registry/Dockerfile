FROM samalba/docker-registry:latest  
  
ADD ./config.yml /docker-registry/config/config.yml  
CMD cd /docker-registry && ./setup-configs.sh && ./run.sh  

