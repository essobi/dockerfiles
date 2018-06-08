FROM gems/concourse-fuselage  
  
RUN apk-install ca-certificates openssl-dev \  
&& update-ca-certificates \  
&& apk del openssl-dev \  
&& gem-install concourse-resource-rubygems  
  
RUN find $(gem environment gemdirs) -type f -path '*/concourse-resource-
rubygems-*/bin/*' -exec ln -s '{}' \;  

