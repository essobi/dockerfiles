FROM node:5  
  
ARG user=node  
ARG group=node  
ARG uid=1000  
ARG gid=1000  
  
RUN groupadd -g ${gid} ${group} \  
&& useradd -u ${uid} -g ${gid} -m -s /bin/bash ${user}  
RUN mkdir /.npm && chown -R ${user} /.npm  
  
USER ${user}  

