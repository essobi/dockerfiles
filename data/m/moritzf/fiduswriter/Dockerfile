# vim: set ts=4 sw=4 sts=0 sta et :  
FROM ubuntu:18.04  
EXPOSE 8000:8000  
ENV VERSION 3.4.5  
# Executing group, with fixed group id  
ENV EXECUTING_GROUP fiduswriter  
ENV EXECUTING_GROUP_ID 999  
# Executing user, with fixed user id  
ENV EXECUTING_USER fiduswriter  
ENV EXECUTING_USER_ID 999  
# Data volume, should be owned by 999:999 to ensure the application can  
# function correctly. Run `chown 999:999 <data-dir-path>` on the host OS to  
# get this right.  
VOLUME ["/data"]  
  
# Create user and group with fixed ID, instead of allowing the OS to pick one.  
RUN groupadd \  
\--system \  
\--gid ${EXECUTING_GROUP_ID} \  
${EXECUTING_GROUP} \  
&& useradd \  
\--system \  
\--create-home \  
\--no-log-init \  
\--uid ${EXECUTING_USER_ID} \  
\--gid ${EXECUTING_USER} \  
${EXECUTING_USER}  
  
# Chain apt-get update, apt-get install and the removal of the lists.  
# This is one of the best practices of Docker, see  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#apt-get  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
gettext \  
git \  
libjpeg-dev \  
nodejs \  
npm \  
python3-venv \  
python3-dev \  
python3-pip \  
unzip \  
wget \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download fiduswriter release from github  
# Run the unzipping, moving and removal of zip file in the same layer.  
RUN wget \  
\--output-document=fiduswriter.zip \  
https://github.com/fiduswriter/fiduswriter/archive/${VERSION}.zip \  
&& unzip fiduswriter.zip \  
&& mv fiduswriter-${VERSION} /fiduswriter \  
&& rm fiduswriter.zip  
  
# Working directories should be absolute.  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#workdir  
WORKDIR /fiduswriter  
  
RUN mkdir static-libs && \  
cp configuration.py-default configuration.py  
  
RUN chmod -R 777 /data /fiduswriter  
  
USER ${EXECUTING_USER}  
  
RUN python3 -m venv venv  
RUN /bin/bash -c "source venv/bin/activate"  
  
RUN pip3 install -r requirements.txt  
  
RUN python3 manage.py init  
  
COPY start-fiduswriter.sh /etc/start-fiduswriter.sh  
  
# Always use the array form for exec, see  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#cmd  
CMD ["/bin/sh", "/etc/start-fiduswriter.sh"]  

