FROM galeone/archlinux-updated-aur  
LABEL maintainer="Alexander Trost <galexrt@googlemail.com>"  
  
ENV NODEJS_VERSION="4.1.2" \  
CAMO_DIR="/home/camo" CAMO_KEY="" \  
PORT="8081"  
RUN pacaur -Syu ca-certificates openssl git nodejs npm gcc-libs --noconfirm  
  
USER root  
RUN useradd -m -s /bin/bash camo  
  
ADD entrypoint.sh /entrypoint.sh  
  
EXPOSE 8081  
VOLUME ["/home/camo"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

