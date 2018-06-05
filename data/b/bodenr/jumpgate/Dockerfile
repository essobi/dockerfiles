FROM dockerfile/ubuntu  
MAINTAINER Boden Russell <bodenru@gmail.com>  
  
ADD install_jumpgate.sh /tmp/install_jumpgate.sh  
RUN chmod 777 /tmp/install_jumpgate.sh && /tmp/install_jumpgate.sh && rm
/tmp/install_jumpgate.sh  
  
ADD jgate /usr/local/bin/jgate  
RUN chmod 777 /usr/local/bin/jgate  
  
EXPOSE 5000  
CMD ["gunicorn", "jumpgate.wsgi:make_api()", "--bind=0.0.0.0:5000", "--
timeout=600", "--access-logfile=-", "-w", "4"]  

