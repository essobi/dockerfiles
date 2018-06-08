FROM debian:jessie  
  
# Install utility scripts  
COPY scripts /scripts  
ENV PATH $PATH:/scripts  
  
RUN set -xe; \  
apt-get-install.sh dnsutils git less make man-db strace sysstat tcpdump; \  
git clone \--depth 1 git://git.kernel.org/pub/scm/docs/man-pages/man-
pages.git; \  
cd man-pages; \  
make; \  
cd ..; \  
rm -rf man-pages; \  
apt-get-purge.sh git make;  
  
CMD ["bash"]  

