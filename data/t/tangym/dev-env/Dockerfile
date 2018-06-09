FROM ubuntu:14.04  
MAINTAINER tym  
  
RUN apt-get update  
RUN apt-get install -y \  
tmux nano unzip curl wget \  
python3 python3-pip python3-scipy python3-matplotlib \  
nginx libfreetype6 libfreetype6-dev libpng12-dev \  
texlive-xetex  
RUN pip3 install flask flask_restful \  
numpy \  
pyyaml markdown  
RUN pip3 install pandas seaborn  
# psyco  
EXPOSE 0-65535  

