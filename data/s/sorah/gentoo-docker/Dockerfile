FROM quay.io/sorah/gentoo-base:latest  
MAINTAINER her@sorah.jp  
  
RUN CONFIG_PROTECT_MASK="/etc" dockemerge -v app-portage/flaggie app-
portage/layman app-portage/gentoolkit && \  
flaggie +ipv6 +ssl && \  
(echo 'source /var/lib/layman/make.conf' >> /etc/portage/make.conf)  
  
RUN CONFIG_PROTECT_MASK="/etc" dockemerge -v \  
app-admin/sudo \  
dev-libs/openssl \  
net-analyzer/netcat \  
sys-apps/less \  
net-misc/curl \  
net-dns/bind-tools \  
dev-vcs/git \  
dev-vcs/subversion \  
dev-vcs/mercurial \  
app-misc/jq  

