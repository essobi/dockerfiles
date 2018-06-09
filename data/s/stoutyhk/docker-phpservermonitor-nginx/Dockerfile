FROM linuxserver/nginx  
  
# set version label  
# ARG BUILD_DATE  
# ARG VERSION  
# LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
LABEL maintainer="stoutyhk"  
# environment settings  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
  
EXPOSE 80 443  
  
# add local files  
COPY root/ /  
  
VOLUME /config  

