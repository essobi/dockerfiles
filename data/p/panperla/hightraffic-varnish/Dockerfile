FROM ubuntu  
MAINTAINER mp@meant4.com  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install varnish -y  
RUN mkdir -p /app  
WORKDIR /app  
COPY start /app/start  
RUN chmod +x /app/start  
EXPOSE 8080  
RUN rm /etc/varnish/default.vcl  
COPY default.vcl /etc/varnish/default.vcl  
RUN chmod 644 /etc/varnish/default.vcl  
RUN chown root.root /etc/varnish/default.vcl  
CMD /app/start

