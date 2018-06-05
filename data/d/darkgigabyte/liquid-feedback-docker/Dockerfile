#  
# Dockerfile for liquid-feedback  
#  
FROM debian:jessie  
  
MAINTAINER Pascal Schneider <https://github.com/DarkGigaByte>  
  
ENV LF_CORE_VERSION 3.2.2  
ENV LF_FEND_VERSION 3.2.1  
ENV LF_WMCP_VERSION 2.1.0  
ENV LF_MOONBRIDGE_VERSION 1.0.1  
ENV LF_LATLON_VERSION 0.12  
#  
# install dependencies  
#  
RUN apt-get update && apt-get -y remove exim && apt-get -y install \  
build-essential \  
ssmtp \  
imagemagick \  
libpq-dev \  
lua5.2 \  
liblua5.2-0 \  
liblua5.2-0-dbg \  
liblua5.2-dev \  
mercurial \  
postgresql \  
postgresql-server-dev-9.4 \  
python-pip \  
pmake \  
libbsd-dev \  
curl \  
&& pip install markdown2 \  
&& ln -s `which ssmtp` /usr/bin/sendmail  
  
#  
# prepare file tree  
#  
RUN mkdir -p /opt/lf/sources/patches \  
/opt/lf/sources/scripts \  
/opt/lf/bin  
  
WORKDIR /opt/lf/sources  
  
#  
# Download sources  
#  
RUN hg clone -r v${LF_CORE_VERSION} http://www.public-software-
group.org/mercurial/liquid_feedback_core/ ./core \  
&& hg clone -r v${LF_FEND_VERSION} http://www.public-software-
group.org/mercurial/liquid_feedback_frontend/ ./frontend \  
&& hg clone -r v${LF_WMCP_VERSION} http://www.public-software-
group.org/mercurial/webmcp ./webmcp  
  
RUN curl -o moonbridge.tar.gz http://www.public-software-
group.org/pub/projects/moonbridge/v${LF_MOONBRIDGE_VERSION}/moonbridge-v${LF_MOONBRIDGE_VERSION}.tar.gz
\  
&& tar -xvf moonbridge.tar.gz  
  
#  
# Build moonbridge  
#  
RUN cd /opt/lf/sources/moonbridge-v${LF_MOONBRIDGE_VERSION} \  
&& pmake MOONBR_LUA_PATH=/opt/lf/moonbridge/?.lua \  
&& mkdir /opt/lf/moonbridge \  
&& cp moonbridge /opt/lf/moonbridge/ \  
&& cp moonbridge_http.lua /opt/lf/moonbridge/  
  
#  
# build core  
#  
WORKDIR /opt/lf/sources/core  
  
RUN make \  
&& cp lf_update lf_update_issue_order lf_update_suggestion_order /opt/lf/bin  
  
#  
# build WebMCP  
#  
WORKDIR /opt/lf/sources/webmcp  
  
RUN make \  
&& mkdir /opt/lf/webmcp \  
&& cp -RL framework/* /opt/lf/webmcp  
  
WORKDIR /opt/lf/  
  
RUN cd /opt/lf/sources/frontend \  
&& hg archive -t files /opt/lf/frontend \  
&& cd /opt/lf/frontend/fastpath \  
&& make \  
&& chown www-data /opt/lf/frontend/tmp  
  
#  
# setup db  
#  
RUN cp /opt/lf/sources/core/core.sql /opt/lf/  
COPY ./scripts/config_db.sql /opt/lf/  
  
RUN addgroup --system lf \  
&& adduser --system --ingroup lf --no-create-home --disabled-password lf  
  
#  
# cleanup  
#  
RUN rm -rf /opt/lf/sources \  
&& apt-get -y purge \  
build-essential \  
liblua5.2-dev \  
libpq-dev \  
mercurial \  
postgresql-server-dev-9.4 \  
python-pip \  
&& apt-get -y autoremove \  
&& apt-get clean  
  
#  
# configure everything  
#  
# app config (for running container without -v)  
COPY ./scripts/lfconfig.lua /opt/lf/frontend/config/  
# app config (for copy-if-not-exists when running container with -v)  
COPY ./scripts/lfconfig.lua /tmp/  
  
# update script  
COPY ./scripts/lf_updated /opt/lf/bin/  
  
# startup script  
COPY ./scripts/start.sh /opt/lf/bin/  
  
#  
# ready to go  
#  
EXPOSE 8080  
VOLUME /opt/lf/frontend/config/  
  
WORKDIR /opt/lf/frontend  
  
ENTRYPOINT ["/opt/lf/bin/start.sh"]  

