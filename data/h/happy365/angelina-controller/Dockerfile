FROM ubuntu:xenial  
ENV BaseUrl http://files.happy366.cn/files/docker/angelina2  
ENV AngelinaUrl https://github.com/happy2048/angelina2.git  
RUN apt-get update  
RUN apt-get install wget git tzdata -y  
EXPOSE 6300  
ENV version 2.3  
RUN cd /opt && \  
git clone https://github.com/happy2048/angelina2.git && \  
cd angelina2 && \  
cp bin/angelina-runner /root/angelina-runner && \  
cp bin/angelina-controller /usr/bin/angelina-controller && \  
cp utils/redis-cli /usr/bin/redis-cli && \  
cp utils/socket_client /usr/bin/socket_client && \  
cp utils/angelina-runner-pod.yml /root/angelina-runner-pod.yml && \  
chmod +x /usr/bin/angelina-controller && \  
chmod +x /usr/bin/redis-cli && \  
chmod +x /usr/bin/socket_client && \  
rm -rf /etc/localtime && \  
ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata && \  
rm -rf /opt/angelina2  
ENTRYPOINT ["angelina-controller"]  

