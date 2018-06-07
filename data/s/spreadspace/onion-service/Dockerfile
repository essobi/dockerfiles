FROM debian:stretch-backports  
MAINTAINER Nicolas Braud-Santoni <nicoo@realraum.at>  
  
RUN set -x \  
&& echo 'APT::Install-Recommends "false";' > /etc/apt/apt.conf.d/02no-
recommends \  
&& echo 'APT::Install-Suggests "false";' >> /etc/apt/apt.conf.d/02no-
recommends \  
&& apt-get update -q \  
&& apt-get install -y -q -t stretch-backports tor \  
&& apt-get install -y -q python3-cryptography \  
&& apt-get upgrade -y -q \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV TINI_VERSION v0.16.1  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini-
static-muslc-amd64 /tini  
RUN chmod +x /tini  
  
RUN adduser --home /srv --no-create-home --system --uid 998 --group app  
  
COPY "run-tor.sh" "/run-tor.sh"  
COPY "torrc" "/torrc"  
COPY "keygen.py" "/keygen.py"  
  
ENV TOR_DIR /var/lib/tor  
VOLUME ["${TOR_DIR}"]  
RUN mkdir -p ${TOR_DIR} && chown app:app ${TOR_DIR}  
  
ENTRYPOINT ["/tini", "--"]  
CMD ["/run-tor.sh"]  
  
USER app  

