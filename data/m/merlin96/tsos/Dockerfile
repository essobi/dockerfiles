FROM cqse/teamscale:4.0.5  
MAINTAINER Erkin Bapisch <erkin.bapisch@vkb.de>  
  
# Based on information of  
# https://docs.openshift.org/latest/creating_images/guidelines.html#openshift-
specific-guidelines  
# https://github.com/RHsyseng/container-rhel-examples/blob/master/starter-
arbitrary-uid/Dockerfile.centos7  
# https://github.com/elastic/elasticsearch-docker/issues/114  
# https://hub.docker.com/r/cqse/teamscale/  
### Setup user for build execution and application runtime  
# TODO Handle /backup folder, is created later  
USER root  
ENV APP_ROOT=/opt/teamscale  
ENV PATH=${APP_ROOT}/bin:${PATH} HOME=${APP_ROOT}  
COPY bin/ ${APP_ROOT}/bin/  
  
RUN chmod u+x ${APP_ROOT}/bin  
RUN chown teamscale:root ${APP_ROOT}/bin  
RUN chgrp 0 ${APP_ROOT}  
RUN mkdir /opt/teamscale/storage  
RUN chgrp 0 ${APP_ROOT}/storage  
RUN mkdir /opt/teamscale/logs  
RUN chgrp 0 ${APP_ROOT}/logs  
RUN chmod -R g=u ${APP_ROOT} /etc/passwd  
  
### Containers should NOT run as root as a good practice  
USER 1000  
WORKDIR ${APP_ROOT}  
### user name recognition at runtime w/ an arbitrary uid - for OpenShift
deployments  
ENTRYPOINT [ "uid_entrypoint" ]  
#VOLUME ${APP_ROOT}/logs ${APP_ROOT}/storage ${APP_ROOT}/config /backup  
EXPOSE 8080  
CMD run  

