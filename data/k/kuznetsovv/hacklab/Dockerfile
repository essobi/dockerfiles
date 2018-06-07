FROM library/debian  
  
RUN apt-get update && apt-get install -y build-essential libssl-dev zlib1g-dev
libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev xz-
utils tk-dev libtimedate-perl libnet-ssleay-perl make wget unzip  
RUN wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz -P
/tmp/python36-dist  
RUN tar xzf /tmp/python36-dist/Python-3.6.0.tgz -C /usr/src  
RUN cd /usr/src/Python-3.6.0 && ./configure && make install  
RUN wget https://github.com/sullo/nikto/archive/master.zip -P /tmp/nikto-dist  
RUN cd /tmp/nikto-dist && unzip master.zip && mv nikto-master /opt/nikto  
RUN echo "EXECDIR=/opt/nikto/program" >> /opt/nikto/program/nikto.conf  
RUN ln -s /opt/nikto/program/nikto.conf /etc/nikto.conf  
RUN chmod +x /opt/nikto/program/nikto.pl  
RUN ln -s /opt/nikto/program/nikto.pl /usr/local/bin/nikto  
RUN wget https://github.com/stanislav-web/OpenDoor/archive/master.zip -P
/tmp/opendoor_dist  
RUN cd /tmp/opendoor_dist && unzip master.zip && mv OpenDoor-master
/opt/opendoor  
RUN cd /opt/opendoor && pip3.6 install -r requirements.txt && chmod +x
opendoor.py  
RUN nikto -update  
  
RUN rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*  
  
CMD echo Hacklab is started && tail -f /var/log/wtmp

