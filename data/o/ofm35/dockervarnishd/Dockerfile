FROM ofm35/dockervarnish  
  
RUN apt-get update \  
&& apt-get install git -y  
  
EXPOSE 6081  
EXPOSE 6082  
ADD ./start.sh /start.sh  
RUN chmod 755 /start.sh  
  
CMD [ "/bin/bash", "/start.sh"]  

