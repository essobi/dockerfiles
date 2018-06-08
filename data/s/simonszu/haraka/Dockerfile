FROM node:latest  
  
USER node  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
ENV PATH=$PATH:/home/node/.npm-global/bin  
ENV HOSTNAME=haraka  
  
RUN npm -g install Haraka \  
&& npm -g install haraka-plugin-rspamd  
  
USER root  
# the application is not started as this user,  
# but Haraka can be configured to drop its privileges  
# via smtp.ini  
RUN mkdir /haraka && \  
groupadd -r haraka && \  
useradd --comment "Haraka Server User" \  
\--home /haraka \  
\--shell /bin/false \  
\--gid haraka \  
-r \  
-M \  
haraka \  
&& chown -R haraka:haraka /haraka  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
  
ENTRYPOINT ["/run.sh"]

