FROM centos:centos7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
LABEL org.openmicroscopy.release-date="unknown"  
  
RUN mkdir /opt/setup  
WORKDIR /opt/setup  
ADD playbook.yml requirements.yml /opt/setup/  
  
RUN yum -y install epel-release \  
&& yum -y install ansible sudo \  
&& ansible-galaxy install -p /opt/setup/roles -r requirements.yml  
  
ARG OMERO_VERSION=5.4.5  
RUN ansible-playbook playbook.yml -e omero_web_release=$OMERO_VERSION  
  
RUN curl -L -o /usr/local/bin/dumb-init \  
https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 && \  
chmod +x /usr/local/bin/dumb-init  
ADD entrypoint.sh /usr/local/bin/  
ADD 50-config.py 60-default-web-config.sh 98-cleanprevious.sh 99-run.sh
/startup/  
  
RUN bash /opt/omero/web/venv/bin/activate \  
&& pip install -r /opt/omero/web/OMERO.web/share/web/requirements-redis.txt  
  
RUN bash /opt/omero/web/venv/bin/activate \  
&& pip install -r /opt/omero/web/OMERO.web/share/web/requirements-redis.txt  
  
USER omero-web  
RUN mkdir /opt/omero/web/OMERO.web/var  
RUN sed -i "s/^\\(omero\\.host\s*=\s*\\).*\$/\1omero/"
/opt/omero/web/OMERO.web/etc/ice.config  
  
EXPOSE 4080  
VOLUME ["/opt/omero/web/OMERO.web/var"]  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

