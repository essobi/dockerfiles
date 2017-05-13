#
# This container will allow you to run Bio-Path-Find
#
FROM debian:testing

#
# Authorship
#
MAINTAINER ap13@sanger.ac.uk

#
# Update and Install dependencies
#
RUN apt-get update -qq && apt-get install -y  cpanminus libssl-dev git make gcc autoconf libmodule-install-perl libperl-dev  libextutils-autoinstall-perl libexpat1-dev

#
# Hack to get String::CamelCase to install
#
RUN cpanm ExtUtils::MakeMaker && mkdir /usr/local/share/perl/5.24.1/inc && cp -R /usr/local/share/perl/5.24.1/ExtUtils /usr/local/share/perl/5.24.1/inc

RUN git clone https://github.com/sanger-pathogens/Bio-Path-Find.git && cd Bio-Path-Find && ./install-travis-dependencies.sh

