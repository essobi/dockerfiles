FROM binarybabel/oracle-jdk:8-alpine  
  
# ____ ____ _________ __  
# |_ _||_ _| | _ _ | [ | _  
# \ \ / / .--. __ _|_/ | | \\_|_ .--. ,--. .---. | | / ]  
# \ \/ // .'`\ \\[ | | | | | [ `/'`\\]`'_\ : / /'`\\] | '' <  
# _| |_| \\__. | | \\_/ |, _| |_ | | // | |,| \\__. | |`\ \  
# |______|'.__.' '.__.'_/|_____| [___] \'-;__/'.___.'[__| \\_]  
ENV APP_DIR=/youtrack DATA_DIR=/youtrack-data JAVA_XMX=1024m  
WORKDIR ${APP_DIR}  
VOLUME ${DATA_DIR}  
EXPOSE 8080  
#COPY youtrack.jar ${APP_DIR}/youtrack.jar  
ENV YOUTRACK_VERSION=2018.2.42223  
RUN
YOUTRACK_DOWNLOAD="https://download.jetbrains.com/charisma/youtrack-${YOUTRACK_VERSION:-$(curl
-s https://lv.binarybabel.org/catalog-api/youtrack/latest.txt?p=version)}.jar"
\  
&& echo Downloading ${YOUTRACK_DOWNLOAD} \  
&& curl -fsSLo youtrack.jar "${YOUTRACK_DOWNLOAD}"  
  
COPY docker-entrypoint.sh ${APP_DIR}  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD []  
  
# ------------------------------------------------------  
# Accept the Oracle License for all users of this image,  
# per Section C of the BCLA, permitting Oracle Java:  
# "(i) ... bundled as part of, and for the  
# sole purpose of running, your Programs"  
# ------------------------------------------------------  
ENV ACCEPT_ORACLE_BCLA=true  

