FROM debian  
MAINTAINER littleqz@gmail.com  
LABEL description="Dropbox cli shipped with debian."  
  
RUN apt-get update && \  
apt-get install -y wget python  
  
RUN useradd -mU -u 1000 -s /bin/bash me && \  
mkdir -p /home/me/Dropbox && \  
chown -R me:me /home/me/Dropbox  
  
RUN cd /home/me && wget -O -
"https://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf - && \  
ln -sf /home/me/.dropbox-dist/dropboxd /usr/bin/dropboxd  
  
RUN wget -O /usr/bin/dropbox
https://www.dropbox.com/download?dl=packages/dropbox.py && \  
chmod +x /usr/bin/dropbox && \  
apt-get purge -y wget  
  
VOLUME ["/home/me/Dropbox"]  
USER me  
  
CMD ["dropboxd"]  

