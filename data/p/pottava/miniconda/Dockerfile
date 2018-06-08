# Miniconda v4.4  
  
FROM alpine:3.7  
  
ENV CONDA_VERSION=4.4.10 \  
GLIBC_VERSION=2.27-r0 \  
PATH=/opt/conda/bin:$PATH \  
LANG=C.UTF-8  
  
RUN apk \--no-cache add \--virtual build-deps bash curl libgcc \  
  
# Install GNU libc  
&& GLIBC_DL_URL="https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}" \  
&& curl \--location \--silent \--show-error -O
${GLIBC_DL_URL}/glibc-${GLIBC_VERSION}.apk \  
&& curl \--location \--silent \--show-error -O ${GLIBC_DL_URL}/glibc-
bin-${GLIBC_VERSION}.apk \  
&& curl \--location \--silent \--show-error -O
${GLIBC_DL_URL}/glibc-i18n-${GLIBC_VERSION}.apk \  
&& apk add \--allow-untrusted glibc-${GLIBC_VERSION}.apk \  
glibc-bin-${GLIBC_VERSION}.apk glibc-i18n-${GLIBC_VERSION}.apk \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib \  
&& /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \  
  
# Install Miniconda  
&& mkdir -p /opt/conda \  
&& curl \--location \--silent \--show-error -o miniconda.sh \  
https://repo.continuum.io/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh
\  
&& bash miniconda.sh -f -b -p /opt/conda \  
  
# Clean up  
&& find / -depth -type d -name tests -exec rm -rf {} \; \  
&& find / -depth -type d -name test -exec rm -rf {} \; \  
&& find / -depth -type d -name \\__pycache__ -exec rm -rf {} \; \  
&& find / -depth -type d -name '*.egg-info' -exec rm -rf {} \; \  
&& apk del \--purge -r build-deps glibc-i18n \  
&& rm -rf glibc-*.apk miniconda.sh /opt/conda/pkgs/cache  

