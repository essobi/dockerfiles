FROM mswinarski/atlassian-base:1.8  
MAINTAINER Maciej Swinarski, mswinarski@atlassian.com  
  
ENV LANG C.UTF-8  
ENV FECRU_VERSION 4.4.0  
ENV FISHEYE_HOME /atlassian/apps/fisheye  
ENV FISHEYE_INST /atlassian/data/fisheye  
ENV FISHEYE_OPTS -Dfecru.configure.from.env.variables=true  
  
# FishEye configuration from environment variables  
# ENV FECRU_CONFIGURE_LICENSE_FISHEYE=  
# ENV FECRU_CONFIGURE_LICENSE_CRUCIBLE=  
# ENV FECRU_CONFIGURE_ADMIN_PASSWORD=  
# ENV FECRU_CONFIGURE_DB_TYPE=  
# ENV FECRU_CONFIGURE_DB_HOST=  
# ENV FECRU_CONFIGURE_DB_PORT=  
# ENV FECRU_CONFIGURE_DB_NAME=  
# ENV FECRU_CONFIGURE_DB_USER=  
# ENV FECRU_CONFIGURE_DB_PASSWORD=  
# ENV FECRU_CONFIGURE_DB_MIN_POOL_SIZE=  
# ENV FECRU_CONFIGURE_DB_MAX_POOL_SIZE=  
RUN echo "Atlassian - FishEye ${FECRU_VERSION} applications runtime
environment"  
  
WORKDIR /atlassian/apps  
  
# download and install fisheye to /atlassian/apps/fisheye  
ADD
http://www.atlassian.com/software/fisheye/downloads/binary/fisheye-${FECRU_VERSION}.zip
/atlassian/apps/  
  
RUN unzip fisheye-${FECRU_VERSION}.zip && rm fisheye-${FECRU_VERSION}.zip  
RUN mv fecru-${FECRU_VERSION} fisheye  
RUN mkdir -p /atlassian/data/fisheye  
  
ADD configure.sh ${FISHEYE_HOME}/  
RUN chmod +x ${FISHEYE_HOME}/configure.sh  
ADD start.sh ${FISHEYE_HOME}/  
RUN chmod +x ${FISHEYE_HOME}/start.sh  
  
VOLUME ${FISHEYE_INST}  
  
EXPOSE 8080  
WORKDIR ${FISHEYE_HOME}/  
  
CMD ["./start.sh"]  

