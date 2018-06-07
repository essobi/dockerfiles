FROM alpine:3.7  
RUN apk add --no-cache \  
bash \  
curl \  
openssl \  
python  
  
ARG DEHYDRATED_TAG=v0.5.0  
ARG LETSENCRYPT_OVH_HOOK=3ca3207f02d7a7c82e6cd637ec2a6200e3d0928  
RUN apk add --no-cache tar && \  
mkdir -p dehydrated && \  
curl -L
https://github.com/lukas2511/dehydrated/archive/${DEHYDRATED_TAG}.tar.gz | tar
-C dehydrated --strip-components 1 -xzf - && \  
mkdir -p dehydrated/hooks/ovh && \  
curl -L https://github.com/Rbeuque74/letsencrypt-ovh-
hook/archive/${LETSENCRYPT_OVH_HOOK}.tar.gz | tar -C dehydrated/hooks/ovh
--strip-components 1 -xzf - && \  
apk del --no-cache tar  
  
RUN apk add --no-cache py2-pip && \  
pip install -r dehydrated/hooks/ovh/requirements.txt && \  
rm -r /root/.cache && \  
apk del --no-cache py2-pip  
  
RUN mkdir /etc/dehydrated && \  
sed \  
-e 's/#CHALLENGETYPE=.*/CHALLENGETYPE="dns-01"/' \  
-e 's@#HOOK=.*@HOOK=/dehydrated/hooks/ovh/hook.py@' \  
/dehydrated/docs/examples/config > /dehydrated/config  
  
COPY /docker-entrypoint.sh .  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
  
RUN mkdir /var/run/dehydrated  
  
WORKDIR /var/run/dehydrated  
  

