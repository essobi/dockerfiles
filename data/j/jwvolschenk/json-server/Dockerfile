FROM clue/json-server:latest  
MAINTAINER J.W. Volschenk <jwvolschenk@gmail.com>  
  
ADD db.json /data/db.json  
  
EXPOSE 5000  
ADD run.sh /run.sh  
ENTRYPOINT ["bash", "/run.sh"]

