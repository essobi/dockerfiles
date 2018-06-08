FROM gems/concourse-fuselage  
  
RUN apk-install git ca-certificates openssl-dev \  
&& update-ca-certificates \  
&& apk del openssl-dev \  
&& gem-install concourse-github-status  
  
WORKDIR /opt/resource  
  
RUN find $(gem environment gemdirs) -type f -path '*/concourse-github-
status-*/bin/*' -exec ln -s '{}' \;  

