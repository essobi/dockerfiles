FROM debian:jessie  
MAINTAINER latrokles@gmail.com  
  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }' \  
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
tmux \  
vim \  
zsh  
  
ENV LANG C.UTF-8  
CMD ["zsh"]  

