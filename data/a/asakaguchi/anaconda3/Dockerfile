FROM alpine:3.6  
  
LABEL maintainer "autumngoodluck@gmail.com"  
  
ENV LOCALE=ja_JP \  
ENCODING=UTF-8 \  
GLIBC_VERSION=2.25-r0 \  
GLIBC_URL=https://github.com/sgerrand/alpine-pkg-glibc/releases/download \  
GLIBC_KEY=sgerrand.rsa.pub \  
CONDA_VERSION=4.4.0 \  
CONDA_INSTALLER_URL=https://repo.continuum.io/archive \  
PATH=/opt/conda/bin:$PATH  
ENV LC_ALL="${LOCALE}.${ENCODING}" \  
LANG="${LOCALE}.${ENCODING}"  
  
RUN set -x \  
&& apk --update --no-cache add \  
bash \  
openssl \  
tini \  
libxext \  
libsm \  
libxrender \  
ncurses5-widec-libs \  
ruby \  
ruby-json \  
zeromq-dev \  
&& apk --no-cache --virtual build-dependencies add \  
autoconf \  
automake \  
build-base \  
libffi-dev \  
libtool \  
ruby-dev \  
&& cd /tmp \  
&& wget -q -O "/etc/apk/keys/${GLIBC_KEY}"
"${GLIBC_URL}/${GLIBC_VERSION}/${GLIBC_KEY}" \  
&& wget "${GLIBC_URL}/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" \  
&& wget "${GLIBC_URL}/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" \  
&& wget "${GLIBC_URL}/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk" \  
&& apk add "glibc-${GLIBC_VERSION}.apk" "glibc-bin-${GLIBC_VERSION}.apk"
"glibc-i18n-${GLIBC_VERSION}.apk" \  
&& /usr/glibc-compat/bin/localedef -i "${LOCALE}" -f "${ENCODING}" "${LANG}" \  
&& wget "${CONDA_INSTALLER_URL}/Anaconda3-${CONDA_VERSION}-Linux-x86_64.sh" -O
anaconda.sh \  
&& bash /tmp/anaconda.sh -b -p /opt/conda \  
&& conda install --yes -c conda-forge \  
jupyter_contrib_nbextensions \  
tensorflow \  
&& conda update --yes \--all \  
&& conda clean --yes \--tarballs \  
&& conda clean --yes \--packages \  
&& gem install rubygems-update --source http://rubygems.org/ --no-document &&
update_rubygems --no-document \  
&& gem install \  
iruby \  
ffi-rzmq \  
pry \  
pry-doc \  
awesome_print \  
gnuplot \  
rubyvis \  
nyaplot \  
\--no-document \  
&& iruby register \  
&& apk del build-dependencies \  
&& rm -rf /tmp/*  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/bin/bash"]

