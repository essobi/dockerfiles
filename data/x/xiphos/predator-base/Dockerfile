FROM alpine:3.6  
  
ENV ALPINE_VERSION=3.6  
  
ENV PACKAGES="\  
dumb-init \  
musl \  
linux-headers \  
build-base \  
bash \  
git \  
gcc \  
g++ \  
curl\  
ca-certificates \  
python3.4 \  
python3.4-dev \  
openblas \  
openblas-dev \  
libstdc++ \  
"  
  
ENV PIP_PACKAGES="\  
dateparser \  
pandas \  
python-whois \  
requests \  
numpy==1.11.0 \  
scipy==0.18.0 \  
scikit-learn==0.18.1 \  
progressbar33 \  
blessings \  
pyasn \  
"  
  
  
RUN echo \  
# replacing default repositories with edge ones  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
# Install all the stuff we need for running AND compiling  
&& apk add \--no-cache $PACKAGES \  
&& if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3.4
/usr/bin/python; fi \  
&& if [[ ! -e /usr/bin/python3 ]]; then ln -sf /usr/bin/python3.4
/usr/bin/python3; fi \  
&& if [[ ! -e /usr/bin/python-config ]]; then ln -sf /usr/bin/python3.4-config
/usr/bin/python-config; fi \  
&& if [[ ! -e /usr/bin/idle ]]; then ln -sf /usr/bin/idle3.4 /usr/bin/idle; fi
\  
&& if [[ ! -e /usr/bin/pydoc ]]; then ln -sf /usr/bin/pydoc3.4 /usr/bin/pydoc;
fi \  
&& if [[ ! -e /usr/bin/easy_install ]]; then ln -sf /usr/bin/easy_install-3.4
/usr/bin/easy_install; fi \  
# Install and upgrade Pip  
&& easy_install pip \  
&& pip install \--upgrade pip \  
&& if [[ ! -e /usr/bin/pip ]]; then ln -sf /usr/bin/pip3.4 /usr/bin/pip; fi \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
# Install and compile modules  
&& pip3 install $PIP_PACKAGES \  
# Clean up and remove the stuff we do not need anymore  
&& apk del curl g++ make musl-dev libc-dev git gcc build-base openblas-dev
gfortran libc-utils \--no-cache  
  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD /usr/bin/python  

