FROM alpine:latest  
  
ARG USER_HOME_DIR="/root"  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
curl \  
jq \  
tar \  
docker \  
py-pip \  
python && \  
pip install awscli && \  
apk --purge del py-pip  
  
# Add the m2 cache and src dirs as volumes so that we can mount it into this
image at run  
# time, thus allowing us to call this image to build and output to the current  
# directory  
#  
RUN mkdir -p $USER_HOME_DIR/.m2  
VOLUME $USER_HOME_DIR/.m2  
  
RUN mkdir -p /usr/src/app  
VOLUME /usr/src/app  
WORKDIR /usr/src/app  
  
ADD travis-entrypoint.sh /  
  
ENTRYPOINT ["/travis-entrypoint.sh"]  
CMD ["bash"]  

