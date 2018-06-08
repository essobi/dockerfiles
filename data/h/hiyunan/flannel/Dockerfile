FROM quay.io/coreos/flannelbox:1.0  
MAINTAINER Eugene Yakubovich <eugene.yakubovich@coreos.com>  
ADD ./flanneld /opt/bin/  
ADD ./mk-docker-opts.sh /opt/bin/  
CMD /opt/bin/flanneld  

