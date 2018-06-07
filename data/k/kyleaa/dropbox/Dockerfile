FROM ubuntu:trusty  
  
RUN ln -s -f /bin/true /usr/bin/chfn  
RUN apt-get update && apt-get install -y python wget && apt-get clean -y  
RUN mkdir /home/dropbox  
RUN cd /home/dropbox/ && wget -O -
"http://www.dropbox.com/download?plat=lnx.x86_64" | tar xzf -  
RUN wget -O /home/dropbox/dropbox.py
"http://www.dropbox.com/download?dl=packages/dropbox.py" && chmod 755
/home/dropbox/dropbox.py  
  
ADD run.sh /run.sh  
RUN chmod 775 /run.sh  
  
ENV DROPBOX_UID 1000  
VOLUME /home/dropbox/.dropbox /home/dropbox/Dropbox  
CMD ["/run.sh"]  

