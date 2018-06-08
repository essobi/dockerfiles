FROM openmicroscopy/omero-ssh-daemon-c7:0.1.1  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
# OMERO prerequesties  
RUN yum install -y epel-release \  
&& yum clean all  
  
RUN yum install -y wget unzip git \  
&& yum clean all  
  
# Install Java  
RUN yum install -y java-1.8.0-openjdk-devel \  
&& yum clean all  
  
# Install Python and other dependences  
RUN yum install -y \  
python-pip python-virtualenv python-virtualenvwrapper \  
python-devel \  
numpy scipy \  
python-pillow \  
python-matplotlib \  
python-tables \  
&& yum clean all  
  
# Install Ice 3.6  
RUN cd /etc/yum.repos.d && wget https://zeroc.com/download/rpm/zeroc-ice-
el7.repo  
RUN yum install -y gcc gcc-c++ \  
libdb-utils \  
openssl-devel bzip2-devel expat-devel \  
&& yum clean all  
RUN cd /etc/yum.repos.d && yum install -y ice-all-runtime ice-all-devel  
  
# Install Postgres tools  
RUN yum -y install http://yum.postgresql.org/9.5/redhat/rhel-7-x86_64/pgdg-
centos95-9.5-3.noarch.rpm \  
&& yum clean all  
RUN yum -y install postgresql95 \  
&& yum clean all  
  
# RUN sript  
ADD ./install /tmp/install  
RUN chmod a+r -R /tmp/install  
RUN chmod a+x /tmp/install/*.sh  
  
# AS OMERO user  
USER omero  
  
# Envirment variables  
ENV HOME /home/omero  
ENV COMPONENT server  
  
ENV OMERO_DB_HOST postgres  
ENV OMERO_DB_PORT 5432  
ENV OMERO_DB_USER postgres  
ENV OMERO_DB_NAME omero  
ENV OMERO_ROOT_PASS omero  
ENV SKIP_UPGRADE_CHECK false  
ENV RUNSCRIPT $COMPONENT  
  
EXPOSE 4063 4064  
WORKDIR $HOME  
  
ENTRYPOINT ["/tmp/install/docker-entrypoint.sh"]  

