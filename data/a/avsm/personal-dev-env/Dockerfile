FROM alpine  
MAINTAINER Anil Madhavapeddy <anil@recoil.org>  
RUN apk add \--update alpine-sdk openssh  
RUN adduser -S -u 501 -g 20 avsm  
RUN echo "avsm ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
RUN echo "PACKAGER=\"Anil Madhavapeddy <anil@recoil.org>\"" >>
/etc/abuild.conf  
RUN addgroup avsm abuild  
RUN chgrp abuild /var/cache/distfiles  
RUN chmod g+w /var/cache/distfiles  
USER avsm  
WORKDIR /home/avsm  
RUN git config \--global user.name "Anil Madhavapeddy"  
RUN git config \--global user.email "anil@recoil.org"  

