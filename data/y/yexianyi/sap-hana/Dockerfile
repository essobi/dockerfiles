# This docker file is for creating Opensuse42 + JDK1.8  
FROM yexianyi/oracle-jdk:opensuse42  
  
ARG SAP_HANA_VERSION=HANA_EXPRESS_20  
ARG
SAP_INSTALL_PACKAGE='https://mega.co.nz/#!5qhmGLpL!GRYnFEVeuDTCVDVZRmTBO1KjhfN2iJyMfLvcEIEvEXE'  
ARG SAP_INSTALL_FILE_NAME=hxe.tgz  
  
MAINTAINER Xianyi Ye <https://cn.linkedin.com/in/yexianyi>  
  
WORKDIR /home  
# Install essential components for installing SAP HANA  
RUN zypper addrepo
http://download.opensuse.org/repositories/network:utilities/openSUSE_Leap_42.2/network:utilities.repo
\  
&& zypper --non-interactive --gpg-auto-import-keys refresh \  
&& zypper install -y megatools \  
# Download and unzip SAP HANA 2.0 EXPRESSION Installation file  
&& megadl $SAP_INSTALL_PACKAGE \  
&& tar -xzvf $SAP_INSTALL_FILE_NAME \  
  
&& zypper rm -y megatools \  
&& zypper clean \  
&& rm -rf /var/cache/zypp/* \  
&& rm -rf /root/.cache/ \  

