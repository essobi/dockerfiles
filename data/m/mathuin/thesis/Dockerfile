FROM ubuntu:xenial  
MAINTAINER Jack Twilley <twilleyj@lifetime.oregonstate.edu>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key E084DAB9  
RUN echo 'deb http://cran.rstudio.com/bin/linux/ubuntu xenial/' >>
/etc/apt/sources.list  
RUN apt update && apt install -y \  
biber \  
build-essential \  
latexmk \  
r-base \  
texlive-latex-extra \  
texlive-latex-recommended \  
texlive-science \  
texlive-xetex && \  
apt clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# https://gist.github.com/stevenworthington/3178163  
# In R code:  
# packages <\- c("ggplot2", "plyr", "reshape2", "RColorBrewer", "scales",
"grid")  
# ipak(packages)  
RUN echo 'r = getOption("repos")\n\  
r["CRAN"] = "https://cran.bnr.berkeley.edu"\n\  
options(repos=r)\n\  
rm(r)\n\  
ipak <\- function(pkg){\n\  
new.pkg <\- pkg[!(pkg %in% installed.packages()[, "Package"])]\n\  
if (length(new.pkg) > 0)\n\  
install.packages(new.pkg, dependencies = TRUE)\n\  
sapply(pkg, require, character.only = TRUE)\n\  
}' > /root/.Rprofile  
  
RUN echo '#!/bin/bash\n\  
source /root/.bashrc\n\  
if [ "$#" -ne 1 ]; then\n\  
"$@"\n\  
else\n\  
make realclean thesis.pdf\n\  
fi' > /root/docker-entrypoint.sh  
RUN chmod +x /root/docker-entrypoint.sh  
  
RUN echo '#!/bin/bash\n\  
chown --reference=/data -R /data\n\  
' > /root/cleanup.sh  
RUN chmod +x /root/cleanup.sh  
  
RUN echo 'trap /root/cleanup.sh EXIT\n\  
' > /root/.bashrc  
RUN chmod +x /root/.bashrc  
  
VOLUME ["/data"]  
WORKDIR "/data"  
  
ARG BUILD_DATE  
ARG VERSION  
ARG VCS_REF  
ARG VCS_URL  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="CC BY-SA 4.0" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url=$VCS_URL  
  
ENTRYPOINT ["/root/docker-entrypoint.sh"]  
CMD ["/bin/bash"]  

