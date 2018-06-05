FROM ubuntu:16.04  
EXPOSE 80  
EXPOSE 443  
EXPOSE 7080  
RUN apt-get update \  
&& apt-get install -y haproxy openssl \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& apt-get clean  
  
RUN openssl req -subj '/CN=proxify/O=PROXIFY/C=US' -new -newkey rsa:2048 -days
3650 -nodes -x509 -keyout /etc/haproxy/proxify.key -out
/etc/haproxy/proxify.crt \  
&& cat /etc/haproxy/proxify.crt /etc/haproxy/proxify.key >
/etc/haproxy/proxify.pem  
  
ADD lib/haproxy.cfg /etc/haproxy/haproxy.cfg  
  
CMD haproxy -f /etc/haproxy/haproxy.cfg -p "/var/run/haproxy.pid"  

