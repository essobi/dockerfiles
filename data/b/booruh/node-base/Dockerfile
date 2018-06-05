FROM node:8.11.1  
RUN apt-get update  
RUN apt-get -y install logrotate  
  
# Assemble a dictionary file for machine names.  
RUN apt-get -y install wbritish-insane unaccent  
RUN cat /usr/share/dict/words \  
| unaccent utf-8 \  
| tr A-Z a-z \  
| sed "s/'s$//" \  
| grep '^.\\{,7\\}$' \  
| grep '^.\\{5,\\}$' \  
| uniq > /usr/share/dict/machine_names  
RUN apt-get -y remove unaccent wbritish-insane  
  
# Update NPM.  
RUN npm i -g npm@^5.7.1  
  
# Node process monitor.  
RUN npm i -g pm2@^2.10.3  
  
# Papertrail deps.  
RUN wget -q
https://github.com/papertrail/remote_syslog2/releases/download/v0.20/remote-
syslog2_0.20_amd64.deb  
RUN dpkg -i remote-syslog2_0.20_amd64.deb  
RUN rm remote-syslog2_0.20_amd64.deb  
  
RUN apt-get -f install  
RUN apt-get -y autoremove  
  
CMD ['']  

