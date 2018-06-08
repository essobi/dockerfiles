FROM patricol/node:17.10  
USER root  
  
RUN npm install --unsafe-perm -g \  
firebase \  
firebase-tools \  
react \  
react-dom \  
material-ui \  
react-tap-event-plugin  
  
#COPY --chown=user:user extras/login.sh /home/user/#Not yet supported by
docker hub's automated builds, which use an outdated version of docker.  
COPY extras/login.sh /home/user/  
RUN chmod +x /home/user/login.sh && \  
chown -R user:user /home/user/login.sh  
  
USER user

