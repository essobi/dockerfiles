FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y python-dev python-virtualenv redis-server supervisor  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
  
USER root  
  
RUN mkdir /root/logs  
  
RUN bash -c "cd /root && virtualenv tb-env && source /root/tb-env/bin/activate
&& pip install tipboard"  
  
EXPOSE 7272  
  
VOLUME /root/.tipboard  
  
CMD ["/usr/bin/supervisord", "-j", "/root/supervisord.pid"]  

