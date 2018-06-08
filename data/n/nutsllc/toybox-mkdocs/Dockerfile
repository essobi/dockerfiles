#FROM python:3.5.2  
FROM python:2.7.12  
MAINTAINER Nuts Project, LLC  
  
# -----------------------------------------  
# General  
# -----------------------------------------  
#RUN apt-get update && apt-get install -y sudo vim && apt-get clean \  
# && groupadd -g 1000 mkdocs && useradd -u 1000 -g mkdocs mkdocs \  
# && echo "mkdocs ALL=NOPASSWD: ALL" >> /etc/sudoers  
# -----------------------------------------  
# mkdocs  
# -----------------------------------------  
ENV MKDOCS_VERSION="0.15.3"  
ENV MKDOCS_ROOT="/mkdocs"  
RUN pip install mkdocs==0.15.3 \  
&& pip install mkdocs-bootstrap \  
&& pip install mkdocs-bootswatch \  
&& mkdocs new /mkdocs \  
&& tar czf /mkdocs.tar.gz -C /mkdocs ./  
  
# -----------------------------------------  
# webhook for Github/Gitbucket  
# -----------------------------------------  
ENV WEBHOOK_ROOT="/Git-Auto-Deploy"  
COPY config.json /config.json  
RUN git clone https://github.com/olipo186/Git-Auto-Deploy.git ${WEBHOOK_ROOT}
\  
&& pip install -r ${WEBHOOK_ROOT}/requirements.txt \  
&& rm -rf ${WEBHOOK_ROOT}/.git \  
${WEBHOOK_ROOT}/.gitignore \  
${WEBHOOK_ROOT}/.travis.yml \  
${WEBHOOK_ROOT}/Dockerfile \  
${WEBHOOK_ROOT}/GitAutoDeploy.py \  
${WEBHOOK_ROOT}/LICENSE \  
${WEBHOOK_ROOT}/Makefile \  
${WEBHOOK_ROOT}/README.md \  
${WEBHOOK_ROOT}/config.json.sample \  
${WEBHOOK_ROOT}/docs \  
${WEBHOOK_ROOT}/platforms/ \  
${WEBHOOK_ROOT}/requirements.txt \  
${WEBHOOK_ROOT}/setup.py \  
${WEBHOOK_ROOT}/test \  
&& tar czf /Git-Auto-Deploy.tar.gz -C ${WEBHOOK_ROOT} ./  
#&& mkdir -p ${WEBHOOK_ROOT}/log \  
# -----------------------------------------  
# Apache2.4  
# -----------------------------------------  
#ENV APACHE_RUN_USER mkdocs  
#ENV APACHE_RUN_GROUP mkdocs  
#ENV APACHE_PID_FILE /var/run/apache2.pid  
#ENV APACHE_RUN_DIR /var/run/apache2  
#ENV APACHE_LOG_DIR /var/log/apache2  
#ENV APACHE_LOCK_DIR /var/lock/apache2  
RUN apt-get update && apt-get install -y apache2 && apt-get clean \  
&& mkdir -p /var/run/apache2 /var/lock/apache2  
  
# -----------------------------------------  
# Supervisor  
# -----------------------------------------  
RUN apt-get update && apt-get install -y supervisor \  
&& mkdir -p /var/run/Git-Auto-Deploy /var/log/supervisor \  
&& { \  
echo "[supervisord]"; \  
echo "nodaemon=true"; \  
echo ""; \  
echo "[program:apache2]"; \  
echo "command=/bin/bash -c 'source /etc/apache2/envvars && exec
/usr/sbin/apache2 -DFOREGROUND'"; \  
echo "autorestart=true"; \  
echo ""; \  
} > /etc/supervisor/conf.d/supervisord.conf  
  
# -----------------------------------------  
# Post building  
# -----------------------------------------  
COPY docker-entrypoint.sh /entrypoint.sh  
  
WORKDIR /mkdocs  
  
EXPOSE 80 8001  
ENTRYPOINT [ "/entrypoint.sh" ]  
#CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

