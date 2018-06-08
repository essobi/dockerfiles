FROM centos:centos7  
MAINTAINER ome-devel@lists.openmicroscopy.org.uk  
  
# TODO: Use separate Nginx container  
RUN yum -y install epel-release && \  
yum -y install ansible  
  
RUN mkdir /opt/infrastructure  
ADD omero-grid-web-deps.yml requirements.yml /opt/infrastructure/  
  
RUN cd /opt/infrastructure && \  
ansible-galaxy install -r requirements.yml && \  
ansible-playbook omero-grid-web-deps.yml  
  
RUN pip install omego  
  
RUN useradd omero && \  
rm /etc/nginx/conf.d/* && \  
sed -i -r -e 's|/var/([^/]+)(/nginx)?/|/home/omero/nginx/\1/|' \  
-e '/^user/s/^/#/' /etc/nginx/nginx.conf && \  
rm -rf /var/cache/nginx /var/log/nginx && \  
chown -R omero /etc/nginx/conf.d && \  
ln -sf /home/omero/nginx/cache /var/cache/nginx && \  
ln -sf /home/omero/nginx/log /var/log/nginx  
# TODO: Use docker logging instead of log files?  
# https://github.com/nginxinc/docker-nginx/blob/master/Dockerfile  
#ln -sf /dev/stdout /var/log/nginx/access.log && \  
#ln -sf /dev/stderr /var/log/nginx/error.log && \  
ARG OMERO_VERSION=latest  
ARG CI_SERVER  
ARG OMEGO_ARGS  
  
USER omero  
WORKDIR /home/omero  
RUN bash -c 'CI=; if [ -n "$CI_SERVER" ]; then CI="--ci $CI_SERVER"; fi; \  
omego download python $CI --release $OMERO_VERSION $OMEGO_ARGS && \  
rm OMERO.py-*.zip && \  
ln -s OMERO.py-*/ OMERO.server'  
# Must create OMERO.server/var because it's marked as a volume and will  
# otherwise default to root ownership  
RUN mkdir -p nginx/cache nginx/log nginx/run nginx/temp OMERO.server/var  
  
ADD run.sh /home/omero/  
  
# TODO: Remove me once the role is updated.  
USER root  
ENV OMERO_REQUIREMENTS_FILE /home/omero/OMERO.server/share/web/requirements-
py27.txt  
ENV REDIS_REQUIREMENTS_FILE /home/omero/OMERO.server/share/web/requirements-
redis.txt  
RUN test -f $OMERO_REQUIREMENTS_FILE && pip install -r
$OMERO_REQUIREMENTS_FILE  
RUN test -f $REDIS_REQUIREMENTS_FILE && pip install -r
$REDIS_REQUIREMENTS_FILE  
  
USER omero  
  
EXPOSE 8080  
VOLUME ["/home/omero/nginx", "/home/omero/OMERO.server/var"]  
  
# Set the default command to run when starting the container  
ENTRYPOINT ["/home/omero/run.sh"]  

