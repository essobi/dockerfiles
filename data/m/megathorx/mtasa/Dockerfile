FROM debian:latest  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y unzip libreadline5 libncursesw5 wget && \  
groupadd -g 2000 container && \  
useradd -d /home/container -m container -u 2000 -g 2000 && \  
mkdir /mtasa && \  
chown 2000:2000 /mtasa  
  
USER 2000:2000  
  
RUN wget -O /home/container/multitheftauto_linux_x64.tar.gz
https://nightly.mtasa.com/?multitheftauto_linux_x64-1.5-rc-latest && \  
tar -xf /home/container/multitheftauto_linux_x64.tar.gz -C /mtasa --strip-
components=1 && \  
rm -f /home/container/multitheftauto_linux_x64.tar.gz && \  
mkdir /mtasa/config && \  
wget -O /home/container/baseconfig.tar.gz
https://linux.mtasa.com/dl/baseconfig.tar.gz && \  
tar -xf /home/container/baseconfig.tar.gz -C /mtasa/config --strip-
components=1 && \  
rm /home/container/baseconfig.tar.gz  
  
EXPOSE 22003 22005 22126  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

