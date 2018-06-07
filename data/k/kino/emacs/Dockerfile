FROM centos:7  
ENV pkg ${PKG:-"emacs-25.2.tar.gz"}  
  
WORKDIR /tmp  
  
RUN yum install -y gcc curl ncurses-devel make  
RUN mkdir -p /usr/local/docker  
RUN curl -O http://ftp.gnu.org/pub/gnu/emacs/$pkg && \  
gunzip -c $pkg|tar xvf - && \  
cd emacs* && \  
./configure --prefix=/usr/local/docker --without-x && \  
make install  
  
ADD copy.sh /root/  
  
# -------------------------------  
CMD ["/root/copy.sh"]  

