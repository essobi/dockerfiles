FROM alpine  
MAINTAINER Gerard Lynch <gerard@halberom.co.uk>  
  
RUN apk add \--no-cache --update weechat weechat-perl weechat-python perl
python bash  
  
ENV LANG C.UTF-8  
ENV HOME /home/user  
  
#Create user to run screen/weechat  
RUN mkdir -p $HOME/.weechat && \  
addgroup user && \  
adduser -h $HOME -D -s /bin/bash -G user user && \  
chown -R user:user $HOME  
#Expose for persistance  
VOLUME $HOME/.weechat  
  
WORKDIR $HOME  
USER user  
  
EXPOSE 9001  
  
CMD ["weechat"]  

