# Pull base image.  
FROM howtox/node_base  
  
RUN apt-get -y install python-setuptools  
  
# Need make  
RUN apt-get install -y build-essential  
  
RUN easy_install supervisor  
RUN mkdir -p /var/log/supervisor  
  
# create directory for child images to store configuration in  
RUN mkdir -p /etc/supervisor/conf.d  
ADD ./docker_config/srv/howtox/supervisord.conf /etc/supervisord.conf  
  
ENV HOME /root  
WORKDIR /root  
  
# Add scripts  
ADD ./docker_config/root /root  
ADD ./docker_config/srv /srv  
RUN chmod +x /srv/howtox/docker_start.sh  
  
# for /srv/howtox  
RUN git clone https://github.com/shaohua/cloud9.git /srv/howtox/cloud9  
RUN cd /srv/howtox/cloud9 && npm install  
RUN cd /srv/howtox && npm install tty.js  
  
# for this repo  
RUN git clone https://github.com/sofish/pen.git /root/pen  
RUN cd /root/pen && npm install  
RUN npm install -g grunt-cli  
  
EXPOSE 3131 3132 3133  
CMD ["/usr/local/bin/supervisord"]  

