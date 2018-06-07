FROM centos:7  
  
LABEL maintainer "Jimmi Dyson <jimmidyson@gmail.com>"  
  
COPY google-chrome.repo /etc/yum.repos.d/google-chrome.repo  
COPY passwd.template /usr/local/share/passwd.template  
COPY chkpasswd /usr/local/bin/chkpasswd  
  
RUN yum update -y && \  
yum install -y epel-release git gettext && \  
yum install -y nss_wrapper && \  
curl https://dl.yarnpkg.com/rpm/yarn.repo > /etc/yum.repos.d/yarn.repo && \  
curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && \  
yum install -y google-chrome-stable xorg-x11-server-Xvfb liberation-mono-fonts
liberation-narrow-fonts liberation-sans-fonts liberation-serif-fonts yarn
nodejs gcc-c++ make && \  
mkdir /.cache /.config && chmod 777 /.cache /.config && \  
dbus-uuidgen > /etc/machine-id  

