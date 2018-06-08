FROM nginx:1.13  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y logrotate
cron wget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use confd: https://github.com/kelseyhightower/confd  
ENV CONFD_VERSION 0.14.0  
RUN cd /opt/ \  
&& wget --no-check-certificate -O confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 \  
&& mv confd /usr/local/bin \  
&& chmod +x /usr/local/bin/confd  
  
# Clear cron daily  
RUN rm /etc/cron.daily/*  
  
COPY ./config/cron/crontab /etc/crontab  
COPY ./config/cron/cron.daily/ /etc/cron.daily/  
COPY ./config/logrotate/nginx /etc/logrotate.d/nginx  
COPY ./config/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./config/confd/ /etc/confd/  
  
COPY ./shell/run.sh /usr/local/bin/run.sh  
  
RUN chmod +x /usr/local/bin/run.sh  
  
EXPOSE 80 443  
CMD ["/usr/local/bin/run.sh"]

