FROM fedora:21  
MAINTAINER Mikulas Dite <mikulas@mangoweb.cz>  
  
ENV cabalVersion 1.24.0.2  
ENV shellcheckVersion 0.4.5  
# Install dependencies and old Cabal  
RUN yum install --setopt=tsflags=nodocs --nogpgcheck --assumeyes --quiet \  
cabal-install \  
tar \  
zlib-devel \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
# Install Cabal  
RUN curl -Lso /tmp/cabal.tar.gz \  
https://github.com/haskell/cabal/archive/cabal-install-v$cabalVersion.tar.gz \  
&& tar zxf /tmp/cabal.tar.gz -C /tmp/ \  
&& rm /tmp/cabal.tar.gz \  
&& cd /tmp/cabal-cabal-install-v$cabalVersion \  
&& cabal update \  
&& (cd Cabal; cabal install) \  
&& (cd cabal-install; cabal install)  
  
# Download ShellCheck  
RUN curl -Lso /tmp/shellcheck-$shellcheckVersion.tar.gz \  
https://github.com/koalaman/shellcheck/archive/v$shellcheckVersion.tar.gz \  
&& tar zxf /tmp/shellcheck-$shellcheckVersion.tar.gz -C /tmp/ \  
&& rm /tmp/shellcheck-$shellcheckVersion.tar.gz  
  
# Install ShellCheck  
RUN export PATH="/root/.cabal/bin:$PATH" \  
&& cabal update \  
&& cabal install /tmp/shellcheck-$shellcheckVersion  
  
ADD wrapper.sh /usr/bin/shellcheck  
RUN chmod a+x /usr/bin/shellcheck  
  
ENTRYPOINT ["/usr/bin/shellcheck"]  
CMD ["-s", "bash", "*.sh"]  

