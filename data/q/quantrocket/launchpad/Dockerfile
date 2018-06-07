FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
COPY qrocket /tmp/uwsgi/qrocket  
COPY uwsgi /etc/uwsgi  
  
RUN mkdir -p /var/lib/launchpad/registrations \  
&& mkdir -p /codeload \  
&& /tmp/build.sh  

