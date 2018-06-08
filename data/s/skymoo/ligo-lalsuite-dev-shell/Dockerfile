FROM ligo/lalsuite-dev:el7  
  
LABEL name="LALSuite Development Shell - Enterprise Linux 7" \  
maintainer="Adam Mercer <adam.mercer@ligo.org>" \  
date="20180228" \  
support="Best Effort"  
  
# install required packages  
RUN yum -y install \  
emacs \  
sudo \  
tmux \  
vim && \  
yum clean all  
  
# setup environment  
COPY /environment/sudoers.d/albert /etc/sudoers.d/albert  
RUN mkdir /container  
  
# setup user  
RUN useradd -m -d /container/albert -s /bin/bash albert  
COPY /environment/.tmux.conf /container/albert/.tmux.conf  
  
# setup git-lfs  
RUN su - albert -c "git lfs install"  
  
# enter shell  
USER albert  
WORKDIR /container/albert  
CMD ["/bin/bash", "-l"]  

