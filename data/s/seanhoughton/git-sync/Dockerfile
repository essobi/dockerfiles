#openweb/git-sync:0.0.1  
FROM golang:1.6-onbuild  
VOLUME ["/git"]  
ENV GIT_SYNC_DEST /git  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]

