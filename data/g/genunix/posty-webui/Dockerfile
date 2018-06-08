FROM httpd:2.4  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y git  
RUN git clone https://github.com/posty/posty_webui.git /tmp/posty_webui  
RUN rm -rf /usr/local/apache2/htdocs/*  
RUN cp -r /tmp/posty_webui/dist/* /usr/local/apache2/htdocs/  
  
ADD files/entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

