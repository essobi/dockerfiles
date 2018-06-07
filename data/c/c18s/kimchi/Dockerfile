FROM centos:7 as builder  
  
ENV WORKDIR /opt/kimchi  
WORKDIR ${WORKDIR}  
  
ARG GIT_BRANCH=master  
ARG PLUGINS_DIR=${WORKDIR}/wok/src/wok/plugins  
ARG NOARCH=rpm/RPMS/noarch  
ARG DIST_DIR=${WORKDIR}/dist  
  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7 && yum
-y update  
RUN yum -y install gcc make autoconf automake gettext-devel git rpm-build
libxslt \  
bzip2 python-lxml  
  
RUN git clone \--recursive https://github.com/kimchi-project/wok.git  
  
RUN mkdir -p ${DIST_DIR}  
RUN cd ${WORKDIR}/wok \  
&& git checkout ${GIT_BRANCH} \  
&& git submodule update --remote \  
&& ./autogen.sh --system \  
&& make >/dev/null \  
&& make rpm >/dev/null \  
&& cp -v ${WORKDIR}/wok/${NOARCH}/wok-*.noarch.rpm
${DIST_DIR}/wok.el7.noarch.rpm  
  
RUN cd ${PLUGINS_DIR}/gingerbase \  
&& ./autogen.sh --system \  
&& make >/dev/null \  
&& make rpm >/dev/null \  
&& cp -v ${PLUGINS_DIR}/gingerbase/${NOARCH}/ginger-base-*.noarch.rpm \  
${DIST_DIR}/ginger-base.el7.noarch.rpm  
  
RUN cd ${PLUGINS_DIR}/ginger \  
&& ./autogen.sh --system \  
&& make >/dev/null \  
&& make rpm >/dev/null \  
&& cp -v ${PLUGINS_DIR}/ginger/${NOARCH}/ginger-*.noarch.rpm \  
${DIST_DIR}/ginger.el7.noarch.rpm  
  
RUN cd ${PLUGINS_DIR}/kimchi \  
&& ./autogen.sh --system \  
&& make >/dev/null \  
&& make rpm >/dev/null \  
&& cp -v ${PLUGINS_DIR}/kimchi/${NOARCH}/kimchi-*.noarch.rpm \  
${DIST_DIR}/kimchi.el7.noarch.rpm  
  
FROM centos:7  
ENV WORKDIR /opt/kimchi  
WORKDIR ${WORKDIR}  
  
COPY bin/. /usr/local/bin/  
COPY config/supervisord.conf /etc/supervisord.conf  
COPY \--from=builder /opt/kimchi/dist .  
  
EXPOSE 8001  
RUN docker-init  
  
CMD ["entrypoint"]  

