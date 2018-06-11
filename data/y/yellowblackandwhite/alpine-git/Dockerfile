FROM yellowblackandwhite/alpine-base  
MAINTAINER Pavel Litvinenko <gerasim13@gmail.com>  
USER root  
RUN apk --update add curl bash git perl  
COPY git_entry_point.sh /  
ENTRYPOINT ["/git_entry_point.sh"]  
USER alpine  

