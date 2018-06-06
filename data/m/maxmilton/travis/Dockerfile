# Run the travis CLI via a container  
#  
# Build image:  
# docker build -t local/travis .  
#  
# Update:  
# docker build --no-cache -t local/travis .  
#  
  
FROM
ruby:alpine@sha256:e46f839001cb722b426f264361ba8743556960bc7088735dd6eb5173ab9e1056  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
build-base \  
&& apk add --no-cache git \  
&& gem install travis --no-rdoc --no-ri \  
&& apk del .build-deps \  
# unset SUID on all files  
&& for i in $(find / -perm /6000 -type f); do chmod a-s $i; done  
  
WORKDIR project  
  
ENTRYPOINT ["travis"]  

