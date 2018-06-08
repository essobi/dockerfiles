FROM nginx:1.9.6  
MAINTAINER Stefan Lapers stefan@lapers.be  
  
RUN \  
deps='curl unzip' \  
&& CONSULTEMPLATE_VERSION=0.11.1 \  
&& CONSULTEMPLATE_SHA=e6a5ac6423e277db053a5b34ab973a126056906b \  
\  
&& echo " ------ GETTING DEPENDENCIES ------" \  
&& apt-get update && apt-get install -y --no-install-recommends $deps \  
\  
&& echo " ------ GETTING BINARIES ------" \  
&& mkdir /tmp/src \  
&& curl -L https://releases.hashicorp.com/consul-
template/${CONSULTEMPLATE_VERSION}/consul-
template_${CONSULTEMPLATE_VERSION}_linux_amd64.zip -o /tmp/src/consul-
template.zip \  
\  
&& echo " ------ CHECKING INTEGRITY ------" \  
&& echo "${CONSULTEMPLATE_SHA} /tmp/src/consul-template.zip" >>
/tmp/src/sha1check \  
&& sha1sum -c /tmp/src/sha1check \  
\  
&& echo " ------ SETTING UP CONSULTEMPLATE ------" \  
&& unzip -j /tmp/src/consul-template.zip -d /usr/bin \  
&& mkdir -p /etc/consul-template/templates \  
&& ln -sf /dev/stdout /var/log/consul-template.log \  
\  
&& echo " ------ CLEANUP ------" \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/tmp/src  
  
  
ADD entrypoint.sh /entrypoint.sh  
ADD consul-template.cfg /etc/consul-template/config.cfg  
ADD templates/ /etc/consul-template/templates/  
  
EXPOSE 80 443  
ENTRYPOINT ["/entrypoint.sh"]  

