FROM gliderlabs/alpine:3.3  
MAINTAINER arnaudsj@gmail.com  
  
# Build dependencies  
RUN apk --update add --no-cache --virtual=build-dependencies wget ca-
certificates bash  
  
# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/andyshinn/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r1" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
wget --quiet \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/andyshinn.rsa.pub" \  
-O "/etc/apk/keys/andyshinn.rsa.pub" && \  
wget --quiet \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
rm "/etc/apk/keys/andyshinn.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV LANG=C.UTF-8  
# Install Miniconda2 (Python 2.7.x) & clean up Alpine install  
RUN wget --quiet
https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh && \  
/bin/bash Miniconda2-4.0.5-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda2-4.0.5-Linux-x86_64.sh && \  
apk del build-dependencies && \  
echo 'export PATH=/opt/conda/bin:$PATH' >> /etc/profile.d/conda.sh  
  
# Install Jupyter, Pandas, Scikit-learn, numpy  
RUN /opt/conda/bin/conda install --quiet --yes numpy jupyter pandas scikit-
learn && \  
/opt/conda/bin/conda clean --yes --all  
  
# Adding Tini (init for containers)  
ENV
ALPINE_EDGE_TESTING_REPO=http://dl-4.alpinelinux.org/alpine/edge/community/  
RUN echo "@edge ${ALPINE_EDGE_TESTING_REPO}" >> /etc/apk/repositories  
RUN apk --update add tini@edge  
  
RUN mkdir -p /notebooks  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/opt/conda/bin/jupyter", "notebook", "--no-browser"]  

