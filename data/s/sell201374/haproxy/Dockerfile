FROM ubuntu:15.04  
RUN apt-get update -y  
RUN apt-get install haproxy -y  
RUN apt-get install git -y  
COPY haproxy.cfg /etc/haproxy/haproxy.cfg  
COPY run_haproxy.sh /etc/haproxy/run_haproxy.sh  
RUN chmod +x /etc/haproxy/run_haproxy.sh  
COPY haproxy /etc/default/haproxy  
# Define default command.  
EXPOSE 80  
CMD ["/etc/haproxy/run_haproxy.sh"]  
#WORKDIR /etc/haproxy  

