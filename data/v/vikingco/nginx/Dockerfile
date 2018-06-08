###########################################################  
# VikingCo: Nginx Server  
###########################################################  
FROM nginx:1.9.11  
MAINTAINER Dirk Moors  
  
# Set env variables  
ENV ROOT /data  
ENV CONF_DIR=/tmp/conf \  
CONF_SRC=./conf \  
SCRIPTS_SRC=./scripts \  
SCRIPTS_DIR=${ROOT}/scripts \  
MEDIA_DIR=${ROOT}/media \  
STATIC_DIR=${ROOT}/static \  
NGINX_LOG_DIR=/var/log/nginx \  
PORT=80 \  
SERVER_NAME=localhost  
  
# Save build args as environment variables  
ENV PORT=${PORT} \  
SERVER_NAME=${SERVER_NAME}  
  
# install and configure packages  
RUN set -x \  
&& buildDeps=' \  
python-pip \  
build-essential \  
' \  
&& requiredAptPackages=' \  
python \  
' \  
&& requiredPipPackages=' \  
Jinja2 \  
' \  
&& apt-get update \  
&& apt-get install -y $buildDeps $requiredAptPackages --no-install-recommends
\  
&& rm -rf /var/lib/apt/lists/* \  
&& pip install $requiredPipPackages \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' + \  
&& apt-get purge -y --auto-remove $buildDeps  
  
# make log directory  
RUN mkdir -p ${NGINX_LOG_DIR} \  
&& chown -R www-data ${NGINX_LOG_DIR}  
  
# add default files  
ADD ${CONF_SRC} ${CONF_DIR}  
ADD ${SCRIPTS_SRC} ${SCRIPTS_DIR}  
  
# make symlink for run script  
RUN ln -s ${SCRIPTS_DIR}/run.sh /usr/local/bin/run  
  
# set run command  
CMD run  

