FROM debian:jessie  
#  
# Set correct environment variables.  
ENV HOME /data  
  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties && apt-get update\  
&& apt-get install -yq --no-install-recommends rsync\  
&& apt-get install -y python python-pip\  
&& pip install supervisor-stdout \  
&& apt-get install -y supervisor\  
&& apt-get purge -y python-software-properties software-properties-common &&
apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /data  
COPY ./run_scripts.py /run_scripts.py  
RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata\  
&& chmod +x /run_scripts.py\  
&& service supervisor stop  
ADD ./supervisord.conf /etc/supervisord.conf  
CMD supervisord -c /etc/supervisord.conf -n  
  

