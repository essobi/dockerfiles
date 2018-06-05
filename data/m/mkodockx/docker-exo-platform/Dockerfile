FROM exoplatform/ubuntu-jdk7-exo:plf-4.1  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
# mongodb setup  
USER root  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' \  
| sudo tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get -qq update && \  
apt-get -qq -y install mongodb-org && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y autoclean  
  
# eXo addons  
USER exo  
# first management  
#RUN ${EXO_APP_DIR}/current/addon install exo-addons-manager:1.0.0  
# other addons  
RUN ${EXO_APP_DIR}/current/addon install exo-chat-community  
#RUN ${EXO_APP_DIR}/current/addon install exo-answers  
#RUN ${EXO_APP_DIR}/current/addon install exo-responsive-addon  
#RUN ${EXO_APP_DIR}/current/addon install exo-cloud-drive:1.2.0-RC2  
#RUN ${EXO_APP_DIR}/current/addon install exo-staging-extension  
#RUN ${EXO_APP_DIR}/current/addon install exo-exchange-extension  
#RUN ${EXO_APP_DIR}/current/addon install exo-maintenance-warning  
#RUN ${EXO_APP_DIR}/current/addon install exo-bonita-extension  
#RUN ${EXO_APP_DIR}/current/addon install exo-ide-addon  
#RUN ${EXO_APP_DIR}/current/addon install exo-mobile-notifications  
#RUN ${EXO_APP_DIR}/current/addon install exo-video-calls  
#RUN ${EXO_APP_DIR}/current/addon install exo-wiki-macro-video  
#RUN ${EXO_APP_DIR}/current/addon install exo-remote-edit  
# mongodb then eXo  
RUN mv ${EXO_APP_DIR}/current/start_eXo.sh ${EXO_APP_DIR}/current/start_eXo-
ORI.sh  
ADD start_eXo.sh ${EXO_APP_DIR}/current/start_eXo.sh  
USER root  
RUN chmod 775 ${EXO_APP_DIR}/current/start_eXo.sh  
RUN chown -R ${EXO_USER}:${EXO_GROUP} ${EXO_APP_DIR}/current/start_eXo.sh  

