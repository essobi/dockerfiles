FROM docker.io/centos:7  
MAINTAINER Simon 1905 <simbo@x.com>  
  
### Install shiny as per instructions at:  
### https://www.rstudio.com/products/shiny/download-server/  
RUN yum -y update && yum -y install epel-release wget && yum -y install R &&
yum clean all  
RUN su - -c "R -e \"install.packages(c('shiny', 'rmarkdown', 'devtools',
'RJDBC'), repos='http://cran.rstudio.com/')\""  
ENV R_SHINY_SERVER_VERSION 1.5.3.838  
RUN wget https://download3.rstudio.org/centos5.9/x86_64/shiny-
server-${R_SHINY_SERVER_VERSION}-rh5-x86_64.rpm && \  
yum -y install --nogpgcheck shiny-
server-${R_SHINY_SERVER_VERSION}-rh5-x86_64.rpm && yum clean all  
  
# custom config which users user 'default' set by openshift  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
## Configure default locale, see https://github.com/rocker-
org/rocker/issues/19  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
RUN mkdir -p /var/lib/shiny-server/bookmarks && \  
chown shiny:0 /var/lib/shiny-server/bookmarks && \  
chmod g+wrX /var/lib/shiny-server/bookmarks && \  
mkdir -p /var/log/shiny-server && \  
chown shiny:0 /var/log/shiny-server && \  
chmod g+wrX /var/log/shiny-server  
  
### Setup user for build execution and application runtime  
### https://github.com/RHsyseng/container-rhel-examples/blob/master/starter-
arbitrary-uid/Dockerfile.centos7  
ENV APP_ROOT=/opt/app-root  
ENV PATH=${APP_ROOT}/bin:${PATH} HOME=${APP_ROOT}  
COPY bin/ ${APP_ROOT}/bin/  
RUN chmod -R u+x ${APP_ROOT}/bin && \  
chgrp -R 0 ${APP_ROOT} && \  
chmod -R g=u ${APP_ROOT} /etc/passwd  
  
# openshift best practice is to use a number not a name this is user shiny  
USER 998  
### Wrapper to allow user name resolution openshift will actually use a random
user number so you need group permissions  
### https://github.com/RHsyseng/container-rhel-examples/blob/master/starter-
arbitrary-uid/Dockerfile.centos7  
ENTRYPOINT [ "uid_entrypoint" ]  
CMD run  

