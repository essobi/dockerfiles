FROM alang/nginx  
  
# dnsmasq: for local dns lookup  
# supervisor: to start dns and nginx  
RUN apt-get update -yqq && apt-get install -yqq \  
dnsmasq \  
supervisor  
  
# local DNS does need root privileges (note that dnsmasq.conf does not end
with a newline)  
RUN echo -n "\nuser=root" >> /etc/dnsmasq.conf  
  
# let nginx output go directly to stdout/stderr (done via symlink in base-
image)  
# this way the output can be picked up by supervisord  
RUN sed '/access_log/c\access_log /dev/stdout;' -i /etc/nginx/nginx.conf  
RUN sed '/error_log/c\error_log /dev/stderr warn;' -i /etc/nginx/nginx.conf  
  
COPY supervisord.conf /etc/supervisor/  
CMD supervisord -c /etc/supervisor/supervisord.conf  
  
COPY server.conf /etc/nginx/conf.d/  

