#
# Kafka Dockerfile
#
FROM ubuntu:vivid

# set env
ENV DEBIAN_FRONTEND noninteractive

# set apt-get repository
ARG APT_MIRROR=jp.archive.ubuntu.com
RUN sed -i "s/archive.ubuntu.com/${APT_MIRROR}/g" /etc/apt/sources.list

RUN apt-get update; \
    apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:gluster/glusterfs-3.5; \
    apt-get install -y glusterfs-server

CMD ["glusterd", "--pid-file=/tmp/gluster.pid", "--log-file=/var/log/gluster.log", "--no-daemon"]
