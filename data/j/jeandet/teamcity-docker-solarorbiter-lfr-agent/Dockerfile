FROM jeandet/teamcity-docker-minimal-agent  
LABEL maintainer "Alexis Jeandet <alexis.jeandet@member.fsf.org>"  
  
RUN dnf install -y git cppcheck bzip2 hg automake autoconf gcc glibc.i686
zlib.i686 ncurses-compat-libs.i686 cmake gcc-c++ tcl  
  
ADD http://www.gaisler.com/anonftp/rcc/bin/linux/sparc-
rtems-4.10-gcc-4.4.6-1.2.21-linux.tar.bz2 /opt/  
ADD http://www.gaisler.com/anonftp/rcc/src/rtems-4.10-1.2.21-src.tar.bz2 /opt/  
  
RUN cd /opt && tar -xf /opt/sparc-rtems-4.10-gcc-4.4.6-1.2.21-linux.tar.bz2 &&
\  
cd /opt/rtems-4.10/src && tar -xf /opt/rtems-4.10-1.2.21-src.tar.bz2 && \  
sed -i
'0,/grspw_hw_reset(pDev);/s/grspw_hw_reset(pDev);/\/\/grspw_hw_reset(pDev);/'
/opt/rtems-4.10/src/rtems-4.10/c/src/lib/libbsp/sparc/shared/spw/grspw.c && \  
make bootstrap && \  
make bootstrap_sparc && \  
make configure-drvmgr && \  
make compile-drvmgr && \  
make install-drvmgr && \  
rm -f /opt/sparc-rtems-4.10-gcc-4.4.6-1.2.21-linux.tar.bz2
/opt/rtems-4.10-1.2.21-src.tar.bz2  
  
  
  
  
RUN echo "" >> /opt/buildagent/conf/buildAgent.dist.properties && \  
echo "system.has_sparc_rtems_for_lfr=true" >>
/opt/buildagent/conf/buildAgent.dist.properties && \  
echo "system.has_cppcheck=true" >>
/opt/buildagent/conf/buildAgent.dist.properties && \  
echo "system.rtems_version=4.10-gcc-4.4.6-1.2.21" >>
/opt/buildagent/conf/buildAgent.dist.properties  
  
  
CMD ["/run-services.sh"]  

