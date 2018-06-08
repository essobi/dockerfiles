FROM debian:latest  
  
MAINTAINER Curt H., <curt@curtcreation.net>  
  
RUN apt update && \  
apt upgrade -y && \  
apt install -y lib32gcc1 unzip curl libreadline5 libncursesw5 lib32ncursesw5
lib32stdc++6 wget && \  
useradd -d /home/container -m container  
  
USER container  
ENV  USER container  
ENV HOME /home/container  
  
WORKDIR /home/container  
  
EXPOSE 1000-30000  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

