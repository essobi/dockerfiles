FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
VOLUME /codeload  
  
COPY bin /opt/quantrocket/bin/  
RUN chmod +x /opt/quantrocket/bin/*  
  
CMD ["/opt/quantrocket/bin/gitclone.sh"]  

