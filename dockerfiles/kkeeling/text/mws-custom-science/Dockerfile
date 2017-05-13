FROM quay.io/keboola/base-python:3.5.1-g

MAINTAINER Keenan Keeling <kkeeling@automatastudios.com>

WORKDIR /home

COPY . /home/

# Install/update packages
RUN yum -y update \
	&& yum -y install \
		ipython \
	&& yum clean all

# Upgrade pip
RUN pip install --upgrade pip --cert=/tmp/cacert.pem

# Install 3rd-party python libs
RUN pip install --no-cache-dir --ignore-installed --cert=/tmp/cacert.pem \
		boto \
		ipython \
	&& pip install --upgrade --no-cache-dir --ignore-installed --cert=/tmp/cacert.pem git+git://github.com/keboola/python-docker-application.git@1.2.0

# Run the application
ENTRYPOINT python ./main.py --data=/data/