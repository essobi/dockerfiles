FROM coursemology/evaluator-image-c_cpp:latest
MAINTAINER Coursemology <coursemology@googlegroups.com>

RUN apt-get update && apt-get install -y --force-yes \
	python3.4 \
	python3.4-dev \
	python3-pip \
  git \
	&& pip3 install git+https://github.com/Coursemology/unittest-xml-reporting.git@extra-attributes \
	&& pip3 install timeout-decorator \
  && apt-get remove -y git \
	&& rm -rf /var/lib/apt/lists/* 
ENV PYTHON=/usr/bin/python3.4
