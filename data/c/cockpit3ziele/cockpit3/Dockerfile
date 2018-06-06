FROM softvisio/pcore:v0.48.0  
  
MAINTAINER zdm <zdm@softvisio.net>  
  
USER root  
  
ENV DIST_PATH="$PCORE_LIB/dreiziele-cockpit"  
  
ADD . $DIST_PATH  
  
ADD ./contrib/nginx.repo /etc/yum.repos.d/  
  
ADD ./contrib/ssh-depl-3ziele.key /root/.ssh/ssh-depl-3ziele.key  
  
WORKDIR $DIST_PATH  
  
RUN /bin/bash -c ' \  
  
chmod 600 ~/.ssh/ssh-depl-3ziele.key \  
  
&& hg clone \--ssh "ssh -i ~/.ssh/ssh-depl-3ziele.key"
ssh://hg@bitbucket.org/softvisio/pcore-share-www "$PCORE_LIB/pcore-share-www/"
\  
&& rm -rf "$PCORE_LIB/pcore-share-www/.hg" \  
&& hg clone \--ssh "ssh -i ~/.ssh/ssh-depl-3ziele.key"
ssh://hg@bitbucket.org/softvisio/pcore-share-ext_v6_2_0 "$PCORE_LIB/pcore-
share-ext_v6_2_0/" \  
&& rm -rf "$PCORE_LIB/pcore-share-ext_v6_2_0/.hg" \  
  
# deploy nginx  
&& yum -y install nginx nginx-module-geoip \  
&& yum clean all \  
  
# deploy  
&& pcore deploy \--recommends \--suggests \  
&& pcore test -j $(nproc) \  
&& rm -rf ~/.cpanm \  
'  
  
ENTRYPOINT ["bin/main.pl"]  

