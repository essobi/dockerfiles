FROM debian:sid  
  
RUN apt-get update && apt-get install -y clang-format-3.8  
  
# switch to uid/gid identical to host uid/gid (forks/users), if not doing
this, files that  
# clang-format written will change user and group all to root.  
USER 1000:100  
  
ENTRYPOINT ["clang-format-3.8", "-style=Google", "-i"]  

