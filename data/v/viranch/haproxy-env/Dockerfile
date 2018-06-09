FROM haproxy:1.5  
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*  
  
RUN curl -L
https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-linux-
amd64-v0.0.2.tar.gz | tar zx -C /usr/local/bin  
  
ADD haproxy.tmpl /etc/dockerize/  
  
CMD dockerize -template
/etc/dockerize/haproxy.tmpl:/usr/local/etc/haproxy/haproxy.cfg haproxy -f
/usr/local/etc/haproxy/haproxy.cfg  

