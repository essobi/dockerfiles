FROM busybox  
MAINTAINER Subak Systems <info@subak.jp>  
  
ENV AST_SOUNDS_DIR /var/lib/asterisk/sounds  
  
RUN mkdir -p $AST_SOUNDS_DIR  
  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-
ja-gsm-current.tar.gz $AST_SOUNDS_DIR  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-
ja-sln16-current.tar.gz $AST_SOUNDS_DIR  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-
ja-wav-current.tar.gz $AST_SOUNDS_DIR  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-core-sounds-
ja-ulaw-current.tar.gz $AST_SOUNDS_DIR  
  
WORKDIR $AST_SOUNDS_DIR  
RUN for s in gsm sln16 wav ulaw; do tar zxvf asterisk-core-sounds-
ja-$s-current.tar.gz; done  
  
RUN rm -f $AST_SOUNDS_DIR/*.tar.gz  
  
VOLUME [ $AST_SOUNDS_DIR ]  
CMD [ "echo", "Asterisk Sounds"]  

