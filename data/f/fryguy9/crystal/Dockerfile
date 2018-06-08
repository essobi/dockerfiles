FROM fedora:20  
RUN curl -sL https://copr.fedorainfracloud.org/coprs/postmodern/ruby-
install/repo/fedora-25/postmodern-ruby-install-fedora-25.repo -o
/etc/yum.repos.d/ruby-install.repo && \  
sed -i 's/\$releasever/25/g' /etc/yum.repos.d/ruby-install.repo  
  
RUN sed -i '1 a tsflags=nodocs' /etc/yum.conf  
  
# NOTE: rpm --rebuilddb is used to fix issue: Rpmdb checksum is invalid:
dCDPT(pkg checksums)  
# See https://github.com/moby/moby/issues/10180#issuecomment-190429512  
# Fix issues with fedora:20 images and being able to install openssl. While
the  
# usual solution is to use `yum distro-sync` (as noted in  
# https://github.com/fedora-cloud/docker-brew-
fedora/issues/19#issuecomment-253166264),  
# this causes a lot of bloat in the docker image. Instead, we can just  
# downgrade the specific packages causing problems.  
RUN rpm --rebuilddb && \  
yum -y downgrade krb5-libs 1.11.5-19.fc20 && \  
yum clean all  
RUN rpm --rebuilddb && \  
yum -y downgrade openssl-libs 1.0.1e-42.fc20 && \  
yum clean all  
  
RUN rpm --rebuilddb && \  
yum -y install \  
ruby-install \  
make \  
git \  
llvm-devel-3.3 \  
libunwind-devel \  
gcc-c++ \  
which && \  
yum clean all  
  
RUN ln -s /usr/bin/llvm-config /usr/bin/llvm-config-3.3  
  
RUN rpm --rebuilddb && \  
ruby-install --system ruby 1.9.3-p547 -- --disable-install-doc --enable-shared
&& \  
rm -rf /usr/local/src/* && \  
yum clean all  
  
RUN echo "gem: --no-ri --no-rdoc --no-document" > ~/.gemrc && \  
gem install bundler && \  
gem install debugger-ruby_core_source -v 1.3.8  
  
RUN git clone https://github.com/crystal-lang/crystal /opt/crystal && \  
cd /opt/crystal && \  
git checkout ruby && \  
rm -rf .git && \  
bundle  
  
ENV PATH /opt/crystal/bin:$PATH  
WORKDIR ~  

