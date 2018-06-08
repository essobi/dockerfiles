FROM livingstoneonline/drupal  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="GPLv3" \  
"Version"="0.0.1"  
  
# Install Python.  
RUN apt-install \  
build-essential \  
python-dev \  
python-pip \  
python-setuptools \  
&& \  
cleanup  
  
# Install csvkit.  
RUN pip install --upgrade pip && \  
pip install csvkit && \  
cleanup  
  
COPY build/dev /build  
RUN cd ${DRUPAL_ROOT} && drush make -y --no-core --no-cache /build/site.make
&& \  
rm -fr ${DRUPAL_ROOT}/sites/all/libraries/plupload/examples && \  
rm -fr ${DRUPAL_ROOT}/sites/all/modules/features && \  
git clone https://github.com/livingstoneonline/livingstone_online_features.git
${DRUPAL_ROOT}/sites/all/modules/features && \  
cd ${DRUPAL_ROOT}/sites/all/modules/features && \  
git checkout -b dev origin/dev; \  
chown -R www-data:www-data ${DRUPAL_ROOT} && \  
cleanup  
  
COPY rootfs /  

