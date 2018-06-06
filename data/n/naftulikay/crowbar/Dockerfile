FROM lambci/lambda:build-python3.6  
MAINTAINER Naftuli Kay <me@naftuli.wtf>  
  
ENV RUST_USER=rust  
ENV RUST_HOME=/home/${RUST_USER}  
  
ENV _TOOL_PACKAGES="\  
autoconf \  
automake \  
bash-completion \  
cmake \  
curl \  
file \  
gcc \  
git \  
jq \  
libtool \  
make \  
man-db \  
man-pages \  
pcre-tools \  
pkgconfig \  
python-pip \  
python34-pip \  
sudo \  
tree \  
unzip \  
wget \  
which \  
zip \  
"  
ENV _STATIC_PACKAGES="\  
glibc-static \  
openssl-static \  
pcre-static \  
zlib-static \  
"  
ENV _DEVEL_PACKAGES="\  
binutils-devel \  
openssl-devel \  
kernel-devel \  
libcurl-devel \  
libffi-devel \  
pcre-devel \  
python-devel \  
python34-devel \  
xz-devel \  
zlib-devel \  
"  
# upgrade all packages, install epel, then install build requirements  
RUN yum install -y epel-release yum-plugin-ovl >/dev/null && \  
yum upgrade -y > /dev/null && \  
yum install -y ${_TOOL_PACKAGES} ${_STATIC_PACKAGES} ${_DEVEL_PACKAGES} && \  
yum clean all  
  
# install and upgrade pip and utils  
RUN pip install --upgrade pip setuptools && pip install awscli ansible  
  
# create sudo group and add sudoers config  
COPY conf/sudoers.d/50-sudo /etc/sudoers.d/  
RUN groupadd sudo && useradd -G sudo -u 1000 -U ${RUST_USER}  
  
# add rust profile setup  
COPY conf/profile.d/base.sh conf/profile.d/rust.sh /etc/profile.d/  
  
# deploy our tfenv command  
RUN install -o ${RUST_USER} -g ${RUST_USER} -m 0700 -d ${RUST_HOME}/.local
${RUST_HOME}/.local/bin  
COPY bin/tfenv ${RUST_HOME}/.local/bin  
RUN chmod 0755 ${RUST_HOME}/.local/bin/tfenv && \  
chown ${RUST_USER}:${RUST_USER} ${RUST_HOME}/.local/bin/tfenv  
  
# install rustup  
RUN curl -o /tmp/rustup-init -sSf https://static.rust-
lang.org/rustup/dist/x86_64-unknown-linux-gnu/rustup-init && \  
chmod +x /tmp/rustup-init && sudo -u ${RUST_USER} /tmp/rustup-init -y && \  
rm -f /tmp/rustup-init && \  
${RUST_HOME}/.cargo/bin/rustup completions bash | tee
/etc/bash_completion.d/rust >/dev/null && \  
chmod 0755 /etc/bash_completion.d/rust && \  
rsync -a ${RUST_HOME}/.rustup/toolchains/stable-x86_64-unknown-linux-
gnu/share/man/man1/ /usr/local/share/man/man1/  
  
# install stable, beta, and nightly versions of rust  
RUN sudo -u rust bash -lc ' \  
rustup toolchain install stable ; \  
rustup toolchain install beta ; \  
rustup toolchain install nightly ; \  
rustup default stable ; \  
'  
  
# install bash libraries  
RUN mkdir -p /usr/lib  
COPY lib/bash /usr/lib/bash  
  
# install create-deployment  
COPY bin/create-deployment /usr/local/bin/create-deployment  
  
# install id-remap  
COPY bin/id-remap /usr/sbin/id-remap  
  
# install init  
COPY bin/init /usr/sbin/init  
  
# degoss the image  
COPY bin/degoss ./test/ /tmp/  
RUN /tmp/degoss /tmp/goss.yml && rm -fr /tmp/degoss /tmp/goss.yml /tmp/goss.d  
  
WORKDIR ${RUST_HOME}  
ENV ["PATH",
"/home/${RUST_USER}/.cargo/bin:/home/${RUST_USER}/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"]  
  
ENTRYPOINT ["/usr/sbin/init"]  

