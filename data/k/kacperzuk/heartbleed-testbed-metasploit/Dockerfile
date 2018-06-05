FROM remnux/metasploit  
RUN bash -c 'source /usr/local/rvm/scripts/rvm && /etc/init.d/postgresql start
&& /opt/msf/msfupdate --git-branch master && /etc/init.d/postgresql stop'  
  
RUN mkdir /scripts/  
ADD init.sh /usr/local/bin/  
ADD ftp-hb.rc /scripts/  
ADD http-hb.rc /scripts/  
RUN chmod +x /usr/local/bin/init.sh  
  
CMD /usr/local/bin/init.sh  

