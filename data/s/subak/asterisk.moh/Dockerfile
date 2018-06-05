FROM busybox  
MAINTAINER Subak Systems <info@subak.jp>  
  
ENV AST_MOH_DIR /var/lib/asterisk/moh  
  
RUN mkdir -p $AST_MOH_DIR  
  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-moh-
opsound-g729-current.tar.gz $AST_MOH_DIR  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-moh-opsound-
sln16-current.tar.gz $AST_MOH_DIR  
ADD http://downloads.asterisk.org/pub/telephony/sounds/asterisk-moh-opsound-
wav-current.tar.gz $AST_MOH_DIR  
  
WORKDIR $AST_MOH_DIR  
RUN for s in g729 sln16 wav; do tar zxvf asterisk-moh-
opsound-$s-current.tar.gz; done  
  
RUN rm -f $AST_MOH_DIR/*.tar.gz  
  
VOLUME [ $AST_MOH_DIR ]  
CMD [ "echo", "Asterisk Music On Hold DVC"]  

