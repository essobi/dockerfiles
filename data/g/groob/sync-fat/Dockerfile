FROM alpine:3.3  
ENV FAT_VERSION 0.5.0  
ENV GIT_SYNC_BRANCH master  
  
ADD https://github.com/groob/git-sync-fat/releases/download/v0.0.2/git-sync-
linux-amd64 /git-sync  
RUN apk add --update git python openssh rsync  
RUN apk add --update --virtual build-dependencies curl && \  
curl -sLO https://github.com/cyaninc/git-fat/archive/${FAT_VERSION}.tar.gz &&
\  
tar xzf /${FAT_VERSION}.tar.gz -C / && \  
mv /git-fat-${FAT_VERSION}/git_fat/git_fat.py /usr/local/bin/git-fat && \  
chmod +x /usr/local/bin/git-fat && chmod +x /git-sync && \  
apk del build-dependencies && \  
rm -rf /git-fat-${FAT_VERSION} && \  
rm -rf /${FAT_VERSION}.tar.gz && \  
rm -rf /var/cache/apk/*  
  
CMD ["/git-sync"]  

