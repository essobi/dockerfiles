FROM showpass/python-django  
  
# CircleCI  
RUN apk update  
RUN apk add git tar gzip openssl openssh-client  
  
# Docker client  
RUN set -x \  
&& VER="17.03.0-ce" \  
&& curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$VER.tgz \  
&& mv /tmp/docker/* /usr/bin  
  
# gcloud client  
RUN CLOUDSDK_CORE_DISABLE_PROMPTS=1 curl https://sdk.cloud.google.com | bash  
  
# gcloud dependencies  
RUN /root/google-cloud-sdk/bin/gcloud components install kubectl \  
&& /root/google-cloud-sdk/bin/gcloud components install beta  
  
# Add gcloud to PATH  
ENV PATH="/root/google-cloud-sdk/bin:${PATH}"

