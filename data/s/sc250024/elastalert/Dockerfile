FROM alpine:3.7  
  
LABEL maintainer="Scott Crooks <scott.crooks@gmail.com>"  
# Set configuration parameters needed for the image and container
configuration  
## CONFIG_FOLDER => Directory holding configuration for Elastalert.  
## CONTAINER_TIMEZONE => Default container timezone as found under the
directory /usr/share/zoneinfo/.  
## DOCKERIZE_VERSION => Version of `dockerize` binary to download.  
## RULES_FOLDER => Elastalert rules directory.  
## SET_CONTAINER_TIMEZONE => Set this environment variable to True to set
timezone on container start.  
  
ENV CONFIG_FOLDER=/opt/elastalert/config \  
CONTAINER_TIMEZONE=Etc/UTC \  
DOCKERIZE_VERSION=0.6.1 \  
RULES_FOLDER=/opt/elastalert/rules \  
SET_CONTAINER_TIMEZONE=True  
  
# Set parameters needed for the `src/docker-entrypoint.sh` script  
## ELASTALERT_CONFIG => Location of the Elastalert configuration file based on
the ${CONFIG_FOLDER}  
## ELASTALERT_INDEX => ElastAlert writeback index  
## ELASTALERT_SYSTEM_GROUP => User to run the Elastlalert process  
## ELASTALERT_SYSTEM_USER => Group to run the Elastlalert process  
## ELASTALERT_VERSION => Version of Elastalert to install and run  
## ELASTICSEARCH_HOST => Alias, DNS or IP of Elasticsearch host to be queried
by Elastalert. Set in default Elasticsearch configuration file.  
## ELASTICSEARCH_PORT => Port on above Elasticsearch host. Set in default
Elasticsearch configuration file.  
## ELASTICSEARCH_USE_SSL => Use TLS to connect to Elasticsearch (True or
False)  
## ELASTICSEARCH_VERIFY_CERTS => Verify TLS  
  
ENV ELASTALERT_CONFIG="${CONFIG_FOLDER}/elastalert_config.yaml" \  
ELASTALERT_INDEX=elastalert_status \  
ELASTALERT_SYSTEM_GROUP=elastalert \  
ELASTALERT_SYSTEM_USER=elastalert \  
ELASTALERT_VERSION=0.1.29 \  
ELASTICSEARCH_HOST=elasticsearch \  
ELASTICSEARCH_PORT=9200 \  
ELASTICSEARCH_USE_SSL=False \  
ELASTICSEARCH_VERIFY_CERTS=False  
  
# Install packages  
RUN set -ex \  
&& apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
ca-certificates \  
dumb-init \  
openntpd \  
openssl \  
py2-pip \  
py2-yaml \  
python2 \  
su-exec \  
tzdata \  
wget \  
&& apk add --no-cache --virtual \  
.build-dependencies \  
gcc \  
libffi-dev \  
musl-dev \  
openssl-dev \  
python2-dev \  
&& pip install --upgrade pip \  
&& pip install elastalert=="${ELASTALERT_VERSION}" \  
&& apk del --purge .build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
# Get Dockerize for configuration templating  
RUN set -ex \  
&& wget -nv -O dockerize.tar.gz \  
"https://github.com/jwilder/dockerize/releases/download/v${DOCKERIZE_VERSION}/dockerize-
alpine-linux-amd64-v${DOCKERIZE_VERSION}.tar.gz" \  
&& tar -C /usr/local/bin -xzvf dockerize.tar.gz \  
&& chmod +x "/usr/local/bin/dockerize" \  
&& rm dockerize.tar.gz  
  
# Create directories and Elastalert system user/group.  
# The /var/empty directory is used by openntpd.  
RUN mkdir -p "${CONFIG_FOLDER}" \  
&& mkdir -p "${RULES_FOLDER}" \  
&& mkdir -p /var/empty \  
&& addgroup "${ELASTALERT_SYSTEM_GROUP}" \  
&& adduser -S -G "${ELASTALERT_SYSTEM_GROUP}" "${ELASTALERT_SYSTEM_USER}" \  
&& chown -R "${ELASTALERT_SYSTEM_USER}":"${ELASTALERT_SYSTEM_GROUP}"
"${CONFIG_FOLDER}" "${RULES_FOLDER}"  
# Copy the ${ELASTALERT_CONFIG} template  
COPY src/elastalert_config.yaml.tmpl
"${CONFIG_FOLDER}/elastalert_config.yaml.tmpl"  
# Copy the script used to launch the Elastalert when a container is started.  
COPY src/docker-entrypoint.sh /docker-entrypoint.sh  
  
# The square brackets around the 'e' are intentional. They prevent `grep`  
# itself from showing up in the process list and falsifying the results.  
# See here: https://stackoverflow.com/questions/9375711/more-elegant-ps-aux-
grep-v-grep  
HEALTHCHECK --interval=30s \--timeout=10s \--retries=3 \  
CMD ps -ef | grep "[e]lastalert.elastalert" >/dev/null 2>&1  
# Runs "/usr/bin/dumb-init -- /my/script --with --args"  
ENTRYPOINT ["/docker-entrypoint.sh"]  

