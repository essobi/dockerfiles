FROM alpine:3.7  
LABEL maintainer="Vendelev Artiom"  
LABEL version="1.0"  
LABEL image="vendelev/supervisor"  
LABEL description="Image for web application with supervisor"  
  
ENV TIMEZONE Europe/Moscow  
  
# Install timezone supervisor  
RUN apk add --no-cache tzdata supervisor \  
&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& echo "${TIMEZONE}" > /etc/timezone \  
&& mkdir /etc/supervisor.d \  
&& mkdir /var/log/supervisor \  
&& sed -i 's/;\\[inet_http_server]/\\[inet_http_server]/g'
/etc/supervisord.conf \  
&& sed -i 's/;port=127.0.0.1:9001/port=*:9999/g' /etc/supervisord.conf  
  
EXPOSE 9999  
CMD ["supervisord", "--nodaemon"]  

