FROM ubuntu:14.04  
MAINTAINER Varun Mittal <varun91@uw.edu>  
MAINTAINER Somebody <somebody@acme.com>  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
RUN apt-get update  
RUN apt-get install -y --force-yes --no-install-recommends software-
properties-common  
#orangeml.json  
add http://biolab.github.io/install-orange/setup-ubuntu.sh /data/setup-
ubuntu.sh  
RUN chmod +x /data/setup-ubuntu.sh  
RUN cd /data/ && /data/setup-ubuntu.sh  
#--  
#novnc.json  
#broker_base.json  
RUN apt-get install -y --force-yes --no-install-recommends python-django
python-pip build-essential python-dev  
RUN pip install librabbitmq mongoengine  
RUN apt-get purge -y --force-yes python-pip build-essential python-dev  
copy lib/broker_base/broker.tar.gz /  
#--  
add lib/broker_base/init.sh /bef7fd33-9270-456a-8153-36cceb04a70f  
RUN apt-get install -y --force-yes --no-install-recommends supervisor openssh-
server pwgen sudo vim-tiny  
RUN apt-get install -y --force-yes --no-install-recommends net-tools lxde
x11vnc x11vnc-data xvfb  
RUN apt-get install -y --force-yes --no-install-recommends gtk2-engines-
murrine ttf-ubuntu-font-family  
RUN apt-get install -y --force-yes --no-install-recommends nginx  
RUN apt-get install -y --force-yes --no-install-recommends python-pip python-
dev build-essential  
RUN apt-get install -y --force-yes --no-install-recommends mesa-utils
libgl1-mesa-dri  
add lib/novnc/web /web/  
RUN pip install -r /web/requirements.txt  
RUN apt-get purge -y --force-yes python-pip python-dev build-essential  
add lib/novnc/noVNC /noVNC/  
add lib/novnc/nginx.conf /etc/nginx/sites-enabled/default  
add lib/novnc/startup.sh /  
add lib/novnc/supervisord.conf /etc/supervisor/conf.d/  
add lib/novnc/doro-lxde-wallpapers /usr/share/doro-lxde-wallpapers/  
#--  
RUN apt-get purge software-properties-common -y --force-yes  
RUN apt-get -y autoclean  
RUN apt-get -y autoremove  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/*  
RUN rm -rf /var/tmp/*  
WORKDIR /root/  
EXPOSE 6080  
RUN bash -c 'echo -e "#!/bin/bash\nchmod +x
/bef7fd33-9270-456a-8153-36cceb04a70f\n/bef7fd33-9270-456a-8153-36cceb04a70f\n/startup.sh"
>> /entrypoint.sh'  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

