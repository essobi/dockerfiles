FROM jballou/steamcmd:latest  
USER root  
  
# Setup scheduling support  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
ADD files/scheduler_app/ /scheduler_app/  
WORKDIR /scheduler_app  
RUN npm install  
WORKDIR /  
  
# Add the steamcmd installation script  
ADD files/install.txt /install.txt  
  
# Copy scripts  
ADD files/start_7dtd.sh /start.sh  
ADD files/shutdown.sh /shutdown.sh  
ADD files/update_check.sh /update_check.sh  
  
# Copy the default server config in place  
ADD files/default.serverconfig.xml /default.serverconfig.xml  
  
# Expose necessary ports  
EXPOSE 26900  
EXPOSE 25000  
EXPOSE 25001  
EXPOSE 25002  
EXPOSE 25003  
EXPOSE 8080  
EXPOSE 8081  
# Setup default environment variables for the server  
ENV SEVEN_DAYS_TO_DIE_SERVER_STARTUP_ARGUMENTS
"-configfile=server_data/serverconfig.xml -logfile /dev/stdout -quit
-batchmode -nographics -dedicated"  
ENV SEVEN_DAYS_TO_DIE_TELNET_PORT 8081  
ENV SEVEN_DAYS_TO_DIE_TELNET_PASSWORD ""  
ENV SEVEN_DAYS_TO_DIE_START_MODE "0"  
ENV SEVEN_DAYS_TO_DIE_UPDATE_CHECKING "0"  
ENV SEVEN_DAYS_TO_DIE_UPDATE_BRANCH "public"  
ADD files/serverconfig.py /serverconfig.py  
  
# Start the server  
ENTRYPOINT ["./start.sh"]  

