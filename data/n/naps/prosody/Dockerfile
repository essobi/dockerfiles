FROM debian:stretch  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install adduser python prosody prosody-modules \  
&& apt-get clean  
  
ADD prosody.cfg.lua /default_prosody.cfg.lua  
  
RUN mkdir /prosody  
  
ADD launcher.py /  
RUN chmod +x /launcher.py  
  
RUN chown prosody:prosody -R /prosody && chmod 755 -R /prosody  
  
USER prosody  
  
# 5222 = s2c, 5269 = s2s  
EXPOSE 5222 5269  
# VOLUME /var/logs  
VOLUME /prosody  
  
CMD []  
ENTRYPOINT ["/launcher.py"]  

