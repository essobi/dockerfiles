FROM ubuntu:trusty  
  
MAINTAINER NAKAYAMA Masahiro <aki@nekoruri.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y git subversion perl libunicode-japanese-perl  
  
RUN useradd -m -s /bin/bash tiarra  
  
RUN mkdir -p /data/logs /data/conf  
RUN chown tiarra.tiarra /data/logs  
  
WORKDIR /home/tiarra  
RUN svn co http://svn.coderepos.org/share/lang/perl/tiarra/trunk tiarra  
  
COPY init.sh /  
RUN chmod +x /init.sh  
ENTRYPOINT [ "/init.sh" ]  
  
EXPOSE 80 443  
VOLUME [ "/data" ]  

