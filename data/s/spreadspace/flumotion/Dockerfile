FROM debian:wheezy  
MAINTAINER Christian Pointner <equinox@spreadspace.org>  
  
COPY spreadspace-build.asc /root  
  
RUN set -x \  
&& echo 'deb http://build.spreadspace.org/ wheezy main' >>
/etc/apt/sources.list \  
&& echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/02no-
recommends \  
&& echo 'APT::Install-Suggests "false";' >> /etc/apt/apt.conf.d/02no-
recommends \  
&& apt-key add /root/spreadspace-build.asc \  
&& apt-get update -q \  
&& apt-get install -y -q tzdata flumotion flumotion-decklink gstreamer-tools \  
&& apt-get upgrade -y -q \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN adduser --home /srv --no-create-home --system --uid 998 --group app  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-muslc-amd64 /tini  
COPY run_flumotion.sh /run_flumotion.sh  
RUN chmod +x /tini /run_flumotion.sh  
ENTRYPOINT ["/tini", "--", "/run_flumotion.sh"]  
  
WORKDIR /srv  
USER app  

