FROM centos:7  
LABEL maintainer daichi703n <daichi703n@gmail.com>  
  
ENV HTTP_PROXY $HTTP_PROXY  
ENV http_proxy $HTTP_PROXY  
ENV HTTPS_PROXY $HTTPS_PROXY  
ENV https_proxy $HTTPS_PROXY  
ENV NO_PROXY localhost,127.0.0.1,$NO_PROXY  
ENV no_proxy localhost,127.0.0.1,$NO_PROXY  
  
USER root  
RUN if [ "$HTTP_PROXY" = "" ] ; then echo "Proxy not set" ; else echo
"proxy=$HTTP_PROXY" >> /etc/yum.conf ; fi  
RUN yum install -y \  
java-1.8.0-openjdk \  
rsyslog \  
unzip \  
vim-common \  
wget  
RUN yum clean all  
RUN wget
https://github.com/hinemos/hinemos/releases/download/v6.1.0/hinemos-6.1-manager-6.1.0-1.el7.x86_64.rpm
\  
&& wget
https://github.com/hinemos/hinemos/releases/download/v6.1.0/hinemos-6.1-web-6.1.0-1.el7.x86_64.rpm  
RUN rpm -ivh hinemos-6.1-manager-6.1.0-1.el7.x86_64.rpm \  
&& rpm -ivh hinemos-6.1-web-6.1.0-1.el7.x86_64.rpm  
RUN rm -f hinemos-6.1-manager-6.1.0-1.el7.x86_64.rpm \  
hinemos-6.1-web-6.1.0-1.el7.x86_64.rpm  
  
EXPOSE 80 8080 8081 8082 514 514/udp 162/udp  
  
CMD /sbin/init  

