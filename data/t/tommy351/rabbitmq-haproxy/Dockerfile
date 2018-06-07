FROM rabbitmq:3.6  
MAINTAINER Tommy Chen <tommy351@gmail.com>  
  
RUN apt-get -y update && \  
apt-get install -y --no-install-recommends --no-install-suggests supervisor
haproxy && \  
rm -rf /var/lib/apt/lists/*  
  
COPY start.sh /  
COPY supervisord.conf /  
COPY haproxy.cfg /etc/haproxy  
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config  
  
EXPOSE 5672 5673 5674  
CMD ["./start.sh"]

