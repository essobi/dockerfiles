FROM dordoka/tomcat  
  
MAINTAINER MinGu Lee <mglee@whatap.io>  
  
# Edit Catalina file to Attach WhaTap APM Agent  
ADD attach_script.sh /  
RUN cat /attach_script.sh >> /opt/tomcat/bin/catalina_new.sh  
RUN cat /opt/tomcat/bin/catalina.sh >> /opt/tomcat/bin/catalina_new.sh  
RUN rm /opt/tomcat/bin/catalina.sh  
RUN mv /opt/tomcat/bin/catalina_new.sh /opt/tomcat/bin/catalina.sh  
RUN chmod +x /opt/tomcat/bin/catalina.sh  
  
# Download WhaTap APM Agent through wget  
RUN wget https://apm.whatap.io/agent/whatap.agent.java.tar.gz -P /  
RUN tar -zxvf whatap.agent.java.tar.gz  
  
# Change license key for personal usage  
# Must be added to the directory which dockerfile is located in  
COPY start_script.sh /  
RUN chmod +x /start_script.sh  
RUN rm whatap/whatap.conf  
RUN touch whatap/whatap.conf  
RUN chmod +x whatap/whatap.conf  
  
# Start Tomcat  
ENTRYPOINT ["/start_script.sh"]  

