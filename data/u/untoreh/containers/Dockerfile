FROM untoreh/chisel-alp  
  
ENV HOME=/home/default  
  
RUN apk add --no-cache tmux sed grep gettext bash  
  
# RUN adduser -D unpriv && \  
# adduser -D dyno && \  
# chown unpriv:dyno -hR $(ls -d /* | grep -Ev "dev|proc|sys")  
# USER unpriv  
ADD services.d /etc/services.d  
  
CMD ["/init"]  

