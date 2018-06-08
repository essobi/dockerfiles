FROM python  
  
WORKDIR /opt/  
RUN git clone \--recursive https://github.com/Al-Azif/ps4-exploit-host.git  
RUN sed -i "s|/usr/bin/python3|/usr/bin/env python3 |g" ps4-exploit-
host/start.py  
EXPOSE 53/udp 53/tcp 80/tcp  
CMD /opt/ps4-exploit-host/start.py  

