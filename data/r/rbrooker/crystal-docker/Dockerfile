FROM ubuntu  
MAINTAINER Ramon Brooker <rbrooker@aetherealmind.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo exit 101 > /usr/sbin/policy-rc.d; chmod +x /usr/sbin/policy-rc.d  
# for setting  
LABEL crystal_version="0.17.0"  
LABEL llvm_version="llvm-3.8"  
  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 09617FD37CC06B54; echo
"deb http://dist.crystal-lang.org/apt crystal main" >
/etc/apt/sources.list.d/crystal.list  
RUN apt-get update; apt-get -y install crystal llvm colordiff colormake  
# clean extra-files  
# RUN apt-get autoremove -y ; apt-get clean && rm -rf /var/lib/apt/lists/*  
ADD bashrc /root/.bashrc  
ADD bash_aliases /root/.bash_aliases  
  
ADD set-time.sh /set-time.sh  
RUN /set-time.sh  
  
VOLUME ["/scripts"]  
  
CMD ["bash"]  
  

