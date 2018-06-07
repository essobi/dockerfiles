FROM centos:7  
RUN yum install -y epel-release  
  
RUN yum update -y \  
&& yum-config-manager --disable extras \  
&& yum makecache \  
&& yum install -y rpm-build rpmdevtools yum-utils sudo tar ccache make rpmlint
gcc \  
&& yum clean packages #20161006 \  
&& sed -i 's/\\(keepcache=\\)0/\11/' /etc/yum.conf  
  
RUN adduser -u 1000 build \  
&& ( \  
echo "build ALL = (root) NOPASSWD: /usr/bin/yum-builddep"; \  
echo "build ALL = (root) NOPASSWD: /usr/bin/yum"; \  
)> /etc/sudoers.d/build \  
&& chmod 440 /etc/sudoers.d/build  
  
RUN sed -i s/enabled=1/enabled=0/ /etc/yum/pluginconf.d/fastestmirror.conf  

