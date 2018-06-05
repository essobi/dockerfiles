# aptly  
#  
  
FROM ubuntu:17.10  
  
LABEL name="aptly" \  
version="3" \  
description="A Docker image for using aptly" \  
author="takayuki goto <takayuki@idein.jp>"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Install aptly and required tools  
RUN apt-get -q update \  
&& apt-get -y install \  
bash-completion \  
bzip2 \  
gnupg1 \  
gpgv \  
graphviz \  
xz-utils \  
gosu \  
ubuntu-keyring \  
curl \  
dirmngr \  
jq \  
python3-boto3 \  
&& echo "deb http://repo.aptly.info/ squeeze main" >
/etc/apt/sources.list.d/aptly.list \  
&& apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
ED75B5A4483DA07C \  
&& apt-get update -q \  
&& apt-get install aptly \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/var/lib/aptly"]  
  
# ENTRYPOINT ["/entrypoint.sh"]  
CMD ["bash"]  
  

