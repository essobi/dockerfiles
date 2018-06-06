FROM centos:centos7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
# TODO: Use separate Nginx container  
ARG OMERO_VERSION=latest  
ARG CI_SERVER  
ARG OMEGO_ARGS  
  
WORKDIR /home/omero  
  
ADD omero-grid-web-deps.yml requirements.yml run.sh /home/omero/  
  
# TODO: Remove requirements install once the role is updated.  
ENV OMERO_REQUIREMENTS_FILE OMERO.server/share/web/requirements-py27.txt  
  
RUN yum -y install epel-release \  
&& yum -y install ansible \  
&& ansible-galaxy install -r requirements.yml \  
&& ansible-playbook omero-grid-web-deps.yml \  
&& useradd omero \  
&& pip install omego \  
&& bash -c 'CI=; if [ -n "$CI_SERVER" ]; then CI="--ci $CI_SERVER"; fi; \  
omego download python $CI --release $OMERO_VERSION $OMEGO_ARGS' \  
&& rm OMERO.py-*.zip \  
&& ln -s OMERO.py-*/ OMERO.server \  
&& rm /etc/nginx/conf.d/* \  
&& sed -i -r -e 's|/var/([^/]+)(/nginx)?/|/home/omero/nginx/\1/|' \  
-e '/^user/s/^/#/' /etc/nginx/nginx.conf \  
&& rm -rf /var/cache/nginx /var/log/nginx \  
# Must create OMERO.server/var because it's marked as a volume and will  
# otherwise default to root ownership  
&& mkdir -p nginx/cache nginx/log nginx/run nginx/temp OMERO.server/var \  
&& ln -sf /home/omero/nginx/cache /var/cache/nginx \  
&& ln -sf /home/omero/nginx/log /var/log/nginx \  
# TODO: Remove requirements install once the role is updated.  
&& test -f $OMERO_REQUIREMENTS_FILE && pip install -r $OMERO_REQUIREMENTS_FILE
\  
&& chown omero:omero -R .  
  
# Unavoidable hack as it is impossible to run omero as root  
USER omero  
RUN OMERO.server/bin/omero web config --http 8080 nginx > omero-web.conf  
USER root  
RUN mv omero-web.conf /etc/nginx/conf.d/omero-web.conf \  
&& chown root:root /etc/nginx/conf.d/omero-web.conf  
  
# TODO: Use docker logging instead of log files?  
# https://github.com/nginxinc/docker-nginx/blob/master/Dockerfile  
#ln -sf /dev/stdout /var/log/nginx/access.log && \  
#ln -sf /dev/stderr /var/log/nginx/error.log && \  
USER omero  
  
EXPOSE 8080  
VOLUME ["/home/omero/nginx", "/home/omero/OMERO.server/var"]  
  
# Set the default command to run when starting the container  
ENTRYPOINT ["/home/omero/run.sh"]  

