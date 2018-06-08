FROM phusion/baseimage:latest  
MAINTAINER Ericson Cepeda <ericson@picorb.com>  
  
# Install Nginx  
RUN apt-get install -y software-properties-common  
#RUN add-apt-repository ppa:nginx/stable  
#RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys B9316A7BC7917B12
&& \  
# add-apt-repository "deb http://ppa.launchpad.net/chris-lea/nginx-
devel/ubuntu trusty main" && \  
# add-apt-repository -s "deb http://ppa.launchpad.net/chris-lea/nginx-
devel/ubuntu trusty main"  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62
&& \  
add-apt-repository "deb http://nginx.org/packages/mainline/ubuntu/ trusty
nginx" && \  
add-apt-repository -s "deb http://nginx.org/packages/mainline/ubuntu/ trusty
nginx" && \  
add-apt-repository -y ppa:certbot/certbot  
RUN apt-get update  
RUN apt-get install -y nginx curl host certbot  
RUN curl https://dl.eff.org/certbot-auto -o /usr/bin/certbot-auto  
RUN chmod +x /usr/bin/certbot-auto  
  
# Install confd  
RUN curl -L
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64 -o confd  
RUN mv confd /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
# Create directories  
RUN mkdir -p /etc/confd/conf.d  
RUN mkdir -p /etc/confd/templates  
  
# Add confd files  
ADD *.tmpl /etc/confd/templates/  
ADD *.toml /etc/confd/conf.d/  
ADD nginx.conf /etc/nginx/  
ADD nginx.app /etc/nginx/  
ADD nginx.stream /etc/nginx/  
ADD cli.ini /etc/letsencrypt/  
  
# Remove default site  
# RUN rm -f /etc/nginx/sites-enabled/default  
# Add boot script  
ADD ./boot.sh /opt/boot.sh  
RUN chmod +x /opt/boot.sh  
  
VOLUME ["/etc/nginx/certs"]  
  
# Run the boot script  
CMD /opt/boot.sh  

