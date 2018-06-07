# HPE IDOL is a commercial software from Hewlett Packard Enterprise
Development LP.  
# To run this docker image you will need a valid license from Hewlett Packard
Enterprise.  
# Here we don't provide a valid license. If you want to run it, please contact
us as registerd partner from HPE at hi@yuntaz.com.  
# Restricted Rights Legend: Confidential computer software. Valid license from
HPE required for possession, use or copying.  
# Consistent with FAR 12.211 and 12.212, Commercial Computer Software,
Computer Software Documentation, and  
# Technical Data for Commercial Items are licensed to the U.S. Government
under vendor's standard commercial license.  
# Copyright Notice  
FROM centos:7  
MAINTAINER Yuntaz <docker@yuntaz.com>  
ENV LANG en_US.utf8  
ENV TZ UTC  
ENV SHELL "/bin/bash"  
ENV container docker  
  
# Setting up ARG and ENV variables  
ARG LICENSE_FILE_URL=http://downloads.yuntaz.com/docker/licensekey.dat  
ENV LICENSE_FILE ${LICENSE_FILE_URL}  
  
ARG TEST_FILE_URL=http://downloads.yuntaz.com/docker/test.idx  
ENV TEST_FILE ${TEST_FILE_URL}  
  
ARG IDOL_TAR_URL=http://downloads.yuntaz.com/docker/idol_11.4.0.tar.gz  
ENV IDOL_TAR ${IDOL_TAR_URL}  
  
USER root  
WORKDIR /opt  
# Disable Firewall  
RUN systemctl mask firewalld && \  
systemctl disable firewalld  
# Update Centos7 and install packages for IDOL  
RUN yum -q -y update && \  
yum update tzdata && \  
yum install -y epel-release initscripts openssl which sudo bind bind-utils
net-tools wget  
# Add idol user and add it to the sudoers  
RUN useradd -ms /bin/bash idol && \  
echo "idol ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/idol && \  
chmod 0440 /etc/sudoers.d/idol && \  
echo "idol:idol!" | chpasswd  
# Download installation & uncompress it  
ADD $IDOL_TAR /opt  
ADD $TEST_FILE /opt  
RUN chmod 666 /opt/test.idx  
RUN chmod 666 idol_11.4.0.tar.gz && \  
tar xzvf idol_11.4.0.tar.gz && \  
chown -R idol:idol HewlettPackardEnterprise  
RUN rm -rf idol_11.4.0.tar.gz  
ADD $LICENSE_FILE
/opt/HewlettPackardEnterprise/IDOLServer-11.4.0/licenseserver/licensekey.dat  
WORKDIR /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/licenseserver  
RUN chown -R idol:idol * && \  
chmod 666 licensekey.dat && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/licenseserver/start-
licenseserver.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/licenseserver/stop-
licenseserver.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/agentstore/start-
agentstore.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/agentstore/stop-
agentstore.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/cfs/start-cfs.sh &&
\  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/cfs/stop-cfs.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/category/start-
category.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/category/stop-
category.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/community/start-
community.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/community/stop-
community.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/content/start-
content.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/content/stop-
content.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/view/start-view.sh
&& \  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/view/stop-view.sh &&
\  
chmod 774 /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/view/stop-view.sh &&
\  
chmod 774 /opt/HewlettPackardEnterprise/EductionSDK_11.4.0/bin/start-
eductionserver.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/EductionSDK_11.4.0/bin/stop-
eductionserver.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/Find/start-find.sh && \  
chmod 774 /opt/HewlettPackardEnterprise/Find/stop-find.sh  
# Add scripts as a commands  
WORKDIR /usr/bin  
RUN ln -s
/opt/HewlettPackardEnterprise/IDOLServer-11.4.0/SMC/scripts/smc_service.sh
smc_service && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/licenseserver/start-
licenseserver.sh start-licenseserver && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/licenseserver/stop-
licenseserver.sh stop-licenseserver && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/agentstore/start-
agentstore.sh start-agentstore && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/agentstore/stop-
agentstore.sh stop-agentstore && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/cfs/start-cfs.sh start-
cfs && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/cfs/stop-cfs.sh stop-cfs
&& \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/community/start-
community.sh start-community && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/community/stop-
community.sh stop-community && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/category/start-
category.sh start-category && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/category/stop-
category.sh stop-category && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/content/start-content.sh
start-content && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/content/stop-content.sh
stop-content && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/view/start-view.sh
start-view && \  
ln -s /opt/HewlettPackardEnterprise/IDOLServer-11.4.0/view/stop-view stop-view
&& \  
ln -s /opt/HewlettPackardEnterprise/EductionSDK_11.4.0/bin/start-
eductionserver.sh start-eductionserver && \  
ln -s /opt/HewlettPackardEnterprise/EductionSDK_11.4.0/bin/stop-
eductionserver.sh stop-eductionserver && \  
ln -s /opt/HewlettPackardEnterprise/Find/start-find.sh start-find && \  
ln -s /opt/HewlettPackardEnterprise/Find/stop-find.sh stop-find  
# Find  
WORKDIR /opt  
RUN wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/8u144-b01/090f390dda5b47b9b721c7dfaa008135/jdk-8u144-linux-x64.rpm
-O /opt/jdk-8u144-linux-x64.rpm && \  
yum -y install /opt/jdk-8u144-linux-x64.rpm && \  
rm -f /opt/jdk-8u144-linux-x64.rpm  
# Entrypoint  
ENTRYPOINT ["/home/idol/docker-entrypoint.sh"]  
ADD ./docker-entrypoint.sh /home/idol/  
RUN chown -R idol:idol /home/idol && \  
chmod +x /home/idol/docker-entrypoint.sh  
USER idol  
WORKDIR /home/idol  
EXPOSE 7000 17000 7025 17025 7026 17026 7027 17027 7028 17028 7029 17029 9020
9022 9030 9050 9080 9100 9101 9102 8080 20000 13000 13002

