FROM centos AS buildcontainer  
  
RUN yum -y install gcc-c++ autoconf openssl-devel automake libtool libcurl-
devel make curl openssl-devel git  
  
RUN git clone https://github.com/BOINC/boinc.git  
  
RUN cd boinc &&\  
./_autosetup &&\  
./configure --disable-server --disable-manager --build=i686-pc-linux-gnu
CXXFLAGS="-O3 -funroll-loops -fforce-addr -ffast-math" &&\  
make  
  
RUN mkdir /deplibs && ldd /boinc/client/boinc | cut -d'>' -f 2 | cut -d'(' -f
1 | tr -d '[:blank:]' | xargs cp -t /deplibs && cp /lib64/libnss_dns.so.2
/deplibs  
  
FROM scratch  
  
COPY \--from=buildcontainer /boinc/client/boinc /  
COPY \--from=buildcontainer /boinc/client/boinccmd /  
COPY \--from=buildcontainer /deplibs /lib64  
COPY gui_rpc_auth.cfg /boinchome/gui_rpc_auth.cfg  
VOLUME /boinchome  
EXPOSE 31416  
CMD ["/boinc", "--allow_remote_gui_rpc", "--dir", "/boinchome"]  

