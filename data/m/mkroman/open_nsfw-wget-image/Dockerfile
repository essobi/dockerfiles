FROM kaixhin/caffe:latest  
MAINTAINER Mikkel Kroman <mk@maero.dk>  
  
ENV OPEN_NSFW_REPO "https://github.com/yahoo/open_nsfw.git"  
ENV OPEN_NSFW_REV "59bca2eea844d804c0ed5d981867dc431f0ab096"  
RUN set -x \  
&& mkdir -p /usr/src \  
&& git clone "${OPEN_NSFW_REPO}" /usr/src/open_nsfw \  
&& cd /usr/src/open_nsfw \  
&& git checkout "${OPEN_NSFW_REV}"  
  
COPY classify.sh /usr/src/classify.sh  
RUN chmod +x /usr/src/classify.sh  
  
ENTRYPOINT ["/usr/src/classify.sh"]  

