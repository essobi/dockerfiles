FROM michielbdejong/devbox  
RUN npm install -g pump.io  
RUN echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen" | tee -a /etc/apt/sources.list.d/10gen.list  
RUN apt-get update  
RUN apt-get install -y --force-yes mongodb-10gen  
RUN apt-get install -y python-pip  
RUN pip install supervisor  
RUN npm install databank-mongodb  
RUN echo_supervisord_conf > /etc/supervisord.conf  
ADD Supervisorfile /pumpio/  
RUN echo "[include]\nfiles = /pumpio/Supervisorfile\n" >>
/etc/supervisord.conf  
RUN ln -s /data/pump.io/pump.io.json /etc/pump.io.json  
EXPOSE 2001  
CMD ["/usr/local/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

