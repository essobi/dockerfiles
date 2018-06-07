From ubuntu:trusty  
MAINTAINER Mark Howells  
# Set noninteractive mode for apt-get...  
ENV DEBIAN_FRONTEND noninteractive  
  
# Upgrade base system packages  
RUN apt-get update  
  
### Start editing here ####  
# Install packages (inc. sniproxy)  
RUN apt-get -y install wget \  
&& apt-get -y install python-software-properties \  
&& apt-get -y install software-properties-common  
  
# Install sniproxy  
RUN add-apt-repository ppa:dlundquist/sniproxy \  
&& apt-get update \  
&& apt-get -y install sniproxy \  
&& mkdir /var/run/sniproxy \  
&& chmod 777 /var/run/sniproxy  
  
# Install supervisor  
RUN apt-get -y install python-setuptools \  
&& easy_install supervisor  
COPY supervisord.conf /etc/  
  
# Install consul-template  
RUN wget -O - https://releases.hashicorp.com/consul-template/0.13.0/consul-
template_0.13.0_linux_amd64.zip | gunzip > /bin/consul-template  
RUN chmod +x /bin/consul-template  
  
COPY consul-template/ /etc/consul-template/  
  
# Install utility scripts  
COPY sniproxyctl /usr/local/bin/  
RUN chmod a+x /usr/local/bin/sniproxyctl  
  
# Finish up  
EXPOSE 80  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]  

