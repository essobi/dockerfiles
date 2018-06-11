FROM alpine:3.4  
MAINTAINER Winston <bjdhjj@gmail.com>  
RUN apk --no-cache add supervisor git python curl  
RUN git clone -b manyuser https://github.com/shadowsocksr/shadowsocksr.git  
COPY supervisord.conf /etc/supervisord.conf  
ADD kcptun /root/kcptun  
COPY reset_daocloud.sh /root/reset_daocloud.sh  
RUN chmod +x /root/kcptun/server_linux_amd64 /root/kcptun/client_linux_amd64
/root/*.sh  
ENV remotehost=10.10.10.10 \  
remoteport=4000 \  
api_token=api_token \  
api_key=api_key \  
app_id=app_id \  
ssr_key=alpine \  
daocloud_appid=daocloud_appid \  
daocloud_token=daocloud_token  
ADD entrypoint.sh /usr/sbin  
RUN chmod +x /usr/sbin/entrypoint.sh  
EXPOSE 443 4000/udp  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]  

