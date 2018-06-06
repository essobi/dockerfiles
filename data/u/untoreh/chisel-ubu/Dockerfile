FROM untoreh/ububase-heroku  
  
ENV CHISEL_VER=1.2.2  
RUN curl -sOL
https://github.com/jpillora/chisel/releases/download/${CHISEL_VER}/chisel_linux_amd64.gz
&& \  
gunzip chisel_linux_amd64.gz && \  
mv chisel_linux_amd64 /usr/sbin/chisel && \  
chmod +x /usr/sbin/chisel  
  
# RUN adduser -D unpriv && \  
# adduser -D dyno && \  
# chown unpriv:dyno -hR $(ls -d /* | grep -Ev "dev|proc|sys")  
# USER unpriv  
COPY ./services.d /etc/services.d  
  
CMD ["/init"]  

