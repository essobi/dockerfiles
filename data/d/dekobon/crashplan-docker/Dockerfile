FROM ubuntu:xenial  
  
ENV CRASHPLAN_VERSION 5.4.1  
ENV CRASHPLAN_MD5_CHECKSUM f1afae0de352b385f24367ae84c5fee8  
ENV ZULE_JCE_POLICY_CHECKSUM ebe83e1bf25de382ce093cf89e93a944  
ENV JAVA_HOME /usr/lib/jvm/zulu-8-amd64  
  
# Installed tools:  
#
==============================================================================  
# curl: for downloading binaries  
# ca-certifiactes: for downloading via https  
# zulu-8 OpenJDK certified by Azul  
# libnss3 Native crypto tools for improving JVM crypo performance  
# unzip: for installing binaries  
# dc: for calculating performance settings  
#
==============================================================================  
# Adds Azul Zulu OpenJDK repository  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
0x219BD9C9 && \  
echo 'deb http://repos.azulsystems.com/ubuntu stable main' >
/etc/apt/sources.list.d/zulu.list  
  
# Install system utilities and Java  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -qy upgrade && \  
apt-get install --no-install-recommends -qy \  
curl ca-certificates zulu-8 libjna-java unzip libnss3 dc && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# Install Java Cryptography Extension Kit  
RUN curl --retry 6 -Ls
"http://www.azulsystems.com/sites/default/files/images/ZuluJCEPolicies.zip" >
/tmp/ZuluJCEPolicies.zip && \  
echo "${ZULE_JCE_POLICY_CHECKSUM} /tmp/ZuluJCEPolicies.zip" && \  
unzip -o -j /tmp/ZuluJCEPolicies.zip -d $JAVA_HOME/jre/lib/security
ZuluJCEPolicies/US_export_policy.jar ZuluJCEPolicies/local_policy.jar && \  
rm /tmp/ZuluJCEPolicies.zip  
  
# Add Native cryptography support via libnss and PKCS11  
COPY etc /etc  
COPY usr /usr  
  
# Install Crashplan Server  
RUN export DEBIAN_FRONTEND=noninteractive && \  
curl --retry 6 -Ls
"https://download.code42.com/installs/proserver/${CRASHPLAN_VERSION}/Code42server_${CRASHPLAN_VERSION}_Linux.tgz"
> /tmp/crashplan.tar.gz && \  
echo "${CRASHPLAN_MD5_CHECKSUM} /tmp/crashplan.tar.gz" | md5sum -c && \  
tar -xz -C /tmp -f /tmp/crashplan.tar.gz && \  
cd /tmp/Code42server_${CRASHPLAN_VERSION}_Linux && \  
./install.sh -u --accept-eula && \  
cd / && \  
rm -rf /tmp/crashplan.tar.gz /tmp/Code42server_${CRASHPLAN_VERSION}_Linux  
  
COPY opt/proserver/bin /opt/proserver/bin  
  
RUN chmod +x /usr/local/bin/proclimit && \  
chmod +x /opt/proserver/bin/proserver-foreground  
  
CMD [ "/opt/proserver/bin/proserver-foreground" ]  
  
EXPOSE 4280  
EXPOSE 4282  
EXPOSE 4285  
EXPOSE 4287  

