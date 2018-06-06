FROM alpine:latest  
  
ENV PYTHON_MAJOR_VERSION=3  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.7.0  
  
ENV PACKAGES="\  
build-base \  
git \  
bash \  
ca-certificates \  
python${PYTHON_MAJOR_VERSION} \  
python${PYTHON_MAJOR_VERSION}-dev \  
clang \  
openssh \  
curl \  
gnupg \  
go \  
"  
  
RUN echo \  
&& if [[ "$PYTHON_MAJOR_VERSION" == '2' ]]; then PACKAGES="$(echo $PACKAGES |
sed -e 's/python2/python/g')"; fi \  
  
&& echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add \--no-cache $PACKAGES || \  
(sed -i -e 's/dl-cdn/dl-4/g' /etc/apk/repositories && apk add \--no-cache
$PACKAGES) \  
  
&& if [[ ! -e /usr/bin/python ]]; then ln -sf
/usr/bin/python${PYTHON_MAJOR_VERSION} /usr/bin/python; fi \  
&& if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python-
config${PYTHON_MAJOR_VERSION} /usr/bin/python-config; fi \  
  
&& if [[ ! -e /usr/bin/idle ]]; then ln -sf
/usr/bin/idle${PYTHON_MAJOR_VERSION} /usr/bin/idle; fi \  
&& if [[ ! -e /usr/bin/pydoc ]]; then ln -sf
/usr/bin/pydoc${PYTHON_MAJOR_VERSION} /usr/bin/pydoc; fi \  
  
&& if [[ ! -e /usr/bin/easy_install ]]; then ln -sf
/usr/bin/easy_install-${PYTHON_MAJOR_VERSION}.* /usr/bin/easy_install; fi \  
  
&& easy_install pip \  
&& pip install \--upgrade pip \  
  
&& if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip${PYTHON_MAJOR_VERSION}
/usr/bin/pip; fi \  
  
&& echo  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
  
COPY ./ /usr/bin  

