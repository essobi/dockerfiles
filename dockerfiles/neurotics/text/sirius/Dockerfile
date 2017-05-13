FROM ubuntu:14.04
MAINTAINER TAYAA Med Amine <tayamino@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

ENV PORT 8080
ENV SIRIUS_HOME /opt/sirius
ENV SIRIUS_APP  /opt/sirius/sirius-application
ENV SIRIUS_WEB  /opt/sirius/sirius-web

RUN export PORT=$PORT
RUN export SIRIUS_HOME=$SIRIUS_HOME
RUN export SIRIUS_APP=$SIRIUS_APP
RUN export SIRIUS_WEB=$SIRIUS_WEB

RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise main restricted universe multiverse" >> /etc/apt/sources.list;\
	echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-updates main restricted universe multiverse" >> /etc/apt/sources.list;\
	echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-backports main restricted universe multiverse" >> /etc/apt/sources.list;\
	echo "deb mirror://mirrors.ubuntu.com/mirrors.txt precise-security main restricted universe multiverse" >> /etc/apt/sources.list

RUN apt-get update;\
	apt-get install -y \
	apt-utils \
	git wget unzip \
	libfaac-dev vim sudo aptitude \
	python-pip python-dev subversion\
	build-essential ruby
RUN pip install --upgrade pip
RUN pip install --upgrade virtualenv
RUN pip install pickledb
RUN gem install --no-rdoc --no-ri foreman
RUN aptitude install -y sox

RUN git clone https://bitbucket.org/uchikoma/sirius.git $SIRIUS_HOME --recursive

WORKDIR $SIRIUS_HOME/sirius-application

RUN $SIRIUS_APP/get-dependencies.sh
RUN $SIRIUS_APP/get-kaldi.sh
RUN $SIRIUS_APP/get-opencv.sh

#RUN $SIRIUS_APP/compile-sirius-servers.sh
#RUN $SIRIUS_APP/image-matching/make-db.py landmarks $SIRIUS_HOME/sirius-application/image-matching/matching/landmarks/db/
WORKDIR $SIRIUS_HOME

RUN foreman start

#VOLUME $SIRIUS_APP/question-answer/
EXPOSE 8080 8081 8082 8083
