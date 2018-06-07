FROM ubuntu:17.10  
MAINTAINER henrik@rockhopper.dk  
WORKDIR /opt  
  
COPY scripts ./scripts  
COPY etc/duplicity/exclude-common /etc/duplicity/exclude-common  
  
RUN set -ex; \  
export DEBIAN_FRONTEND=noninteractive; export DEBIAN_PRIORITY=critical; export
DEBCONF_NOWARNINGS=yes; \  
apt-get update \  
&& apt-get -y -q --no-install-recommends install software-properties-common \  
&& add-apt-repository ppa:duplicity-team/ppa \  
&& apt-get update \  
&& apt-get -y -q --no-install-recommends install
duplicity=0.7.16-0ubuntu1ppa1347~ubuntu17.10.1 python-paramiko \  
&& apt-get clean -y \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache /var/lib/dpkg/info
/user/share/man \  
&& mkdir /backup  
  
ENTRYPOINT ["./scripts/entry"]  
CMD ["/usr/bin/duplicity", "--help"]  
  
ARG VCS_REF="local"  
LABEL org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/henrik-farre/duplicity-
docker.git" \  
org.label-schema.version="0.7.16-1"  

