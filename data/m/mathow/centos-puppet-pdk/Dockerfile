FROM centos:latest  
MAINTAINER Mark Athow (mark.athow@gmail.com)  
  
RUN curl -s -L --output pdk.rpm \  
"https://pm.puppetlabs.com/cgi-
bin/pdk_download.cgi?dist=el&rel=7&arch=x86_64&ver=latest" && \  
rpm -i pdk.rpm && \  
rm -rf pdk.rpm && \  
ln -s /opt/puppetlabs/pdk/private/git/bin/git /usr/bin/git  
  

