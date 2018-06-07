# Version 1.0 docker-baseensime  
FROM idng/baseensime  
  
MAINTAINER IDNG <docker@idng.com>  
  
COPY emacs/.emacs /root/.emacs  
  
COPY sbt/plugins.sbt /root/.sbt/0.13/plugins/plugins.sbt  
  
RUN mkdir /tempensime && \  
cd /tempensime && \  
sbt -sbt-create gen-ensime && \  
cd / && \  
rm -Rf /tempensime  
  
RUN emacs --daemon && \  
emacsclient -e "(package-install 'ensime)(require 'ensime) (kill-emacs)"  
  
CMD ["/sbin/my_init"]  

