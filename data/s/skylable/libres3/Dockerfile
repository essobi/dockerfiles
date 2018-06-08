FROM centos:centos7  
MAINTAINER Skylable Dev-Team <dev-team@skylable.com>  
  
# Install deps  
RUN yum clean all && \  
yum -y install epel-release && \  
yum -y install ocaml ocaml-camlp4-devel ocaml-camlp4 \  
ocaml-compiler-libs ocaml-runtime pcre-devel openssl-devel make m4 \  
which ncurses-devel git openssl libev-devel libev && \  
yum clean all && \  
git clone http://git.skylable.com/libres3 && \  
cd libres3/ && \  
./configure --prefix=/usr --sysconfdir=/data/etc --localstatedir=/var && \  
make && make install && \  
cd .. && rm -rf libres3 && \  
yum remove -y ocaml ocaml-camlp4-devel ocaml-camlp4 \  
ocaml-compiler-libs ocaml-runtime pcre-devel openssl-devel m4 \  
which ncurses-devel git libev-devel && \  
yum autoremove -y && \  
yum clean all  
  
ADD mime.types /etc/  
  
COPY run.sh /  
  
EXPOSE 443 80  
CMD ["/run.sh"]  

