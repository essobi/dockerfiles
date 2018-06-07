FROM roninkenji/slackware-base:latest  
MAINTAINER roninkenji  
  
RUN mkdir -p /dropbox  
WORKDIR /dropbox  
EXPOSE 17500  
EXPOSE 17500/udp  
  
RUN slackpkg -batch=on -default_answer=yes install glibc-[0-9]* shadow
python-2.7 cxxlibs  
RUN wget -nv -O /usr/local/bin/dropbox.py
https://www.dropbox.com/download?dl=packages/dropbox.py && chmod +x
/usr/local/bin/dropbox.py  
RUN wget -nv -O- https://www.dropbox.com/download?plat=lnx.x86_64 | tar -C
/usr/local -zx && chown -Rv root:root .  
  
ADD dockerinit.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/dockerinit.sh  
ENTRYPOINT ["/usr/local/bin/dockerinit.sh"]  
  

