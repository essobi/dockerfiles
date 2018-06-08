FROM centos:centos7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
LABEL org.openmicroscopy.release-date="unknown"  
  
RUN mkdir /opt/setup  
WORKDIR /opt/setup  
ADD playbook.yml requirements.yml /opt/setup/  
  
RUN yum -y install epel-release \  
&& yum -y install ansible sudo \  
&& ansible-galaxy install -p /opt/setup/roles -r requirements.yml  
  
ARG OMERO_VERSION=latest  
ARG OMEGO_ADDITIONAL_ARGS=  
RUN ansible-playbook playbook.yml \  
-e omero_web_release=$OMERO_VERSION \  
-e omero_web_omego_additional_args="$OMEGO_ADDITIONAL_ARGS"  
  
RUN curl -L -o /usr/local/bin/dumb-init \  
https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 && \  
chmod +x /usr/local/bin/dumb-init  
ADD entrypoint.sh /usr/local/bin/  
ADD 50-config.py 60-default-web-config.sh 98-cleanprevious.sh 99-run.sh
/startup/  
  
USER omero-web  
RUN mkdir /opt/omero/web/OMERO.web/var  
RUN sed -i "s/^\\(omero\\.host\s*=\s*\\).*\$/\1omero/"
/opt/omero/web/OMERO.web/etc/ice.config  
  
EXPOSE 4080  
VOLUME ["/opt/omero/web/OMERO.web/var"]  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

