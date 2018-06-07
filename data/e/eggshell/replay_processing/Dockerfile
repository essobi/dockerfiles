FROM python:3.6-alpine  
MAINTAINER Cullen Taylor <CullenTaylor@outlook.com>  
  
RUN apk add --no-cache git \  
&& pip3 install -U pip && pip3 install -e
git+git://github.com/GraylinKim/sc2reader#egg=sc2reader \  
&& pip3 install -e
git+git://github.com/StoicLoofah/spawningtool.git#egg=spawningtool \  
&& pip3 install -e
git+git://github.com/nibalizer/replay_processing.git#egg=replay_processing \  
&& rm -rf /var/lib/apt/lists/*  

