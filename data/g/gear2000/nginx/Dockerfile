FROM ubuntu:16.04  
MAINTAINER Gary Leong <gwleong@gmail.com>  
  
RUN apt-get update -qq && \  
apt-get install -y -qq nginx && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
##############################  
######For SSL purposes  
ADD snippets/ /etc/nginx/snippets/  
RUN mkdir -p /etc/ssl/certs && mkdir -p /etc/ssl/private  
RUN rm -rf /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
##############################  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \  
apt-get update -qq && \  
apt-get install -qq -y pwgen wget curl git-core build-essential scons
devscripts lintian dh-make \  
libpcre3 libpcre3-dev libboost-dev libboost-date-time-dev libboost-filesystem-
dev \  
libboost-program-options-dev libboost-system-dev libboost-thread-dev \  
libpcap-dev libreadline-dev libssl-dev rng-tools  
  
CMD ["nginx", "-g", "daemon off;"]  
  
#http://www.geoffstratton.com/install-latest-nginx-source-ubuntu-1604  
#  
#RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 &&
\  
# apt-get update -qq && \  
# apt-get install -qq -y pwgen wget curl git-core build-essential scons
devscripts lintian dh-make \  
# libpcre3 libpcre3-dev libboost-dev libboost-date-time-dev libboost-
filesystem-dev \  
# libboost-program-options-dev libboost-system-dev libboost-thread-dev \  
# libpcap-dev libreadline-dev libssl-dev rng-tools && \  
# rm -rf /var/lib/apt/lists/*  
#  
#RUN apt-get update -qq && \  
# apt-get build-dep nginx -y && \  
# cd /opt && \  
# apt-get source nginx -y  
#  
#RUN cd /opt/nginx*/debian/modules && \  
# git clone http://github.com/wandenberg/nginx-push-stream-module.git  
#  
#Edit our rules file at /opt/nginx-1.11.2/debian/rules to reference our new
module:  
#  
#full_configure_flags := \  
# $(common_configure_flags) \  
# \--with-http_addition_module \  
# \--with-http_dav_module \  
# \--with-http_geoip_module \  
# \--with-http_gunzip_module \  
# \--with-http_gzip_static_module \  
# \--with-http_image_filter_module \  
# \--with-http_v2_module \  
# \--with-http_sub_module \  
# \--with-http_xslt_module \  
# \--with-stream \  
# \--with-stream_ssl_module \  
# \--with-mail \  
# \--with-mail_ssl_module \  
# \--with-threads \  
# \--add-module=$(MODULESDIR)/nginx-auth-pam \  
# \--add-module=$(MODULESDIR)/nginx-dav-ext-module \  
# \--add-module=$(MODULESDIR)/nginx-echo \  
# \--add-module=$(MODULESDIR)/nginx-upstream-fair \  
# \--add-module=$(MODULESDIR)/ngx_http_substitutions_filter_module \  
# \--add-module=$(MODULESDIR)/nginx-push-stream-module <\-----------  
#  
#RUN dpkg-buildpackage -uc -b && \  
# dpkg --install nginx-common_1.11.2-0+xenial0_all.deb && \  
# dpkg --install nginx-full_1.11.2-0+xenial0_amd64.deb  
#  
#CMD ["nginx", "-g", "daemon off;"]  

