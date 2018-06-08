FROM fedora:latest  
  
LABEL maintainer="zdm <zdm@softvisio.net>"  
  
USER root  
  
ENV TZ=UTC \  
PERL_VERSION="5.26.2" \  
PERL_CPANM_OPT="--metacpan --from https://cpan.metacpan.org/" \  
PERL_CPANM_HOME=/tmp/.cpanm \  
PCORE_LIB="/var/local" \  
DIST_PATH="/var/local/pcore"  
ENV PATH="$DIST_PATH/bin:/usr/perlbrew/perls/perl-$PERL_VERSION/bin:$PATH" \  
PERL5LIB="$DIST_PATH/lib"  
  
ADD . $DIST_PATH  
  
WORKDIR $DIST_PATH  
  
# --develop  
RUN /bin/bash -c ' \  
\  
# install prereqs  
dnf -y install ca-certificates wget \  
\  
# setup host  
&& source <( wget -q -O -
https://bitbucket.org/softvisio/scripts/raw/tip/setup-host.sh || echo false )
\  
\  
# setup perl build env  
&& source <( wget -q -O -
https://bitbucket.org/softvisio/scripts/raw/tip/perl-build-env.sh || echo
false ) setup \  
\  
# install && update perl  
&& dnf -y install perl-$PERL_VERSION \  
&& source <( wget -q -O -
https://bitbucket.org/softvisio/scripts/raw/tip/perl-exclusions-install.sh ||
echo false ) \  
&& cpanm App::cpanoutdated \  
&& cpan-outdated | cpanm \  
\  
# deploy pcore  
&& perl bin/pcore deploy --recommends --suggests \  
&& pcore test -j $(nproc) \  
\  
# cleanup perl build env  
&& source <( wget -q -O -
https://bitbucket.org/softvisio/scripts/raw/tip/perl-build-env.sh || echo
false ) cleanup \  
'  

