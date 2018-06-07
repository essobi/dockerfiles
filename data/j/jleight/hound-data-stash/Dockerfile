FROM python:2  
MAINTAINER Jonathon Leight <jonathon.leight@jleight.com>  
  
ENV CFG_GIST_ID 8723c837c5322172c983  
ENV CFG_VERSION 3edaa5b7b926d8b0ea0c6ea98b87346997a905a6  
ENV CFG_BASEURL https://gist.githubusercontent.com/platan/${CFG_GIST_ID}/raw  
ENV CFG_URL ${CFG_BASEURL}/${CFG_VERSION}/prepare_hound_config.py  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
&& pip install stashy \  
&& mkdir /hound \  
&& curl -o /hound/config.py "${CFG_URL}"  
  
ADD config.sh /hound/config.sh  
  
VOLUME ["/hound"]  
CMD ["/hound/config.sh"]  

