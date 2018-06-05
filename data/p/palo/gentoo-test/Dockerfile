  
FROM gentoo/stage3-amd64  
MAINTAINER Ingolf Wagner <docker@ingolf-wagner.de>  
  
COPY localOverlay /etc/portage/repos.conf/localOverlay  
COPY run.sh /ebuilds/run.sh  
  
# install some tools  
RUN emerge --sync \  
&& emerge \  
app-portage/repoman \  
app-portage/gentoolkit \  
app-text/tree \  
dev-vcs/git \  
&& rm -rf /usr/portage  
  
WORKDIR /ebuilds  
CMD ./run.sh  

