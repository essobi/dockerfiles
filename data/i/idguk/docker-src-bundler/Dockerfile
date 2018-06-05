FROM node:8  
  
ENV DEBCONF_NONINTERACTIVE_SEEN="true" \  
DEBIAN_FRONTEND="noninteractive"  
  
COPY src/entrypoint.sh /opt/  
  
RUN apt-get -qq update \  
&& apt-get -qqy install ruby-full rubygems \  
&& gem update \  
&& yes | gem cleanup -q \  
&& yes | gem uninstall -q -a -x sass \  
&& gem install sass -v 3.4.22 \  
&& gem install compass -v 1.0.3 \  
&& gem install compass-blueprint -v 1.0.0 \  
&& npm install -g webpack@1.13.3 \  
&& npm install -g gulp \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["/opt/entrypoint.sh"]  

