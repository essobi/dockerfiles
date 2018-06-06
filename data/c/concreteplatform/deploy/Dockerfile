FROM docker:stable-git  
  
# Install curl/nodejs/npm/yarn + dependencies  
RUN apk update && \  
apk add --no-cache --update \  
bash \  
c-ares-dev \  
openssl \  
openssl-dev \  
ca-certificates \  
binutils-gold \  
curl-dev \  
curl \  
autoconf \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
nodejs \  
nodejs-npm \  
&& rm -r /var/cache/apk \  
&& rm -r /usr/share/man  
  
RUN curl
"https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get" | bash  
RUN helm init --client-only && \  
helm plugin install "https://github.com/hypnoglow/helm-s3.git"  
  
RUN apk --no-cache add --virtual .awscli-deps py2-pip py-setuptools && \  
apk --no-cache add groff less python2 && \  
pip --no-cache-dir install awscli && \  
apk del .awscli-deps  
  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --rc  
ENV PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"  
  

