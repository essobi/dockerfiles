FROM centos:7  
MAINTAINER Naftuli Kay <rfkrocktk@gmail.com>  
  
# security environment variable for tainting the image when necessary  
ENV BUILD_DATE=20161208  
# packages  
ENV SYSTEM_PACKAGES="bind-utils jq man-db man-pages openssl-devel python-pip
tmux traceroute net-tools nc nmap vim wget"  
ENV REINSTALL_SYSTEM_PACKAGES="curl"  
ENV PYTHON_PACKAGES="awscli ipython requests"  
# install the man pages, glorious man pages  
RUN sed -i s/nodocs//g /etc/yum.conf  
  
# upgrade everything  
RUN yum upgrade -y >/dev/null  
  
# install epel  
RUN yum install -y epel-release >/dev/null  
  
# install system packages  
RUN yum install -y $SYSTEM_PACKAGES >/dev/null  
  
# reinstall certain system packages for man pages  
RUN yum reinstall -y $REINSTALL_SYSTEM_PACKAGES >/dev/null  
  
# install pip packages  
RUN pip install --upgrade pip >/dev/null && \  
pip install $PYTHON_PACKAGES >/dev/null  
  
# clean up  
RUN yum clean all >/dev/null  
  
ENTRYPOINT /bin/bash  

