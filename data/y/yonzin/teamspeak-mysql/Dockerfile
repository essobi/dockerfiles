FROM mbentley/teamspeak  
  
USER root  
  
ADD files/libs/libts3db_mysql.so /opt/teamspeak/libts3db_mysql.so  
  
ADD files/libs/libmysqlclient.so.15 /usr/lib/libmysqlclient.so.15  
  
ADD files/config/ts3server.ini /opt/teamspeak/ts3server.ini  
  
ADD files/config/ts3db_mysql.ini /opt/teamspeak/ts3db_mysql.ini  
  
EXPOSE 9987/udp 10011 30033 41144  
  
RUN chown -R teamspeak.teamspeak /opt/teamspeak/  
  
USER teamspeak  
  
VOLUME /opt/teamspeak/logs  
  
ENTRYPOINT ["/opt/teamspeak/ts3server_minimal_runscript.sh"]  
  
CMD ["inifile=/opt/teamspeak/ts3server.ini"]  

