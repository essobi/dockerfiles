FROM exoplatform/base-jdk:jdk8 AS install  
  
ARG CHAT_SERVER_VERSION=2.1.0-M07  
  
ENV GROUP_ID=org.exoplatform.addons.chat  
ENV ARTIFACT_ID=chat-standalone-server-tomcat-distrib  
  
COPY download.sh /  
RUN chmod u+x /download.sh && sync && /download.sh  
# COPY install.sh /  
# RUN chmod u+x /install.sh && /install.sh  
RUN cd /usr/local && unzip /chatserver.zip && mv chat-server-
standalone-${CHAT_SERVER_VERSION} chat-server  
  
FROM exoplatform/base-jdk:jdk8  
  
LABEL maintainer="eXo Platform <docker@exoplatform.com>"  
  
ENV EXO_USER=exo  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
# (we use 999 as uid like in official Docker images)  
RUN useradd --create-home -u 999 --user-group --shell /bin/bash ${EXO_USER}  
  
COPY \--from=install /usr/local/chat-server /usr/local/chat-server  
COPY bin/setenv.sh /usr/local/chat-server/bin/setenv-customize.sh  
RUN chmod u+x /usr/local/chat-server/bin/setenv-customize.sh  
  
EXPOSE 8080  
CMD [ "/usr/local/chat-server/start_chatServer.sh" ]  

