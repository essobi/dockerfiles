FROM programfan/docker-gitit:latest  
LABEL maintainer="Yang Zhang <zyangmath@gmail.com>"  
  
VOLUME ["/data/gitit-wiki", "/data/gitit-run"]  
ADD ./gitit-templates-enhanced /data/gitit-templates-enhanced/  
ADD ./docker-entrypoint.sh /usr/local/bin/  
ADD ./run-service.sh /usr/local/bin/  
  
EXPOSE 7500  
WORKDIR "/data/gitit-run"  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  

