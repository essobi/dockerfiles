FROM lsiobase/alpine.python:3.6  
MAINTAINER sparklyballs  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# set locale stuff  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# install pip packages  
RUN \  
pip install --no-cache-dir -U \  
comictagger \  
configparser \  
tzlocal && \  
  
# install app  
git clone https://github.com/evilhero/mylar.git /app/mylar && \  
  
git \--git-dir=/app/mylar/.git --work-tree=/app/mylar checkout development &&
\  
  
git -C /app/mylar pull && \  
  
# cleanup  
rm -rf \  
/root/.cache \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /comics /downloads  
EXPOSE 8090  
#Update1.5  

