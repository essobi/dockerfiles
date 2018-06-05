FROM fdiblen/archsci:latest  
  
MAINTAINER fdiblen  
  
ENV container docker  
  
USER root  
  
# setup port mapping  
EXPOSE 1935:1935  
EXPOSE 80:80  
EXPOSE 443:443  
ADD nginx.conf.template /tmp/nginx.conf  
  
ADD serve.sh /usr/local/bin/serve.sh  
RUN chmod +x /usr/local/bin/serve.sh  
  
USER archsci  
  
RUN yaourt --noconfirm --needed -S \  
nginx-rtmp  
  
RUN echo 'cat /tmp/nginx.conf >> /etc/nginx/nginx.conf' | sudo -s \  
&& sudo rm -f /tmp/nginx.conf  
  
CMD ["/usr/local/bin/serve.sh"]  

