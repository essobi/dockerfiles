FROM southbanksoftware/cienvy:node-nm  
LABEL maintainer="developer@southbanksoftware.com"  
  
EXPOSE 9090  
COPY entrypoint.bash /  
  
WORKDIR /cienvy  
  
# -l: mimic login-shell  
ENTRYPOINT ["/bin/bash", "-l", "/entrypoint.bash"]  

