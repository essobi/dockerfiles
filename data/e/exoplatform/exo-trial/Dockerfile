# Dockerizing base image for eXo Platform with:  
#  
# - Libre Office  
# - MongoDB  
# - eXo Platform Trial edition  
# Build: docker build -t exoplatform/exo-trial .  
#  
# Run: docker run -p 8080:8080 exoplatform/exo-trial  
# docker run -d -p 8080:8080 exoplatform/exo-trial  
# docker run -d --rm -p 8080:8080 -v exo_trial:/srv exoplatform/exo-trial  
# docker run -d --rm -p 8080:8080 -v exo_trial_data:/srv -v
exo_trial_logs:/var/log/exo exoplatform/exo-trial  
FROM exoplatform/base-jdk:jdk8  
LABEL maintainer="eXo Platform <docker@exoplatform.com>"  
  
# Environment variables  
ENV EXO_VERSION 5.1.0-M07  
ENV MONGO_VERSION 3.4  
ENV MONGO_REPO_KEY 0C49F3730359A14518585931BC711F9BA15703C6  
  
ENV EXO_APP_DIR /opt/exo  
ENV EXO_CONF_DIR /etc/exo  
ENV EXO_DATA_DIR /srv/exo  
ENV EXO_LOG_DIR /var/log/exo  
ENV EXO_TMP_DIR /tmp/exo-tmp  
ENV MONGO_DATA_DIR /srv/mongodb  
  
ENV EXO_USER exo  
ENV EXO_GROUP ${EXO_USER}  
  
# Customise system  
RUN rm -f /bin/sh && ln -s /bin/bash /bin/sh  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
# and give him all rights  
RUN useradd --create-home --user-group --shell /bin/bash ${EXO_USER} \  
&& echo "exo ALL = NOPASSWD: ALL" > /etc/sudoers.d/exo && chmod 440
/etc/sudoers.d/exo  
  
# Install some useful or needed tools  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
${MONGO_REPO_KEY} \  
&& echo "deb http://repo.mongodb.org/apt/ubuntu $(lsb_release -cs)/mongodb-
org/${MONGO_VERSION} multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-
org-${MONGO_VERSION}.list  
  
RUN apt-get -qq update \  
&& apt-get -qq -y upgrade ${_APT_OPTIONS} \  
&& apt-get -qq -y install ${_APT_OPTIONS} xmlstarlet \  
&& apt-get -qq -y install ${_APT_OPTIONS} libreoffice-calc libreoffice-draw
libreoffice-impress libreoffice-math libreoffice-writer \  
&& apt-get -qq -y install ${_APT_OPTIONS} mongodb-org-server mongodb-org-shell
\  
&& apt-get -qq -y autoremove \  
&& apt-get -qq -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Create needed directories  
RUN mkdir -p ${EXO_DATA_DIR} && chown ${EXO_USER}:${EXO_GROUP} ${EXO_DATA_DIR}
\  
&& mkdir -p ${EXO_TMP_DIR} && chown ${EXO_USER}:${EXO_GROUP} ${EXO_TMP_DIR} \  
&& mkdir -p ${EXO_LOG_DIR} && chown ${EXO_USER}:${EXO_GROUP} ${EXO_LOG_DIR} \  
&& mkdir -p ${MONGO_DATA_DIR} && chown mongodb:mongodb ${MONGO_DATA_DIR}  
# && mkdir ${EXO_DATA_DIR}/.eXo/ && chown ${EXO_USER}:${EXO_GROUP}
${EXO_DATA_DIR}/.eXo \  
# && ln -s ${EXO_DATA_DIR}/.eXo /home/${EXO_USER}/.eXo \  
# Install eXo Platform  
RUN EXO_VERSION_SHORT=$(echo ${EXO_VERSION} | awk -F "\\." '{ print
$1"."$2}'); \  
DOWNLOAD_URL="https://downloads.exoplatform.org/public/releases/platform/${EXO_VERSION_SHORT}/${EXO_VERSION}/platform-
trial-${EXO_VERSION}.zip"; \  
curl -L -o /srv/downloads/eXo-Platform-trial-${EXO_VERSION}.zip
${DOWNLOAD_URL} \  
&& unzip -q /srv/downloads/eXo-Platform-trial-${EXO_VERSION}.zip -d
/srv/downloads/ \  
&& rm -f /srv/downloads/eXo-Platform-trial-${EXO_VERSION}.zip \  
&& mv /srv/downloads/platform-${EXO_VERSION}-trial ${EXO_APP_DIR} \  
&& chown -R ${EXO_USER}:${EXO_GROUP} ${EXO_APP_DIR} \  
&& ln -s ${EXO_APP_DIR}/gatein/conf /etc/exo \  
&& rm -rf ${EXO_APP_DIR}/logs && ln -s ${EXO_LOG_DIR} ${EXO_APP_DIR}/logs  
  
USER ${EXO_USER}  
RUN for a in ${ADDONS}; do echo "Installing addon $a"; /opt/exo/addon install
$a; done  
USER root  
  
# Install Docker customization file  
ADD scripts/setenv-docker-customize.sh ${EXO_APP_DIR}/bin/setenv-docker-
customize.sh  
RUN chmod 755 ${EXO_APP_DIR}/bin/setenv-docker-customize.sh \  
&& chown ${EXO_USER}:${EXO_USER} ${EXO_APP_DIR}/bin/setenv-docker-customize.sh
\  
&& sed -i '/# Load custom settings/i \  
\\# Load custom settings for docker environment\n\  
[ -r "$CATALINA_BASE/bin/setenv-docker-customize.sh" ] && { \n\  
source $CATALINA_BASE/bin/setenv-docker-customize.sh \n\  
if [ $? != 0 ]; then \n\  
echo "Problem during docker customization process ... startup aborted !" \n\  
exit 1 \n\  
fi \n\  
} || echo "No Docker eXo Platform customization file :
$CATALINA_BASE/bin/setenv-docker-customize.sh"\n\  
' ${EXO_APP_DIR}/bin/setenv.sh \  
&& grep 'setenv-docker-customize.sh' ${EXO_APP_DIR}/bin/setenv.sh  
  
COPY scripts/wait-for-it.sh /opt/wait-for-it.sh  
RUN chmod 755 /opt/wait-for-it.sh \  
&& chown ${EXO_USER}:${EXO_GROUP} /opt/wait-for-it.sh  
  
# Add Configuration files  
RUN mkdir /etc/service/mongod  
RUN mkdir /etc/service/exo  
  
ADD conf/mongod.conf /etc/mongod.conf  
ADD conf/mongod.sh /etc/service/mongod/run  
ADD conf/exo.sh /etc/service/exo/run  
#ADD conf/chat.properties /etc/exo/chat.properties  
RUN chmod +x /etc/service/mongod/run  
RUN chmod +x /etc/service/exo/run  
  
EXPOSE 8080  
WORKDIR "/opt/exo/"  
VOLUME ["/srv"]  

