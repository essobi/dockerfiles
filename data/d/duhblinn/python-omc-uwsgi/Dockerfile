FROM ubuntu:14.04  
RUN apt-get -y update && \  
apt-get -y install wget python-pip python-setuptools build-essential python-
dev libatlas-dev libatlas3gf-base liblapack-dev gfortran \  
libfreetype6 libpng12-0 libfreetype6-dev libxft-dev libfreetype6-dev pkg-
config  
  
ENV WHEEL_DIR=/opt/python/wheelhouse TMP_WHEEL_DIR=/tmp/wheelhouse/  
  
RUN mkdir -p "$WHEEL_DIR"  
VOLUME ["/opt/python/wheelhouse"]  
  
# Add scripts and config files to docker container  
RUN mkdir -p /opt/scripts/  
COPY modelica_files/*.sh uwsgi_files/*.sh python_files/*.sh
python_files/requirements-*.txt /opt/scripts/  
RUN chmod u+x /opt/scripts/*.sh  
  
# Setup wheelhouse and install specific pip version  
RUN pip install --find-links "$WHEEL_DIR" -U 'pip==1.5.4' 'wheel==0.24.0'  
  
# Install default dependencies just using pip  
RUN pip install --find-links "$WHEEL_DIR" -U -r /opt/scripts/requirements-
science.txt  
RUN pip install --find-links "$WHEEL_DIR" -U -r /opt/scripts/requirements-
web.txt  
  
# Add uwsgi config files to docker container  
COPY uwsgi_files/wsgi_custom.conf /httpd/conf.d/wsgi_custom.conf  
  
# Install/Update modelica  
RUN /opt/scripts/update_modelica_194.sh  
  
# Setup UWSGI user and logs  
ENV UWSGI_PORT=8080  
ENV UWSGI_UID=uwsgi UWSGI_GID=uwsgi UWSGI_LOG_FILE=/var/log/uwsgi/uwsgi.log  
RUN echo "Adding user '${UWSGI_UID}' with group '${UWSGI_GID}'for uwsgi and
logging to '${UWSGI_LOG_FILE}' . " && \  
groupadd "${UWSGI_GID}" && useradd "${UWSGI_UID}" -g "${UWSGI_GID}" -s
/bin/false && \  
export UWSGI_LOG_DIR=$(dirname "${UWSGI_LOG_FILE}") && \  
if [ '!' -d "$UWSGI_LOG_DIR" ] ; then mkdir -p "$UWSGI_LOG_DIR" && chown -R
${UWSGI_UID}:${UWSGI_GID} "$UWSGI_LOG_DIR" ; fi && \  
touch "${UWSGI_LOG_FILE}" && chown -R ${UWSGI_UID}:${UWSGI_GID}
"$UWSGI_LOG_FILE"  
  
ENV APP_DIR /var/app  
ONBUILD COPY . $APP_DIR  
ONBUILD RUN chmod a+x "$APP_DIR"/scripts/*.py && chown -R uwsgi:uwsgi $APP_DIR  
WORKDIR $APP_DIR  
  
ONBUILD RUN pip install --find-links $WHEEL_DIR -r $APP_DIR/requirements.txt  
  
ENV PYTHONPATH=/usr/lib/python2.7/dist-packages/:$APP_DIR  
  
EXPOSE 8080  
CMD []  
ENTRYPOINT ["/opt/scripts/uwsgi-start.sh"]

