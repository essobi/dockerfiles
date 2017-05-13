FROM python:3.4

ENV \
BASE_APTLIST="build-essential \
	libblas-dev \
	liblapack-dev \
	libatlas-base-dev \
	gfortran \
	mysql-client \
	libmysqlclient-dev \
	postgresql-client \
	libpq-dev \
	sqlite3 \
  libmemcached-dev \
	memcached \
	fftw3-dev"
#	LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"

RUN apt-get update && \
    apt-get install $BASE_APTLIST -qy --no-install-recommends && \
	apt-get -y clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade --quiet \
		wheel \
		setuptools \
		numpy \
		scipy \
		Pillow \
    pytest \
		pyfftw \
		sphinx \
		Cython
