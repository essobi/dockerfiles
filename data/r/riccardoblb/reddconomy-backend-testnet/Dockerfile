FROM riccardoblb/reddcoin:amd64  
  
ENV COIN_SHORT="rdd"  
ENV COIN="reddcoin"  
ADD init_daemon.sh /init_daemon.sh  
ADD init_reddconomy.sh /init_reddconomy.sh  
ADD updater.sh /updater.sh  
ADD reddconomy_updater.sh /reddconomy_updater.sh  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ADD install.sh /install.sh  
RUN chmod +x /install.sh  
RUN bash /install.sh  
  
ENTRYPOINT [ "/usr/bin/supervisord" ]  

