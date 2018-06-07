FROM phusion/baseimage:0.9.19  
# Standard stuff  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ARG SOURCE_COMMIT  
ENV SOURCE_COMMIT ${SOURCE_COMMIT}  
ARG DOCKER_TAG  
ENV DOCKER_TAG ${DOCKER_TAG}  
  
ENV HTTP_SERVER_PORT 8080  
ENV APP_SERVER_PORT 9000  
ENV APP_ROOT /app  
ENV APP_STATIC_ROOT ${APP_ROOT}/static  
ENV APPRUN_ROOT ${APP_ROOT}  
ENV APPRUN_CMD ${APP_ROOT}/bin/steemyo  
  
ENV ENVIRONMENT DEV  
  
# Dependencies  
RUN \  
apt-get update && \  
apt-get install -y \  
build-essential \  
checkinstall \  
pkg-config \  
daemontools \  
git \  
libffi-dev \  
libmysqlclient-dev \  
libssl-dev \  
make \  
python3 \  
python3-dev \  
python3-pip \  
libxml2-dev \  
libxslt-dev \  
runit \  
nginx \  
wget \  
libsqlite3-dev \  
pandoc  
  
# Python 3.6  
RUN \  
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz && \  
tar xvf Python-3.6.2.tar.xz && \  
cd Python-3.6.2/ && \  
./configure && \  
make altinstall  
  
# Configure nginx etc  
RUN \  
mkdir -p /var/lib/nginx/body && \  
mkdir -p /var/lib/nginx/scgi && \  
mkdir -p /var/lib/nginx/uwsgi && \  
mkdir -p /var/lib/nginx/fastcgi && \  
mkdir -p /var/lib/nginx/proxy && \  
chown -R www-data:www-data /var/lib/nginx && \  
mkdir -p /var/log/nginx && \  
touch /var/log/nginx/access.log && \  
touch /var/log/nginx/error.log && \  
chown www-data:www-data /var/log/nginx/*.log && \  
touch /var/run/nginx.pid && \  
chown www-data:www-data /var/run/nginx.pid  
  
ADD ./service /etc/service  
RUN chmod +x /etc/service/*/run  
  
# This updates the distro-provided pip and gives us pip3.6 binary  
RUN python3.6 -m pip install --upgrade pip pipenv  
  
WORKDIR ${APP_ROOT}  
  
# Copy code into a suitable place  
COPY ./Makefile ${APP_ROOT}/Makefile  
COPY ./Pipfile ${APP_ROOT}/Pipfile  
COPY ./Pipfile.lock ${APP_ROOT}/Pipfile.lock  
COPY ./scripts ${APP_ROOT}/scripts  
COPY ./tests ${APP_ROOT}/tests  
COPY ./yo ${APP_ROOT}/yo  
COPY ./yo.cfg ${APP_ROOT}/yo.cfg  
COPY ./.pylintrc ${APP_ROOT}/.pylintrc  
COPY ./mail_templates ${APP_ROOT}/mail_templates  
  
ENV HOME ${APP_ROOT}  
  
RUN pipenv install --dev  
  
# run tests  
RUN make test  
  
# Expose the HTTP server port  
EXPOSE ${HTTP_SERVER_PORT}  

