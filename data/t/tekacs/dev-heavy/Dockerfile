FROM fedora:rawhide  
MAINTAINER Amar Sood <mail@tekacs.com>  
  
EXPOSE 22  
RUN dnf -y update && \  
dnf -y install --allowerasing openssh-server passwd docker xonsh sudo dtach
tmux hostname @c-development @development-tools \  
&& dnf clean all  
  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
COPY entrypoint.sh /  
COPY boot.sh /  
  
CMD ["/boot.sh"]  

