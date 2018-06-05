FROM alpine:3.5  
ARG CLOUDSDK_VERSION  
ENV CLOUDSDK_VERSION ${CLOUDSDK_VERSION:-160}  
  
RUN apk update && apk upgrade  
  
RUN apk add \  
bash \  
curl \  
ca-certificates \  
python \  
gnupg \  
openssl \  
openssh-client \  
docker  
  
RUN export CLOUDSDK_CORE_DISABLE_PROMPTS=1 && \  
curl https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-$CLOUDSDK_VERSION.0.0-linux-x86_64.tar.gz -o google-cloud-
sdk-$CLOUDSDK_VERSION.0.0-linux-x86_64.tar.gz && \  
tar -zxvf google-cloud-sdk-$CLOUDSDK_VERSION.0.0-linux-x86_64.tar.gz && \  
bash ./google-cloud-sdk/install.sh && \  
unlink google-cloud-sdk-$CLOUDSDK_VERSION.0.0-linux-x86_64.tar.gz  
  
RUN echo "source /google-cloud-sdk/completion.bash.inc" >> ~/.bashrc && \  
echo "source /google-cloud-sdk/path.bash.inc" >> ~/.bashrc  
  
RUN rm -rf /var/cache/apk/* /tmp/* /usr/share/man  
  
CMD bash

