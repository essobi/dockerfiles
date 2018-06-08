FROM debian:jessie  
  
ENV ATOM_VERSION v1.9.9  
ENV DEBIAN_FRONTEND=noninteractive  
ENV RUST_VERSION=1.11.0  
ENV RUST_ARCHIVE=rust-${RUST_VERSION}-x86_64-unknown-linux-gnu.tar.gz  
ENV RUST_DOWNLOAD_URL=https://static.rust-lang.org/dist/$RUST_ARCHIVE  
ENV RUST_ARCHIVE_SRC=rustc-${RUST_VERSION}-src.tar.gz  
ENV RUST_DOWNLOAD_SRC=https://static.rust-lang.org/dist/$RUST_ARCHIVE_SRC  
ENV RUST_SRC_PATH=/rustsrc/src  
ENV GOSU_VERSION 1.9  
# SYSTEM INSTALLS  
RUN apt-get update && \  
apt-get install \  
ca-certificates \  
curl \  
gcc \  
libc6-dev \  
git \  
curl \  
ca-certificates \  
libgtk2.0-0 \  
libxtst6 \  
libnss3 \  
libgconf-2-4 \  
libasound2 \  
fakeroot \  
gconf2 \  
gconf-service \  
libcap2 \  
libnotify4 \  
libxtst6 \  
libnss3 \  
gvfs-bin \  
xdg-utils \  
python \  
-qqy \  
\--no-install-recommends  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
#RUST INSTALL  
RUN mkdir /rust && mkdir /rustsrc  
  
WORKDIR /rust  
  
RUN curl -fsOSL $RUST_DOWNLOAD_URL \  
&& curl -s $RUST_DOWNLOAD_URL.sha256 | sha256sum -c - \  
&& tar -C /rust -xzf $RUST_ARCHIVE \--strip-components=1 \  
&& rm $RUST_ARCHIVE \  
&& ./install.sh  
  
WORKDIR /rustsrc  
  
RUN curl -fsOSL $RUST_DOWNLOAD_SRC \  
&& curl -s $RUST_DOWNLOAD_SRC.sha256 | sha256sum -c - \  
&& tar -C /rustsrc -xzf $RUST_ARCHIVE_SRC \--strip-components=1 \  
&& rm $RUST_ARCHIVE_SRC  
  
#ATOM INSTALLATION  
RUN curl -L
https://github.com/atom/atom/releases/download/${ATOM_VERSION}/atom-amd64.deb
> /tmp/atom.deb && \  
dpkg -i /tmp/atom.deb && \  
rm -f /tmp/atom.deb  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# see https://github.com/atom/atom/issues/4360  
#RUN cp /usr/lib/x86_64-linux-gnu/libxcb.so.1 /usr/share/atom/ \  
# && sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/share/atom/libxcb.so.1  
RUN useradd -u 1000 -d /home/atom -m atom && \  
mkdir -p /home/atom/project && \  
mkdir -p /home/atom/project_template  
  
USER atom  
RUN cargo install racer  
ENV PATH=$PATH:/home/atom/.cargo/bin  
RUN apm install build  
RUN apm install build-cargo  
RUN apm install language-rust  
RUN apm install linter  
RUN apm install linter-rust  
RUN apm install platformio-ide-terminal  
RUN apm install racer  
RUN apm install rust-api-docs-helper  
RUN apm install busy  
RUN apm install atom-browser-webview  
USER root  
  
  
  
  
ADD project /home/atom/project/  
ADD project /home/atom/project_template/  
ADD config.cson /home/atom/.atom/config.cson  
ADD styles.less /home/atom/.atom/styles.less  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh && chown -R atom:atom /home/atom && cp -R
/home/atom/.atom /home/atom/.atom_template  
  
ENV USER=atom  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["atom", "/usr/bin/atom","-f", "/home/atom/project"]  
  

