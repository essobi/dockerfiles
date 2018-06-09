FROM golang:1.9-alpine  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
LABEL ca.unb.lib.daemon="git-lfs"  
LABEL vcs-ref="alpine"  
LABEL vcs-url="https://github.com/unb-libraries/docker-git-lfs-reference-
server"  
LABEL vendor="University of New Brunswick Libraries"  
  
ENV LFS_LISTEN tcp://:6983  
ENV LFS_HOST localhost:6983  
ENV LFS_CONTENTPATH /data  
ENV LFS_ADMINUSER notadmin  
ENV LFS_ADMINPASS notadminpass  
ENV LFS_SCHEME http  
  
COPY ./scripts /scripts  
RUN apk --update add git && \  
rm -f /var/cache/apk/* && \  
go get github.com/github/lfs-test-server && \  
go install github.com/github/lfs-test-server  
  
VOLUME /data  
EXPOSE 6983  
CMD /scripts/run.sh  

