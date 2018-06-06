#  
# Based on https://github.com/walm/docker-pgtap/blob/master/Dockerfile  
#  
FROM postgres:latest  
MAINTAINER Damien Clochard <damien.clochard@dalibo.com>  
  
RUN apt-get update \  
&& apt-get install -y build-essential git-core libv8-dev curl postgresql-
server-dev-$PG_MAJOR \  
&& rm -rf /var/lib/apt/lists/*  
  
# install pg_prove  
RUN curl -LO http://xrl.us/cpanm \  
&& chmod +x cpanm \  
&& ./cpanm TAP::Parser::SourceHandler::pgTAP  
  
# install pgtap  
RUN git clone git://github.com/theory/pgtap.git \  
&& cd pgtap \  
&& make \  
&& make install  
  

