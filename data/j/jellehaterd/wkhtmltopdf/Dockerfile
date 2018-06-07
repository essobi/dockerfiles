FROM centos:7  
ARG WKHTMLTOPDF_VERSION=0.12.4  
ARG BASE_DIR="/data"  
ARG DIR_TO_WATCH="${BASE_DIR}/watching"  
ENV BASE_DIR=${BASE_DIR} \  
IR_TO_WATCH=${DIR_TO_WATCH} \  
RUNSCRIPT="/usr/local/bin/runscript" \  
LANG=en_US.utf8 \  
LC_ALL=en_US.utf8  
  
######################  
# Setup default user #  
######################  
ARG UID=1000  
ARG GID=1000  
ARG USERNAME=python  
ARG GROUPNAME=${USERNAME}  
RUN set -e \  
&& yum install -y sudo \  
&& yum clean all \  
&& echo "Defaults:${USERNAME} !env_reset" >> /etc/sudoers \  
&& echo "Defaults:${USERNAME} !requiretty" >> /etc/sudoers \  
&& echo "Defaults:${USERNAME} secure_path=\"$PATH\"" >> /etc/sudoers \  
&& echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \  
&& groupadd -r -g ${GID} ${GROUPNAME} \  
&& useradd -r -m -d ${BASE_DIR} -u ${UID} -g ${GROUPNAME} -s /bin/bash
${USERNAME}  
ENV UID=${UID} \  
GID=${GID} \  
USERNAME=${USERNAME} \  
GROUPNAME=${GROUPNAME}  
  
RUN yum -y install epel-release && \  
yum -y update && \  
yum -y install \  
xz \  
libXrender \  
libXext \  
fontconfig \  
xorg-x11-fonts-75dpi \  
xorg-x11-fonts-Type1 \  
python-pip && \  
yum -y clean all && \  
rm -rf /var/cache/yum  
  
ADD
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/${WKHTMLTOPDF_VERSION}/wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-
generic-amd64.tar.xz /tmp/wkhtmltopdf/  
  
RUN cd /tmp/wkhtmltopdf && \  
unxz /tmp/wkhtmltopdf/wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-generic-
amd64.tar.xz && \  
tar -xvf /tmp/wkhtmltopdf/wkhtmltox-${WKHTMLTOPDF_VERSION}_linux-generic-
amd64.tar && \  
mv /tmp/wkhtmltopdf/wkhtmltox/bin/* /usr/local/bin/ && \  
rm -rf /tmp/wkhtmltopdf  
  
WORKDIR ${DIR_TO_WATCH}  
  
COPY docker-entrypoint.sh /usr/local/sbin/entrypoint.sh  
COPY runscript.py ${RUNSCRIPT}  
  
RUN pip install watchdog && \  
mkdir -p ${DIR_TO_WATCH} && \  
chown -R ${UID}:${GID} ${RUNSCRIPT} && \  
chmod +x ${RUNSCRIPT}  
  
ENTRYPOINT ["entrypoint.sh", "runscript"]  
  
CMD ["--encoding", "utf-8", "--load-error-handling", "ignore"]

