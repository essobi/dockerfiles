FROM nginx:latest  
  
RUN apt-get update \  
&& apt-get install -y unzip \  
&& apt-get install -y git \  
&& apt-get install -y dnsutils \  
&& apt-get install -y cron \  
&& apt-get install curl -y  
  
ADD files/start.sh /bin/start.sh  
ADD files/generate-ssl-certs.sh /bin/generate-ssl-certs.sh  
ADD files/renew-ssl /etc/cron.weekly/renew-ssl  
  
ADD files/switch /bin/switch  
RUN chmod +x /bin/start.sh  
RUN chmod +x /bin/switch  
RUN chmod +x /bin/generate-ssl-certs.sh  
RUN chmod +x /etc/cron.weekly/renew-ssl  
  
RUN cd /opt \  
&& git clone https://github.com/certbot/certbot  
  
ADD files/default.ctmpl /templates/default.ctmpl  
ADD files/unsecured.ctmpl /templates/unsecured.ctmpl  
  
ADD https://releases.hashicorp.com/consul-template/0.12.2/consul-
template_0.12.2_linux_amd64.zip /usr/bin/  
RUN unzip /usr/bin/consul-template_0.12.2_linux_amd64.zip -d /usr/local/bin  
  
RUN /etc/init.d/cron start  
  
RUN mkdir /app  
RUN mkdir /api  
ENV LIVE green  
ENV BLUE_APP ekaya_vip_blue  
ENV GREEN_APP ekaya_vip_green  
ENV BLUE_API ekaya_server_blue  
ENV GREEN_API ekaya_server_green  
  
EXPOSE 80 8888 443  
ENTRYPOINT ["/bin/start.sh"]  

