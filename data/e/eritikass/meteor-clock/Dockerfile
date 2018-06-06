FROM ulexus/meteor  
  
# install meteor for build  
RUN curl https://install.meteor.com/ | sh  
  
# build and place into image  
COPY . /tmp/meteor_build  
RUN cd /tmp/meteor_build \  
&& ./add_buildinfo.sh \  
&& npm install \  
&& meteor build --directory meteor_build --allow-superuser \  
&& mv meteor_build /home/meteor/www \  
&& chown -R meteor:meteor /home/meteor/ \  
&& rm -fr /tmp/meteor_build  
  
# todo: remove meteor?  

