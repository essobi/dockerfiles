# This image is layered from SCL centos7 openshift postgresql 9.5  
# https://github.com/sclorg/postgresql-container/tree/master/9.5  
FROM centos/postgresql-95-centos7:9.5  
MAINTAINER ManageIQ https://github.com/ManageIQ/manageiq-appliance-build  
  
ENV CONTAINER_SCRIPTS_ROOT=/opt/manageiq/container-scripts/ \  
START_HOOKS_DIR=/opt/app-root/src/postgresql-start/  
  
# Switch USER to root to add required repo and packages  
USER root  
  
# Fetch MIQ repo for pglogical and repmgr packages  
RUN curl -sSLko /etc/yum.repos.d/manageiq-ManageIQ-Master-epel-7.repo \  
https://copr.fedorainfracloud.org/coprs/manageiq/ManageIQ-
Master/repo/epel-7/manageiq-ManageIQ-Master-epel-7.repo  
  
RUN yum -y --setopt=tsflags=nodocs install rh-postgresql95-postgresql-
pglogical \  
rh-postgresql95-repmgr && \  
yum clean all  
  
# Add pglogical openshift tag to new image  
LABEL io.openshift.tags="database,postgresql,postgresql95,rh-
postgresql95,pglogical"  
  
ADD container-assets/container-scripts ${CONTAINER_SCRIPTS_ROOT}  
ADD container-assets/on-start.sh ${START_HOOKS_DIR}  
  
# Loosen permission bits to avoid problems running container with arbitrary
UID  
RUN /usr/libexec/fix-permissions /var/lib/pgsql && \  
/usr/libexec/fix-permissions /var/run/postgresql  
  
# Switch USER back to postgres  
USER 26  

