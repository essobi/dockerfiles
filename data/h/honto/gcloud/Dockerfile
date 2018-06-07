FROM honto/java:8u111  
MAINTAINER tsukasa.tamaru<tsukasa.tamaru@2dfacto.co.jp>  
  
RUN apk --update --no-cache add python git tar php5 go  
  
# google cloud sdk  
RUN wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip
&& unzip google-cloud-sdk.zip && rm google-cloud-sdk.zip  
RUN google-cloud-sdk/install.sh --usage-reporting=true \--path-update=true
\--bash-completion=true \--rc-path=/.bashrc --additional-components app
kubectl alpha beta  
  
# docker  
ENV DOCKER_BUCKET get.docker.com  
ENV DOCKER_VERSION latest  
  
RUN set -x \  
&& curl -fSL
"https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz" -o
docker.tgz \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v  
COPY docker-entrypoint.sh /usr/local/bin/  
  
# Finalize  
RUN mkdir /.ssh  
VOLUME ["/root/.config"]  
ENV PATH $PATH:/google-cloud-sdk/bin  
CMD ["bash"]  
  

