FROM gentoo/stage3-amd64  
LABEL maintainer Nicolas LAURENT <docker@aegypius.com>  
  
ADD http://distfiles.gentoo.org/snapshots/portage-latest.tar.bz2 /portage-
latest.tar.bz2  
  
RUN set -x \  
&& tar -jxf /portage-latest.tar.bz2 -C /usr \  
&& emerge -1 app-portage/repoman dev-vcs/git \  
&& rm -fr /portage-latest.tar.bz2 /var/tmp/portage  
  
WORKDIR /overlay  
  
ENTRYPOINT ["repoman"]  
  
CMD ["full"]  

