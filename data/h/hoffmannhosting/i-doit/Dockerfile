FROM debian:latest  
  
RUN apt-get update  
RUN apt-get install -y wget systemd  
RUN wget https://raw.githubusercontent.com/bheisig/i-doit-
scripts/master/idoit-install.sh  
RUN chmod 755 idoit-install.sh  
RUN ./idoit-install.sh  

