FROM gliderlabs/alpine:3.3  
MAINTAINER Enrico Maria Carmona, e.carmona@asst-monza.it  
  
ENV HOME /root  
ENV REPOS_DIR=${HOME}/repos \  
BITBUCKET_USER=enricomariam42 \  
BITBUCKET_REPOS=test  
  
RUN apk-install mercurial \  
openssh-client  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["hg"]  
VOLUME ["${REPOS_DIR}"]  
  

