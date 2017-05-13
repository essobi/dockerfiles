#
# Spark Dockerfile
#
FROM ubuntu:vivid

# set env
ENV DEBIAN_FRONTEND noninteractive
# set apt-get repository
ARG APT_MIRROR=jp.archive.ubuntu.com
RUN sed -i "s/archive.ubuntu.com/${APT_MIRROR}/g" /etc/apt/sources.list

# Setting environment
ENV VERSION 2.0.0
# Install Python
RUN apt-get update && \
    apt-get install -y \
    python-dev \
    python-pip

RUN pip install luigi==${VERSION}

# Expose ports
EXPOSE 8082
# command
CMD luigid

#Cleanup
RUN rm -rf /tmp/*
