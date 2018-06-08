FROM ubuntu:16.04  
LABEL maintainer "smurex <se.mueller91@gmail.com>"  
  
RUN apt-get update &&\  
apt-get install -y texlive-full \  
biber \  
fonts-liberation \  
\--no-install-recommends &&\  
rm -rf /var/lib/apt/lists/* &&\  
luaotfload-tool --update  
  
CMD /bin/bash  

