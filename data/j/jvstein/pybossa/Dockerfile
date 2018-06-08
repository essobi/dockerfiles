FROM python:2.7-alpine  
  
ENV REDIS_SENTINEL=redis-sentinel  
ENV REDIS_MASTER=mymaster  
  
# install git and various python library dependencies with alpine tools  
RUN set -x && \  
apk --no-cache add postgresql-dev g++ gcc git jpeg-dev libffi-dev libjpeg
libxml2-dev libxslt-dev linux-headers musl-dev openssl zlib zlib-dev  
  
# install python dependencies with pip  
# install pybossa from git  
# add unprivileged user for running the service  
ENV LIBRARY_PATH=/lib:/usr/lib  
RUN set -x && \  
git clone \--recursive https://github.com/Scifabric/pybossa /opt/pybossa && \  
cd /opt/pybossa && \  
pip install -U pip setuptools && \  
pip install -r /opt/pybossa/requirements.txt && \  
rm -rf /opt/pybossa/.git/ && \  
addgroup pybossa && \  
adduser -D -G pybossa -s /bin/sh -h /opt/pybossa pybossa && \  
passwd -u pybossa  
  
# variables in these files are modified with sed from /entrypoint.sh  
ADD alembic.ini /opt/pybossa/  
ADD settings_local.py /opt/pybossa/  
  
# TODO: we shouldn't need write permissions on the whole folder  
# Known files written during runtime:  
# - /opt/pybossa/pybossa/themes/default/static/.webassets-cache  
# - /opt/pybossa/alembic.ini and /opt/pybossa/settings_local.py (from
entrypoint.sh)  
RUN chown -R pybossa:pybossa /opt/pybossa  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
# run with unprivileged user  
USER pybossa  
WORKDIR /opt/pybossa  
EXPOSE 8080  
# Background worker is also necessary and should be run from another copy of
this container  
# python app_context_rqworker.py scheduled_jobs super high medium low email
maintenance  
CMD ["python", "run.py"]  

