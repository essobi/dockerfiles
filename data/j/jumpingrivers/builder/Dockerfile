FROM jumpingrivers/builder:latest  
  
COPY generic-install.sh /tmp/install.sh  
  
ONBUILD COPY Dockerfile install.sh* /tmp/  
ONBUILD COPY Dockerfile install.d* /tmp/install.d/  
ONBUILD USER root  
ONBUILD WORKDIR /tmp  
ONBUILD RUN test -x /tmp/install.sh && /tmp/install.sh || true  
ONBUILD USER trainer  
ONBUILD WORKDIR /src  
  

