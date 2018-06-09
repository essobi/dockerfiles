FROM python:3.5-alpine  
  
RUN apk --no-cache add tzdata ca-certificates \  
&& pip install -I flexget subliminal>=2.0 \  
&& cp /usr/share/zoneinfo/Europe/Paris /etc/localtime \  
&& echo "Europe/Paris" > /etc/timezone \  
&& apk del tzdata \  
&& mkdir -p /var/lib/flexget  
  
COPY flexget.sh /var/lib/flexget/flexget.sh  
  
RUN chmod +x /var/lib/flexget/flexget.sh  
  
VOLUME ["/var/lib/flexget"]  
  
CMD ["/var/lib/flexget/flexget.sh"]  

