FROM debian:stable  
MAINTAINER Johannes Dröge, johannes.droege@uni-duesseldorf.de  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# anonymous volumes  
VOLUME ["/tmp", "/var/tmp"]  
  
# biobox base directory  
ENV BBX_BASE /bbx  
  
# location for container executables  
ENV BBX_BINDIR ${BBX_BASE}/bin  
  
# location of host mounts in the container  
ENV BBX_MNTDIR ${BBX_BASE}/mnt  
  
# container configuration files  
ENV BBX_ETCDIR ${BBX_BASE}/etc  
  
# location for container shared code  
ENV BBX_LIBDIR ${BBX_BASE}/lib  
  
# persistent storage, can be linked to named volume  
ENV BBX_CACHEDIR ${BBX_MNTDIR}/cache  
  
# location for task definitions (simple sh syntax)  
ENV BBX_TASKDIR ${BBX_ETCDIR}/tasks.d  
  
# manditory mount point definitions  
ENV BBX_MNTCONF ${BBX_ETCDIR}/mount.conf  
  
# location for user-added programs  
ENV BBX_OPTDIR /opt  
  
# add container functionality  
COPY bbx ${BBX_BASE}  
  
# upgrade to latest debian packages (avoid upgrade:
https://docs.docker.com/articles/dockerfile_best-practices/)  
RUN "$BBX_BINDIR"/dockerfile-install-packages bc python-yaml  
  
# create mandatory directories  
RUN mkdir -p "$BBX_MNTDIR"  
  
# create optional default user  
ENV BBX_RUNUSER bbx  
ENV BBX_RUNGROUP bbx  
RUN groupadd "$BBX_RUNGROUP" || echo "$BBX_RUNGROUP exists."  
RUN useradd -N -g "$BBX_RUNGROUP" "${BBX_RUNUSER}" || echo "$BBX_RUNUSER
exists."  
  
# cleanup all temporary data  
RUN "$BBX_BINDIR"/dockerfile-clean-tmpdata  
  
# default process on container startup (no support for infile variable
substitution in Dockerfile)  
ENTRYPOINT ["/bbx/bin/run"]  
  

