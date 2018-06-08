FROM frolvlad/alpine-python3  
  
RUN apk --no-cache add tzdata ca-certificates \  
&& pip install -I flexget transmissionrpc \  
&& mkdir -p /root/.flexget \  
&& touch /root/.flexget/config.yml \  
&& cp /usr/share/zoneinfo/Europe/London /etc/localtime \  
&& echo "Europe/London" > /etc/timezone \  
&& apk del tzdata  
  
COPY bootstrap.sh /root/bootstrap.sh  
  
RUN chmod +x /root/bootstrap.sh  
  
CMD ["/root/bootstrap.sh"]  

