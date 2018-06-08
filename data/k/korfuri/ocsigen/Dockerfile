FROM ubuntu:saucy  
MAINTAINER Uriel Corfa "uriel@corfa.fr"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq -y update  
RUN apt-get -qq -y upgrade  
RUN apt-get -qq -y install libyojson-ocaml-dev ocsigenserver ocsigenserver-doc
libcalendar-ocaml-doc libcalendar-ocaml-dev libextlib-ocaml-dev libcurl-ocaml-
dev git-core build-essential make eliom libeliom-ocaml libeliom-ocaml-dev
libeliom-ocaml-doc nodejs npm nano wget curl  
RUN npm install -g less  
RUN mkdir /etc/ocsigenserver/conf.d  

