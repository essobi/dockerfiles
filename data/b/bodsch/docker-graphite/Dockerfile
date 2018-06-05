  
FROM alpine:3.7 as builder  
  
ARG BUILD_DATE  
ARG GRAPHITE_VERSION  
ARG PYTHON_VERSION  
ARG BUILD_TYPE  
  
ENV \  
TZ='Europe/Berlin' \  
TERM=xterm  
  
# 2003: Carbon line receiver port  
# 7002: Carbon cache query port  
# 8080: Graphite-Web port  
EXPOSE 2003 2003/udp 7002 8080  
  
LABEL \  
version="1804" \  
maintainer="Bodo Schulz <bodo@boone-schulz.de>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="Graphite Docker Image" \  
org.label-schema.description="Inofficial Graphite Docker Image" \  
org.label-schema.url="https://graphite.readthedocs.io/en/latest/index.html" \  
org.label-schema.vcs-url="https://github.com/bodsch/docker-graphite" \  
org.label-schema.vendor="Bodo Schulz" \  
org.label-schema.version=${GRAPHITE_VERSION} \  
org.label-schema.schema-version="1.0" \  
com.microscaling.docker.dockerfile="/Dockerfile" \  
com.microscaling.license="The Unlicense"  
#
---------------------------------------------------------------------------------------  
  
RUN \  
echo "export TZ=${TZ}" > /etc/enviroment && \  
echo "export BUILD_DATE=${BUILD_DATE}" >> /etc/enviroment && \  
echo "export BUILD_TYPE=${BUILD_TYPE}" >> /etc/enviroment && \  
echo "export GRAPHITE_VERSION=${GRAPHITE_VERSION}" >> /etc/enviroment && \  
apk update --quiet --no-cache && \  
apk upgrade --quiet --no-cache && \  
apk add --quiet --no-cache --virtual .build-deps \  
build-base git libffi-dev py${PYTHON_VERSION}-pip python${PYTHON_VERSION}-dev
&& \  
apk add --quiet --no-cache \  
cairo curl mariadb-client nginx supervisor python${PYTHON_VERSION}
py${PYTHON_VERSION}-cairo py${PYTHON_VERSION}-parsing py-mysqldb && \  
pip${PYTHON_VERSION} install \  
\--quiet --trusted-host http://d.pypi.python.org/simple --upgrade pip && \  
mkdir /src && \  
git clone https://github.com/graphite-project/whisper.git /src/whisper && \  
git clone https://github.com/graphite-project/carbon.git /src/carbon && \  
git clone https://github.com/graphite-project/graphite-web.git /src/graphite-
web && \  
if [ "${BUILD_TYPE}" == "stable" ] ; then \  
for i in whisper carbon graphite-web ; do \  
echo "switch to stable Tag ${GRAPHITE_VERSION} for $i" && \  
cd /src/$i ; \  
git checkout tags/${GRAPHITE_VERSION} 2> /dev/null ; \  
done ; \  
fi && \  
if [[ "${PYTHON_VERSION}" = 3 ]] ; then \  
sed -i 's|^python-memcached|# python-memcached|g' /src/graphite-
web/requirements.txt; \  
fi && \  
cd /src/graphite-web && pip${PYTHON_VERSION} install --quiet --requirement
requirements.txt && \  
cd /src/whisper && python -W ignore::UserWarning:distutils.dist setup.py
install --quiet > /dev/null && \  
cd /src/carbon && python -W ignore::UserWarning:distutils.dist setup.py
install --quiet > /dev/null && \  
cd /src/graphite-web && python -W ignore::UserWarning:distutils.dist setup.py
install --quiet > /dev/null && \  
mv /opt/graphite/conf/graphite.wsgi.example
/opt/graphite/webapp/graphite/graphite_wsgi.py && \  
mv /src/carbon/lib/carbon/tests/data/conf-directory/storage-aggregation.conf
/opt/graphite/conf/storage-aggregation.conf-DIST && \  
mv /src/carbon/lib/carbon/tests/data/conf-directory/storage-schemas.conf
/opt/graphite/conf/storage-schemas.conf-DIST && \  
apk del --quiet .build-deps && \  
rm -rf \  
/src \  
/tmp/* \  
/root/.cache \  
/var/cache/apk/*  
  
COPY rootfs/ /  
  
VOLUME /srv  
  
HEALTHCHECK \  
\--interval=5s \  
\--timeout=2s \  
\--retries=12 \  
CMD curl --silent --fail http://localhost:8080 || exit 1  
  
CMD [ "/init/run.sh" ]  
  
#
---------------------------------------------------------------------------------------  

