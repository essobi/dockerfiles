FROM docker:18.03.0-ce-dind  
  
ENV AWSCLI_VERSION 1.15.4  
ENV YAMLLINT_VERSION 1.11.1  
RUN \  
apk --no-cache add git openssl python py-pip bash gettext jq \  
&& pip install -Iv --upgrade \  
pip \  
awscli==${AWSCLI_VERSION} \  
yamllint==${YAMLLINT_VERSION} \  
&& apk del py-pip \  
&& mkdir ~/.aws  
  
VOLUME ["~/.aws"]  
  
ENTRYPOINT []  

