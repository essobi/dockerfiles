FROM devinsba/supervisor_base  
  
RUN \  
echo "deb http://www.rabbitmq.com/debian/ testing main" >>
/etc/apt/sources.list.d/rabbit.list && \  
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc && \  
apt-key add rabbitmq-signing-key-public.asc && \  
rm rabbitmq-signing-key-public.asc && \  
apt-get update && \  
apt-get install -y rabbitmq-server && \  
rabbitmq-plugins enable rabbitmq_management && \  
echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config  
  
ADD rabbit.conf /etc/supervisor/conf.d/rabbit.conf  
ADD rabbit.sh /bin/rabbit.sh  
RUN chmod u+x /bin/rabbit.sh  
  
EXPOSE 5672 15672 25672  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

