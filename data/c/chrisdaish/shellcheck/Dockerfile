FROM fedora:21  
MAINTAINER Chris Daish <chrisdaish@gmail.com>  
  
ENV shellcheckVersion 0.4.3  
ENV shellcheckTag v$shellcheckVersion  
  
RUN useradd shellcheck; \  
yum install --setopt=tsflags=nodocs --nogpgcheck --assumeyes --quiet cabal-
install \  
tar \  
&& yum clean all \  
&& rm -rf /var/cache/yum  
  
USER shellcheck  
  
RUN cabal update \  
&& curl -Lso /tmp/shellcheck-$shellcheckTag.tar.gz
https://github.com/koalaman/shellcheck/archive/$shellcheckTag.tar.gz \  
&& tar zxf /tmp/shellcheck-$shellcheckTag.tar.gz -C /tmp/ \  
&& rm /tmp/shellcheck-$shellcheckTag.tar.gz \  
&& cabal install /tmp/shellcheck-$shellcheckVersion  
  
CMD ["/home/shellcheck/.cabal/bin/shellcheck", "-s", "bash",
"/tmp/FileToBeChecked"]  

