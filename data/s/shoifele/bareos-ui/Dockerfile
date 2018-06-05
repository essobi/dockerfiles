FROM shoifele/bone-centos  
  
MAINTAINER Christoph Wiechert <wio@psitrax.de>  
  
ENV REFRESHED_AT="2016-04-21" \  
BAREOS_DIR_HOST="bareos-dir"  
# https://github.com/docker/hub-feedback/issues/461  
RUN yum -y install httpd || true ; yum clean all  
  
RUN curl -Ls
http://download.bareos.org/bareos/release/latest/CentOS_7/bareos.repo \  
> /etc/yum.repos.d/bareos.repo \  
&& yum -y install \  
bareos-webui \  
&& yum clean all \  
&& mv /etc/bareos-webui/directors.ini /etc/bareos-webui/directors.ini.default
\  
# Patch session timeout, 60s is way too short  
&& sed -i 's/$timeout = 600;/$timeout = 3600;/' /usr/share/bareos-
webui/module/Application/src/Application/Controller/Plugin/SessionTimeoutPlugin.php  
  
ADD rootfs /  
  
EXPOSE 80  
VOLUME /etc/bareos-webui  
  
CMD ["/init"]  

