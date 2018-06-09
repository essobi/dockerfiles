# BUILD-USING: docker build -t haproxy .  
# PUSH-USING: docker tag haproxy surf/haproxy && docker push surf/haproxy  
FROM surf/docker-base  
  
RUN sudo apt-get update && apt-get install -y haproxy  
  
EXPOSE 80  
EXPOSE 3212  
CMD ["haproxy", "-f" ,"/haproxy/haproxy.cfg" ,"-db"]  

