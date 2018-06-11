FROM ubuntu:latest  
  
RUN apt-get update && apt-get upgrade -y && \  
apt-get install wget -y && \  
wget --no-check-certificate
https://files.zimbra.com/downloads/8.7.5_GA/zcs-8.7.5_GA_1764.UBUNTU16_64.20170314032533.tgz
&& \  
tar -xvf /zcs-8.7.5_GA_1764.UBUNTU16_64.20170314032533.tgz && \  
mv /zcs-8.7.5_GA_1764.UBUNTU16_64.20170314032533 /root/zimbra && \  
cd /root/zimbra && \  
chmod +x install.sh  
COPY ./entrypoint.sh /  
RUN chmod +x entrypoint.sh && apt-get install lsb-release -y  
ENTRYPOINT ["/entrypoint.sh"]  

