FROM bastilimbach/docker-magicmirror  
  
LABEL maintainer="Jean-Pierre Palik - kama@palik.fr" \  
description="MagicMirror personnal image based from bastilimbach/docker-
magicmirror" \  
version="1.1"  
  
RUN git clone \--depth 1 -b master https://github.com/jvanoost/MMM-SNCF.git
/opt/magic_mirror/modules/MMM-SNCF && \  
git clone \--depth 1 -b master https://github.com/PtrBld/MMM-Scrobbler.git
/opt/magic_mirror/modules/MMM-Scrobbler  
  
WORKDIR /opt/magic_mirror/modules/MMM-SNCF  
  
RUN npm install  
  
WORKDIR /opt/magic_mirror  
  
EXPOSE 8080  
CMD ["node serveronly"]  
ENTRYPOINT ["/opt/docker-entrypoint.sh"]  

