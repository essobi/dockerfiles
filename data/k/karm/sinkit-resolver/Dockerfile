FROM fedora:22  
MAINTAINER Michal Karm Babacek <karm@email.cz>  
#LABEL description="Codename Feed: Sinkit Recursive Resolver"  
# TODO: Optimize this out. GO build tool chain is too heavy.  
ENV DEPS unbound go supervisor wget unzip git wget  
#ENV GODNS_TAG playground  
ENV GODNS_TAG logging-disabled-core  
#ENV GODNS_REPO github.com/intfeed/godns  
ENV GODNS_REPO github.com/Karm/godns  
ENV GOPATH /home/sinkit/go  
RUN dnf -y update && dnf -y install ${DEPS} && dnf clean all  
  
RUN useradd -s /sbin/nologin sinkit  
  
USER sinkit  
  
# GoDNS  
RUN go get ${GODNS_REPO} && \  
echo "Got GoDNS." && \  
cd ${GOPATH}/src/${GODNS_REPO}/ && \  
git checkout ${GODNS_TAG} && \  
echo "Switched to tag ${GODNS_TAG}." && \  
go build && \  
echo "Built GoDNS." && \  
cp godns /home/sinkit/ && \  
ls -lah ./ && \  
cd /home/sinkit/ && \  
ls -lah ./ && \  
rm -rf ${GOPATH}  
ADD godns.conf /home/sinkit/godns.conf  
  
USER root  
  
RUN ls -lah /home/sinkit/  
RUN setcap 'cap_net_bind_service=+ep' /home/sinkit/godns  
  
# Unbound  
ADD unbound.conf /etc/unbound/unbound.conf  
RUN wget -O /etc/unbound/named.cache
ftp://ftp.internic.net./domain/named.cache  
  
# Supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 53/tcp  
EXPOSE 53/udp  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf",
"-n"]  

