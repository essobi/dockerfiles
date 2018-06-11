FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common python-software-properties \  
&& apt-get install -y python python-pip\  
&& apt-get install -y supervisor\  
&& pip install supervisor-stdout \  
&& apt-get purge -y python-software-properties software-properties-common \  
&& apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN service supervisor stop  
  
# Set the time zone to the local time zone  
RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
CMD supervisord -c /etc/supervisord.conf -n  

