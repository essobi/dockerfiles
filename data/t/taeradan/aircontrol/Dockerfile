FROM debian:jessie  
  
RUN apt-get update && apt-get install -y default-jre-headless jsvc wget  
RUN wget
http://www.ubnt.com/downloads/aircontrol/aircontrol_1.4.2-beta_all.deb &&\  
dpkg -i aircontrol_1.4.2-beta_all.deb &&\  
rm aircontrol_1.4.2-beta_all.deb  
  
RUN sed -i -e's/JAVA_HOME=/#JAVA_HOME=/' /etc/init.d/aircontrol  
RUN sed -i -e's/export\ JAVA_HOME/#export JAVA_HOME/' /etc/init.d/aircontrol  
  
EXPOSE 9080  
RUN mkdir -p /usr/share/aircontrol/logs/ &&\  
touch /usr/share/aircontrol/logs/server.log  
  
ENTRYPOINT service aircontrol start && tail -f
/usr/share/aircontrol/logs/server.log  

