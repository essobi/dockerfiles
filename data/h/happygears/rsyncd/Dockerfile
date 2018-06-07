  
# base this on the official "bash" image because entrypoint script needs bash  
FROM bash  
  
RUN set -ex; \  
apk add --no-cache --virtual .build-deps rsync  
  
#  
#RUN apt-get update && \  
# DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
rsync && \  
# apt-get clean autoclean && \  
# apt-get autoremove -y && \  
# rm -rf /var/lib/{apt,dpkg,cache,log}/  
EXPOSE 873  
VOLUME /volume  
ADD ./run.sh /run.sh  
RUN chmod +x /run.sh  
ENTRYPOINT ["/run.sh"]  

