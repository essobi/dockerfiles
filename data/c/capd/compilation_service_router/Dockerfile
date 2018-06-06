# we need distcc 3.2, for BACKOFF_PERRIOD support  
FROM fedora:24  
MAINTAINER Mateusz Juda <mateusz.juda@gmail.com>  
RUN dnf -y update && dnf -y install ccache distcc distcc-server && dnf clean
all  
  
  
COPY scripts /usr/local/scripts  
  
ENV PATH_ORG="$PATH" \  
PATH_DISTCC="/usr/local/scripts/distcc:$PATH" \  
PATH_CCACHE="/usr/local/scripts/ccache:$PATH" \  
TMPDIR="/workdir/tmp" \  
CCACHE_DIR="/workdir/ccache" \  
CCACHE_PREFIX="distcc-wrap.sh" \  
CCACHE_MAXSIZE="5G" \  
DISTCC_DIR="/workdir/distcc" \  
DISTCC_IO_TIMEOUT=900 \  
DISTCC_SKIP_LOCAL_RETRY=1 \  
DISTCC_FALLBACK=0 \  
DISTCC_BACKOFF_PERIOD=0 \  
DISTCC_HOSTS="" \  
ALLOW="0.0.0.0/32" \  
PORT="3632" \  
JOBS="1" \  
DISTCCD_OPTS=""  
  
WORKDIR /workdir  
ENTRYPOINT ["/usr/local/scripts/start.sh"]  

