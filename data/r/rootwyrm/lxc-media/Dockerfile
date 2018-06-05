FROM docker.io/rootwyrm/lxc-media:base  
## The magic begins...  
MAINTAINER Phillip "RootWyrm" Jaenke <docker@rootwyrm.com>  
  
## We always use labels.  
## NOTE: Uses TSLE NVD with Substring ISO8601  
LABEL com.rootwyrm.vendor="RootWyrm" \  
com.rootwyrm.project="lxc-media" \  
com.rootwyrm.status="stable" \  
com.rootwyrm.nvd.release="1" \  
com.rootwyrm.nvd.version="0" \  
com.rootwyrm.nvd.update="0" \  
com.rootwyrm.nvd.update_sub="2016-02-09" \  
com.rootwyrm.nvd.hash="81a857d03955ccce8de1bcccc8018badfaac3a0f4eb7f49747e899705f375985"
\  
com.rootwyrm.vcs-type="git" \  
com.rootwyrm.changelog-url="https://www.github.com/rootwyrm/lxc-
media/transmission/CHANGELOG"  
  
LABEL com.rootwyrm.rootcore.base="gliderlabs/alpine" \  
com.rootwyrm.rootcore.base.tag="latest" \  
com.rootwyrm.rootcore.depends="" \  
com.rootwyrm.rootcore.provides="transmission" \  
com.rootwyrm.rootcore.svctype="torrent" \  
com.rootwyrm.rootcore.ports_tcp="9091" \  
com.rootwyrm.rootcore.ports_udp="9091 43454" \  
com.rootwyrm.rootcore.qnap_compatible="true" \  
com.rootwyrm.rootcore.synology_compatible="true"  
## PHASE ZERO  
## Global container variables  
EXPOSE 9091/udp 9091/tcp 43454/udp  
  
## PHASE ONE  
## Common components  
## PHASE TWO  
## Application and support installation  
ENV pkg_application="openssl transmission-daemon dcron apk-cron"  
RUN apk add \--no-cache $pkg_application  
COPY [ "application/", "/opt/rootwyrm/" ]  
COPY [ "sv/", "/etc/sv/" ]  
  
## PHASE THREE  
## Configuration  
## PHASE TEN (from Navarone)  
## Cleanup unsafe/unneeded users...  
ADD README.md /README.md  
  
## TERMINUS  
CMD [ "/sbin/runsvdir", "-P", "/etc/service" ]  

