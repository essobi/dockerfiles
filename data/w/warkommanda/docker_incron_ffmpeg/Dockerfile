FROM debian:latest  
MAINTAINER Manuel Mueller  
  
# __ __ __ .__  
#/ \ / \\_____ _/ |_ ____ | |__ _____ ____  
#\ \/\/ /\\__ \\\ __\/ ___\| | \ / \\_/ __ \  
#\ / / __ \| | \ \\___| Y \ Y Y \ ___/  
# \\__/\ / (____ /__| \\___ >___| /__|_| /\\___ >  
# \/ \/ \/ \/ \/ \/  
# get base  
RUN apt-get update && apt-get upgrade -y  
  
# get essentials  
RUN apt-get -y install git nano ffmpeg incron rsyslog task-spooler  
  
# don't you rootizle me  
RUN echo "root" >> /etc/incron.allow  
  
##################################  
# Base Section Start  
##################################  
# add the convert script  
COPY convert.sh /opt/convertscript/  
RUN chmod +x /opt/convertscript/convert.sh  
COPY incrontab.txt /opt/convertscript/  
RUN incrontab /opt/convertscript/incrontab.txt -f  
  
# create the watch directory  
RUN mkdir /home/fileconversion  
RUN mkdir /home/output  
  
# Run services  
COPY start.sh /  
RUN chmod +x /start.sh  
CMD /start.sh  

