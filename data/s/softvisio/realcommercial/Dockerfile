FROM softvisio/pcore:v0.66.0  
  
LABEL maintainer="zdm <zdm@softvisio.net>"  
  
USER root  
  
ENV DIST_PATH="$PCORE_LIB/realcommercial"  
  
ADD . $DIST_PATH  
  
WORKDIR $DIST_PATH  
  
RUN /bin/bash -c ' \  
  
# setup perl build env  
source <( wget -q -O - https://bitbucket.org/softvisio/scripts/raw/tip/perl-
build-env.sh || echo false ) setup \  
  
# deploy  
&& pcore deploy \--recommends \--suggests \  
&& pcore test -j $(nproc) \  
  
# cleanup perl build env  
&& source <( wget -q -O -
https://bitbucket.org/softvisio/scripts/raw/tip/perl-build-env.sh || echo
false ) cleanup \  
'  
  
ENTRYPOINT ["bin/main.pl"]  

