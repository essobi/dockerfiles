# original image  
#FROM leadingfellows/php-drupal:5.6 AS source-image  
#FROM scratch  
#COPY --from=source-image / /  
FROM leadingfellows/php-drupal:5.6  
USER root  
#-------  
# ensure local python is preferred over distribution python  
ENV PATH /usr/local/bin:$PATH  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
# install ca-certificates so that HTTPS works consistently  
# add python3, basg git  
# the other runtime dependencies for Python are installed later  
RUN apk add --no-cache ca-certificates \  
&& apk add --no-cache --virtual .fetch-deps openssl \  
&& apk add --no-cache python3 git bash gcc  
  
# make some useful symlinks that are expected to exist  
RUN set -ex \  
&& ln -s `which idle3` /usr/local/bin/idle \  
&& ln -s `which pydoc3` /usr/local/bin/pydoc \  
&& ln -s `which python3` /usr/local/bin/python \  
&& ln -s `which python3-config` /usr/local/bin/python-config  
  
# copy from https://github.com/docker-library/python  
# ENV PYTHON_PIP_VERSION 9.0.1  
# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid
truth value '<VERSION>'"  
RUN set -ex \  
\  
&& apk add --no-cache --virtual .fetch-deps libressl \  
\  
&& wget -O get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
\  
&& apk del .fetch-deps \  
\  
&& python get-pip.py \  
# --disable-pip-version-check \  
\--no-cache-dir \  
# "pip==$PYTHON_PIP_VERSION" \  
\  
&& ln -s `which pip3` /usr/local/bin/pip \  
&& pip --version \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a \\( -name test -o -name tests \\) \\) \  
-o \  
\\( -type f -a \\( -name '*.pyc' -o -name '*.pyo' \\) \\) \  
\\) -exec rm -rf '{}' +; \  
rm -f get-pip.py \  
&& rm -f python-config  
  
#-------------------  
RUN set -ex &&\  
pip install -U wheel &&\  
pip install -U PyGithub &&\  
pip install -U tornado &&\  
pip install -U python-dotenv &&\  
pip install -U netaddr &&\  
pip install -U ipaddress &&\  
pip install -U dnspython &&\  
pip install -U ovh  
  
# install Drupal console, drush, composer and python libs  
RUN set -ex && \  
chown -R www-data /home/www-data/ && \  
su-exec www-data composer global require drush/drush && \  
su-exec www-data composer clear-cache && \  
su-exec www-data drush cc drush && \  
curl https://drupalconsole.com/installer -L -o drupal.phar && \  
mv drupal.phar /usr/local/bin/drupal && \  
chmod +x /usr/local/bin/drupal  
  
# supervisord  
RUN set -ex && \  
apk add --no-cache supervisor && \  
rm /etc/supervisord.conf && \  
mkdir -p /etc/supervisor/conf.d && \  
mkdir -p /etc/supervisor/conf.d.available && \  
mkdir -p /var/log/supervisor && \  
mkdir -p /var/run/ && \  
touch /var/run/supervisor.sock && \  
touch /var/run/supervisor.pid && \  
rm -rf /var/cache/apk/*  
  
COPY supervisord.conf /etc/supervisor  
COPY website_manager.conf /etc/supervisor/conf.d  
RUN chown -R www-data /etc/supervisor /var/log/supervisor/
/var/run/supervisor.sock /var/run/supervisor.pid  
  
# pre-configure env file for website  
ENV DRUPAL_WEBSITE_ROOT /var/www/html  
RUN mkdir -p ${DRUPAL_WEBSITE_ROOT}  
RUN touch ${DRUPAL_WEBSITE_ROOT}/.env  
RUN chmod -xw ${DRUPAL_WEBSITE_ROOT}/.env  
RUN chmod +r ${DRUPAL_WEBSITE_ROOT}/.env  
  
# install website_manager  
ENV WEBSITE_MANAGER_DIRECTORY /usr/local/website_manager  
  
RUN mkdir -p ${WEBSITE_MANAGER_DIRECTORY}  
RUN chown -R www-data ${WEBSITE_MANAGER_DIRECTORY}  
  
COPY ./website_manager.sh /usr/local/bin/  
RUN chmod u+wrx /usr/local/bin/website_manager.sh  
RUN chown www-data /usr/local/bin/website_manager.sh  
  
COPY ./docker-entrypoint-website-manager.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint-website-manager.sh  
  
# set php user and update PATH  
USER www-data  
ENV PATH /usr/local/bin:$PATH  
ENTRYPOINT ["docker-entrypoint-website-manager.sh"]  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"]  
  

