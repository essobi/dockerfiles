FROM jekyll/jekyll  
  
# From https://github.com/anigeo/docker-awscli/blob/master/Dockerfile  
RUN \  
mkdir -p /aws && \  
apk -Uuv add groff less python py-yaml py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/*  

