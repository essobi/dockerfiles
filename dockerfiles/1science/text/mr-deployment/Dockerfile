#
# 1Science image with boto and aws cli
#
FROM ubuntu:16.04
MAINTAINER 1Science <devops@1science.org>

RUN apt-get update
RUN apt-get install -y \
    python-dev \
    python-pip \
    libncurses5-dev

# Install awscli
ADD requirements.txt /dependencies/
RUN pip install -r /dependencies/requirements.txt

RUN apt-get clean autoclean
RUN apt-get autoremove -y
RUN rm -rf /var/lib/{apt,dpkg,cache,log}/

RUN mkdir /root/.ssh
RUN chmod 0700 /root/.ssh
RUN touch /root/.ssh/known_hosts

RUN apt-get install -y jq curl

ADD update_databricks_libs.py /root

WORKDIR /scripts
