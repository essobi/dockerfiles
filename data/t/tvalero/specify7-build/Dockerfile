FROM buildpack-deps:jessie  
  
MAINTAINER MIVEGEC  
  
RUN apt-get update && apt-get install -y \  
git python-pip python-dev libmysqlclient-dev \  
build-essential curl sudo  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -  
  
RUN apt-get install -y nodejs  
  
RUN git clone https://github.com/tvalero/specify7.git  
  
RUN pip install -r specify7/requirements.txt  
  
RUN make -C specify7  
  
EXPOSE 8080  
# ENTRYPOINT python specify7/specifyweb/manage.py runserver  
# The webapp server piggy backs on the thick client.  
# Set the path to a thick client installation.  
ENV SPECIFY_THICK_CLIENT_LOCATION '/opt/Specify'  
ENV SPECIFY_VERSION '6.6.04'  
RUN mkdir -p ${SPECIFY_THICK_CLIENT_LOCATION}/config  
ADD specify.jar ${SPECIFY_THICK_CLIENT_LOCATION}  
ADD specify-6-config/ ${SPECIFY_THICK_CLIENT_LOCATION}/config  
  
# Set the database name to the mysql database you  
# want to access.  
ENV SPECIFY_DATABASE_NAME 'specify'  
ENV SPECIFY_DATABASE_HOST 'hansel.local'  
ENV SPECIFY_DATABASE_PORT 3306  
# The master user login. Use the same values as  
# you did setting up the thick client.  
ENV SPECIFY_MASTER_NAME 'master'  
ENV SPECIFY_MASTER_PASSWORD 'master'  
# Select the schema localization language.  
ENV SPECIFY_SCHEMA_LANGUAGE 'en'  
# The Specify web attachement server URL.  
ENV SPECIFY_WEB_ATTACHMENT_URL "http://example.com/web_asset_store.xml"  
# The Specify web attachment server key.  
ENV SPECIFY_WEB_ATTACHMENT_KEY None  
  
# The collection name to use with the web attachment server.  
ENV SPECIFY_WEB_ATTACHMENT_COLLECTION None  
  
# Set to true if asset server requires auth token to get files.  
ENV SPECIFY_WEB_ATTACHMENT_REQUIRES_KEY_FOR_GET False  
  
# Report runner service  
ENV SPECIFY_REPORT_RUNNER_HOST ''  
ENV SPECIFY_REPORT_RUNNER_PORT ''  
# Workbench uploader log directory.  
# Must exist and be writeable by the web server process.  
ENV SPECIFY_WB_UPLOAD_LOG_DIR "/var/cache/specify_wb_upload/"  
RUN mkdir -p ${SPECIFY_WB_UPLOAD_LOG_DIR}  
  
# To allow anonymous use, set ANONYMOUS_USER to a Specify username  
# to use for anonymous access.  
ENV SPECIFY_ANONYMOUS_USER None  
  
# For exception logging using Sentry (https://github.com/getsentry/sentry).  
ENV SPECIFY_RAVEN_CONFIG None  
  
# Support login mechanism.  
ENV SPECIFY_ALLOW_SUPPORT_LOGIN False  
ENV SPECIFY_SUPPORT_LOGIN_TTL 300  

