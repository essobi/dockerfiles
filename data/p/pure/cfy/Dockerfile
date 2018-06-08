FROM centos:7  
MAINTAINER Andrew Taranik  
  
RUN yum -y -q \--nogpgcheck update \  
&& yum -y -q \--nogpgcheck install which python-setuptools \  
&& easy_install --quiet --upgrade --no-deps pip virtualenv \  
&& curl -sSL http://repository.cloudifysource.org/org/cloudify3/3.3.1/sp-
RELEASE/cloudify-centos-Core-cli-3.3.1-sp_b310.x86_64.rpm -o cfy.rpm \  
&& rpm --quiet -i cfy.rpm \  
&& rm -f cfy.rpm \  
&& yum -y -q clean all \  
&& rm -rf ~/.cache \  
&& echo -e "#!/bin/sh\nsource /opt/cfy/env/bin/activate && cfy \$*"
>/bin/run_cfy \  
&& chmod +x /bin/run_cfy  
  
RUN mkdir -p /cfy  
WORKDIR /cfy  
  
VOLUME /cfy  
  
#ENTRYPOINT ["run_cfy"]  
#CMD ["-h"]  
CMD run_cfy -h  

