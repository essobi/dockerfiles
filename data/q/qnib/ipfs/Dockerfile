FROM qnib/alpn-consul  
  
#ENV IPFS_GATEWAY_ADDR=/ip4/0.0.0.0/tcp/8080  
#ENV IPFS_API_ADDR=/ip4/0.0.0.0/tcp/5001  
ENV GATEWAY_PORT=8080 \  
API_PORT=5001 \  
IPFS_LOGGING=info  
  
VOLUME /data/ipfs/  
RUN wget -qO /usr/local/bin/ipfs https://github.com/qnib/go-
ipfs/releases/download/0.4.5-pnet/ipfs-0.4.5-pnet_MuslLinux \  
&& chmod +x /usr/local/bin/ipfs  
ADD etc/supervisord.d/ipfs.ini /etc/supervisord.d/  
ADD etc/consul.d/ipfs.json /etc/consul.d/  
ADD opt/qnib/ipfs/bin/start.sh \  
opt/qnib/ipfs/bin/check.sh \  
/opt/qnib/ipfs/bin/  
RUN echo 'tail -f /var/log/supervisor/ipfs.log' >> /root/.bash_history  

