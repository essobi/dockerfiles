FROM python:alpine  
  
ENV PACKAGES="\  
musl \  
linux-headers \  
build-base \  
bash \  
git \  
ca-certificates \  
py-setuptools \  
zip \  
groff \  
less \  
jq \  
openssh-client \  
"  
RUN echo \  
# Add the packages, with a CDN-breakage fallback if needed  
&& apk add \--no-cache $PACKAGES || \  
(sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add --no-cache
$PACKAGES) \  
&& pip install dumb-init  
  
WORKDIR /base  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
COPY scripts /base/scripts  
  
ENTRYPOINT ["dumb-init"]  
CMD /bin/bash  

