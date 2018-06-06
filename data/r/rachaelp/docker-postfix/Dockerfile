FROM ubuntu:xenial  
MAINTAINER Rachael Passov <docker@rachael.io>  
  
ADD common/bin /usr/local/bin/  
RUN image-prep  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN lazy-apt \  
# importante  
ssl-cert \  
# meat  
postfix \  
# auth  
sasl2-bin libsasl2-modules \  
# postfix only likes to log to syslog baby  
rsyslog \  
# debugging  
swaks netcat \  
&& :  
RUN useradd -m -U rae \  
&& adduser postfix sasl  
  
ADD etc /etc/  
  
ADD start integration-test /usr/local/bin/  
  
CMD start  
  
EXPOSE 25  

