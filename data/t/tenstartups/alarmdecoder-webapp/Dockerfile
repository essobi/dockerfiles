#  
# AlarmDecoder web application  
#  
# http://github.com/tenstartups/alarmdecoder-webapp  
#  
FROM alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment variables.  
ENV \  
PAGER=more \  
PIP_NO_CACHE_DIR=off \  
PIP_DISABLE_PIP_VERSION_CHECK=on  
  
# Install packages.  
RUN \  
apk --update add \  
bsd-compat-headers \  
build-base \  
curl-dev \  
dosfstools \  
git \  
libffi-dev \  
libressl-dev \  
libxml2-dev \  
libxslt-dev \  
linux-headers \  
pcre-dev \  
python \  
python-dev \  
py2-pip \  
sqlite \  
sudo \  
zlib-dev && \  
rm -rf /var/cache/apk/*  
  
# Install python packages.  
RUN \  
pip install gunicorn --upgrade  
  
# Create the required user.  
RUN \  
addgroup alarmdecoder && \  
adduser -D -s /bin/sh alarmdecoder -G alarmdecoder  
  
# Set the working directory.  
WORKDIR /opt/alarmdecoder-webapp  
  
# Install the alarmdecoder web application  
RUN \  
git clone https://github.com/nutechsoftware/alarmdecoder-webapp.git . && \  
pip install -r requirements.txt && \  
pip install -e
git://github.com/nutechsoftware/alarmdecoder.git@master#egg=alarmdecoder && \  
mkdir instance && \  
chown -R alarmdecoder:alarmdecoder .  
  
# Initialize the application database  
RUN \  
su alarmdecoder -c 'python manage.py initdb'  
  
# Add files to the container.  
COPY entrypoint.sh /docker-entrypoint  
  
# Set the entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Create data volume.  
VOLUME /opt/alarmdecoder-webapp/instance  
  
# Expose the default alarmdecoder port.  
# Note that we need to run this image with --net=host so this port is
unimportant.  
EXPOSE 5000  
# Set the default command.  
CMD ["gunicorn", "-u", "alarmdecoder", "-g", "alarmdecoder", "-b",
"unix:/tmp/gunicorn.sock", "wsgi:application"]  

