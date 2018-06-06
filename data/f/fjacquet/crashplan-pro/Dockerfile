#  
# crashplan-pro Dockerfile  
#  
# https://github.com/fjacquet/docker-crashplan-pro  
#  
FROM ubuntu:bionic  
# Metadata.  
LABEL \  
org.label-schema.name="crashplan-pro" \  
org.label-schema.description="Docker container for CrashPlan PRO" \  
org.label-schema.version="unknown" \  
org.label-schema.vcs-url="https://github.com/fjacquet/crashplan-pro" \  
org.label-schema.schema-version="1.0"  
  
# Define software versions  
ARG CRASHPLANPRO_VERSION=6.7.1  
ARG CRASHPLANPRO_TIMESTAMP=1512021600671  
ARG CRASHPLANPRO_BUILD=4615  
# Define software download URLs  
ARG CRASHPLANPRO_URL=https://web-eam-
msp.crashplanpro.com/client/installers/CrashPlanSmb_${CRASHPLANPRO_VERSION}_${CRASHPLANPRO_TIMESTAMP}_${CRASHPLANPRO_BUILD}_Linux.tgz  
# Define container build variables  
ARG TARGETDIR=/usr/local/crashplan  
# Define mountable directories.  
VOLUME ["/config"]  
VOLUME ["/volume1"]  
EXPOSE 6080  
COPY crashplan-pro.sh /crashplan-pro.sh  
COPY startup.sh /startup.sh  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APP_NAME="CrashPlan for Small Business"  
ENV KEEP_APP_RUNNING=1  
ENV CRASHPLAN_DIR="${TARGETDIR}"  
ENV JAVACOMMON="${TARGETDIR}/jre/bin/java"  
ENV PATH="${TARGETDIR}/electron/:${PATH}"  
ENV USER_ID=1021  
ENV GROUP_ID=101  
WORKDIR /root  
  
RUN \  
chmod 0755 /startup.sh && \  
apt-get update -y && \  
apt-get install -y git x11vnc python python-numpy unzip xvfb openbox cpio curl
sed libgconf2-4 net-tools openjdk-8-jdk && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone "https://github.com/kanaka/noVNC.git"  
WORKDIR /root/noVNC/utils  
RUN git clone "https://github.com/kanaka/websockify" websockify  
  
WORKDIR /tmp  
# Installing CrashPlanSmb_${CRASHPLANPRO_VERSION}...  
RUN \  
curl -# -L "${CRASHPLANPRO_URL}" | tar -xz && \  
mkdir -p "${TARGETDIR}"  
  
# Installing JRE...  
RUN . "/tmp/crashplan-install/install.defaults" && \  
curl -# -L "$JRE_X64_DOWNLOAD_URL" | tar -xz -C "$TARGETDIR" && \  
chown -R root:root "$TARGETDIR/jre"  
  
WORKDIR /usr/local/crashplan  
  
RUN mv "/tmp/crashplan-install/CrashPlanSmb_${CRASHPLANPRO_VERSION}.cpi"
"/tmp/crashplan-install/CrashPlanSmb_${CRASHPLANPRO_VERSION}.cpio.gz" && \  
gunzip "/tmp/crashplan-install/CrashPlanSmb_${CRASHPLANPRO_VERSION}.cpio.gz"
&& \  
cpio -i --verbose --no-preserve-owner < "/tmp/crashplan-
install/CrashPlanSmb_${CRASHPLANPRO_VERSION}.cpio" && \  
mv "${TARGETDIR}/app.asar" "${TARGETDIR}/electron/resources" && \  
chmod 755 "${TARGETDIR}/electron/crashplan"  
  
RUN \  
mv "${TARGETDIR}/conf" /etc/conf && \  
cp /tmp/crashplan-install/scripts/run.conf /etc && \  
sed -i '/<orgType>BUSINESS<\/orgType>/a
\\\t<serviceUIConfig>\n\t\t<serviceHost>127.0.0.1<\/serviceHost>\n\t<\/serviceUIConfig>'
/etc/conf/default.service.xml && \  
sed -i
's|<backupConfig>|<backupConfig>\n\t\t\t<manifestPath>/usr/local/var/crashplan</manifestPath>|g'
/etc/conf/default.service.xml && \  
mkdir -p /usr/local/var/crashplan && \  
rm -r /usr/local/crashplan/upgrade && \  
touch /usr/local/crashplan/upgrade && chmod 400 /usr/local/crashplan/upgrade
&& \  
ln -s /config/conf "${TARGETDIR}/conf" && \  
ln -s /config/bin/run.conf "${TARGETDIR}/bin/run.conf" && \  
ln -s /config/cache "${TARGETDIR}/cache" && \  
rm -r "${TARGETDIR}/log" && \  
ln -s /config/log "${TARGETDIR}/log" && \  
ln -s /config/var /var/lib/crashplan && \  
ln -s /config/repository/metadata /usr/local/crashplan/metadata && \  
sed -i '/^nobody:/d' /etc/passwd && \  
sed -i '/^nobody:/d' /etc/group && \  
sed -i '/^nobody:/d' /etc/shadow && \  
echo > /etc/fstab && \  
rm /etc/machine-id && \  
ln -s /config/machine-id /etc/machine-id && \  
echo "${CRASHPLANPRO_VERSION}" > /etc/cp_version && \  
rm -rf "/tmp/*"  
  
CMD ["/startup.sh"]

