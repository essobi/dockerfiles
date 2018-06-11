FROM buildpack-deps:jessie  
  
RUN wget https://drone.io/github.com/wansc2015/dockerui/files/build.tgz && tar
-C / -xzf build.tgz  
  
EXPOSE 9000  
ENTRYPOINT ["/dockerui"]  

