# Version: 0.0.2  
# Apache Nifi Sensor pipeline  
FROM centos:centos7  
  
MAINTAINER Yury Kavaliou <yury_kavaliou@epam.com>  
  
ENV NIFI_DISTR http://mirror.cc.columbia.edu/pub/software/apache/nifi  
ENV NIFI_HOME /opt/nifi  
ENV NIFI_VERSION 0.4.1  
ENV NIFI_SCRIPTS /opt/nifi/sensor  
  
RUN yum install -y java-1.8.0-openjdk-devel tar  
RUN mkdir -p /opt/nifi  
RUN mkdir -p ${NIFI_SCRIPTS}  
RUN curl ${NIFI_DISTR}/${NIFI_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz | tar
xvz -C ${NIFI_HOME} \--strip-components=1  
RUN sed -i -e "s|^nifi.ui.banner.text=.*$|nifi.ui.banner.text=IOT Sensor -
Nifi ${NIFI_VERSION}|" ${NIFI_HOME}/conf/nifi.properties  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
RUN pip install requests  
  
# Copy additional files  
COPY ./files/start.sh ${NIFI_SCRIPTS}/start.sh  
COPY ./files/ipso.py ${NIFI_SCRIPTS}/ipso.py  
COPY ./files/filtering.py ${NIFI_SCRIPTS}/filtering.py  
COPY ./files/outputstream.py ${NIFI_SCRIPTS}/outputstream.py  
COPY ./files/leshan_poller.py ${NIFI_SCRIPTS}/leshan_poller.py  
COPY ./files/leshan.cfg ${NIFI_SCRIPTS}/leshan.cfg  
  
RUN mkdir -p ${NIFI_SCRIPTS}/app && \  
mkdir -p ${NIFI_SCRIPTS}/app/conf && mkdir -p ${NIFI_SCRIPTS}/app/handlers  
COPY ./files/app/controller.py ${NIFI_SCRIPTS}/app/controller.py  
  
# Copy templates  
COPY ./files/nifi-tpl/SensorPipeline.xml
${NIFI_HOME}/conf/templates/1d4dfd36-c513-434e-bce4-13245559a514.template  
COPY ./files/nifi-tpl/ListenHandlers.xml
${NIFI_HOME}/conf/templates/4166652a-735a-43aa-a8bf-20cba9eea397.template  
  
RUN chmod +x ${NIFI_SCRIPTS}/filtering.py ${NIFI_SCRIPTS}/outputstream.py
${NIFI_SCRIPTS}/leshan_poller.py ${NIFI_SCRIPTS}/start.sh
${NIFI_SCRIPTS}/app/controller.py  
  
ENTRYPOINT ["bash", "/opt/nifi/sensor/start.sh"]  
  
# Expose web port (nifi ui)  
# 8090 - ui, 8088 - http listener (endpoint: contentListener)  
EXPOSE 8090 8088  

