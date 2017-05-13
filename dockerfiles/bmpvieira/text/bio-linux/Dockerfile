# bio-linux
#
# VERSION 8

FROM ubuntu:14.04
MAINTAINER Bruno Vieira <mail@bmpvieira.com>

ENV DEBIAN_FRONTEND noninteractive

RUN sudo su

RUN apt-get update && apt-get install -y wget vim git python software-properties-common

RUN add-apt-repository universe && add-apt-repository multiverse && apt-get update

RUN wget -qO- http://nebc.nerc.ac.uk/downloads/bl8_only/upgrade8.sh | sh && apt-get clean
