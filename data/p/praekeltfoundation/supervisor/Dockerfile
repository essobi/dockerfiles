FROM praekeltfoundation/python-base:debian  
  
COPY ./requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
  
# Mimic the Debian/Ubuntu config file structure  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
RUN mkdir -p /etc/supervisor/conf.d \  
/var/log/supervisor  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

