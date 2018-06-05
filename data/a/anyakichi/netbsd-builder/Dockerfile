FROM debian  
MAINTAINER INAJIMA Daisuke <inajima@sopht.jp>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential \  
ccache \  
cvs \  
git \  
sudo \  
zlib1g-dev \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
ADD https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 \  
/usr/local/bin/gosu  
ADD https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64.asc \  
/usr/local/bin/gosu.asc  
RUN \  
export GNUPGHOME="$(mktemp -d)" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 && \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu && \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc && \  
chmod +x /usr/local/bin/gosu && \  
gosu nobody true  
  
COPY mk.conf /etc/  
  
RUN useradd -ms /bin/bash builder  
USER builder  
RUN \  
echo '. <(buildenv init)' >> ~/.bashrc && \  
mkdir -m 700 ~/.ssh && \  
printf "Host anoncvs.NetBSD.org\n\tStrictHostKeyChecking no\n" \  
>> ~/.ssh/config  
  
USER root  
WORKDIR /home/builder  
  
ENV \  
BUILD_MACH="amd64" \  
BUILD_OPTS="" \  
CVSROOT="anoncvs@anoncvs.NetBSD.org:/cvsroot" \  
CVS_CO_OPTS="-P" \  
CVS_OPTS="-z6" \  
NETBSD_TAG=""  
COPY buildenv/entrypoint.sh /usr/local/sbin/entrypoint  
COPY buildenv/buildenv.sh /usr/local/bin/buildenv  
  
COPY buildenv/buildenv.conf /etc/  
COPY buildenv.d/ /etc/buildenv.d/  
  
RUN sed -i 's/^#DOTCMDS=.*/DOTCMDS=setup/' /etc/buildenv.conf  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint"]  
CMD ["/bin/bash"]  

