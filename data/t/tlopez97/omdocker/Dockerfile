FROM frett27/xvfbssh:latest  
  
LABEL Maintainer="Tomas Antonio Lopez (tomasantonio97@gmail.com)" \  
Version="1.0" \  
Description="Backend Docker image for OMdocker containerized app" \  
"Upstream repository"="https://github.com/tal357/omdocker-backend"  
  
#Install utility packages for locale generation, password generation and repo
configuration  
RUN apt-get update && \  
apt-get install -y locales \  
pwgen \  
lsb-release  
  
#Set and generate locale  
ENV LOCALE_SETUP en_US.UTF-8  
RUN locale-gen "$LOCALE_SETUP"  
  
#Copy scripts from the scripts/ directory into /usr/local/bin  
COPY scripts /usr/local/bin/  
  
#Enable execution for the following scripts:  
## 1. SSH key regeneration;  
## 2. user password generation and setup;  
## 3. repositories configuration  
RUN chmod 500 /usr/local/bin/key_regen.sh &&\  
chmod 500 /usr/local/bin/passgen.sh &&\  
chmod 550 /usr/local/bin/repoconf.sh;  
  
#Add the Open Modelica repositories to the database  
RUN ["/usr/local/bin/repoconf.sh"]  
  
#Refresh package database and install the OM software  
RUN apt-get update && apt-get install -y openmodelica  
  
#Set environment variables for X and init script  
ENV DISPLAY=0 \  
SCREEN=0 \  
DISPLAY_MODE=1024x768x16  
  
EXPOSE 22/tcp  
  
ENTRYPOINT ["/usr/local/bin/xvfbssh.sh"]  

