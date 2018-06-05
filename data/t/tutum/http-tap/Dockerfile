FROM tutum/haproxy:latest  
  
RUN apt-get update && apt-get install -yq socat && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
ADD / /  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
ENV FRONTEND_BIND 0.0.0.0:80  
ENV BACKEND_SERVER 127.0.0.1:8080  
ENV PATH $PATH:/  
CMD ["/run.sh"]

