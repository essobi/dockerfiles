FROM centos:7  
MAINTAINER Naftuli Kay <me@naftuli.wtf>  
  
ENV CIRCLECI_USER=circleci  
ENV CIRCLECI_HOME=/home/${CIRCLECI_USER}  
  
# install epel  
RUN yum install -y epel-release >/dev/null && yum clean all  
  
# install devel packages  
RUN yum install -y sudo unzip git openssl-devel kernel-devel which make gcc
python-devel python34-devel python-pip \  
curl file autoconf automake cmake libtool libcurl-devel binutils-devel zlib-
devel wget xz-devel pkgconfig \  
bash-completion man-pages tree jq zip && \  
yum clean all  
  
# install and upgrade pip and utils  
RUN pip install --upgrade pip && pip install awscli  
  
# create sudo group and add sudoers config  
COPY conf/sudoers.d/50-sudo /etc/sudoers.d/  
RUN groupadd sudo  
  
# add ldconfig for /usr/local  
RUN echo '/usr/local/lib' > /etc/ld.so.conf.d/local.conf  
  
# create the user  
RUN adduser -G sudo -m ${CIRCLECI_USER}  
  
# deploy our tfenv command  
RUN install -o ${CIRCLECI_USER} -g ${CIRCLECI_USER} -m 0700 -d
${CIRCLECI_HOME}/.local ${CIRCLECI_HOME}/.local/bin  
COPY bin/tfenv ${CIRCLECI_HOME}/.local/bin  
RUN chmod 0755 ${CIRCLECI_HOME}/.local/bin/tfenv && \  
chown ${CIRCLECI_USER}:${CIRCLECI_USER} ${CIRCLECI_HOME}/.local/bin/tfenv  
  
# create circleci base dir  
RUN install -o ${CIRCLECI_USER} -g ${CIRCLECI_USER} -m 0700 -d
${CIRCLECI_HOME}/circleci  
  
USER ${CIRCLECI_USER}  
WORKDIR /home/${CIRCLECI_USER}/circleci  
  
CMD ["/bin/bash", "-l"]  

