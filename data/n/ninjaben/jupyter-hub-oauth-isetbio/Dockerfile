# ninjaben/jupyter-hub-oauth-isetbio  
#  
# Add isetbio toolboxes to the JupyterHub OAuth Matlab image
(ninjaben/jupyter-hub-oauth-matlab)  
#  
FROM ninjaben/jupyter-hub-oauth-matlab  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
# remote data toolbox and gradle will need java  
RUN apt-get install -y openjdk-7-jre  
  
# pre-deploy a few toolboxes to a shared folder expected by toolbox-toolbox  
RUN git clone \--depth=1 https://github.com/isetbio/isetbio.git /srv/toolbox-
toolbox/toolboxes/isetbio  
RUN git clone \--depth=1 https://github.com/isetbio/RemoteDataToolbox.git
/srv/toolbox-toolbox/toolboxes/RemoteDataToolbox  
RUN git clone \--depth=1 https://github.com/isetbio/IBIOColorDetect.git
/srv/toolbox-toolbox/toolboxes/IBIOColorDetect  
  
# let jupyter group pull on these repos  
RUN git -C /srv/toolbox-toolbox/toolboxes/isetbio pull \  
&& chown -R :jupyter /srv/toolbox-toolbox/toolboxes/isetbio \  
&& chmod -R g+w /srv/toolbox-toolbox/toolboxes/isetbio/ \  
&& git -C /srv/toolbox-toolbox/toolboxes/isetbio config core.sharedRepository
group  
RUN git -C /srv/toolbox-toolbox/toolboxes/RemoteDataToolbox pull \  
&& chown -R :jupyter /srv/toolbox-toolbox/toolboxes/RemoteDataToolbox \  
&& chmod -R g+w /srv/toolbox-toolbox/toolboxes/RemoteDataToolbox/ \  
&& git -C /srv/toolbox-toolbox/toolboxes/RemoteDataToolbox config
core.sharedRepository group  
RUN git -C /srv/toolbox-toolbox/toolboxes/IBIOColorDetect pull \  
&& chown -R :jupyter /srv/toolbox-toolbox/toolboxes/IBIOColorDetect \  
&& chmod -R g+w /srv/toolbox-toolbox/toolboxes/IBIOColorDetect/ \  
&& git -C /srv/toolbox-toolbox/toolboxes/IBIOColorDetect config
core.sharedRepository group  
  
# add a common toolbox configuration to shared folder expected by toolbox-
toolbox  
# this allows automatic update of above toolboxes  
# each user can modify this with additional toolboxes  
COPY toolbox-config.json /srv/toolbox-toolbox/toolbox-config.json  
  

