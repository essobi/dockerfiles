FROM konstruktoid/alpine  
  
ENV USER irssi  
ENV HOME /home/$USER  
ENV LANG C.UTF-8  
RUN apk update && \  
apk upgrade && \  
apk --update add ca-certificates irssi && \  
adduser -D -h $HOME $USER && \  
mkdir -p $HOME/.irssi && \  
chown -R $USER:$USER $HOME && \  
rm -rf /var/cache/apk/*  
  
WORKDIR $HOME  
VOLUME $HOME/.irssi  
  
USER $USER  
ENTRYPOINT ["/usr/bin/irssi"]  
CMD []  

