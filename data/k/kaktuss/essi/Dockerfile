FROM debian:8  
  
ENV GOSU_VERSION=1.10  
ENV
GOSU_SHA256=5b3b03713a888cee84ecbf4582b21ac9fd46c3d935ff2d7ea25dd5055d302d3c  
  
ENV
CPANM_SHA256=d2221f1adb956591fa43cd61d0846b961be1fffa222210f097bfd472a11e0539  
  
RUN \  
apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
curl git libcommon-sense-perl build-essential \  
libextutils-makemaker-cpanfile-perl dh-make-perl apt-file ssh-client \  
dnsutils libanyevent-perl libmodule-install-perl \  
libmodule-install-xsutil-perl libmodule-install-authortests-perl \  
libmodule-build-xsutil-perl ca-certificates wget \  
libdata-validate-domain-perl \  
  
# Build fixes for some modules  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
libclass-xsaccessor-perl \  
  
&& cd /bin \  
&& curl -L https://cpanmin.us/ -o cpanm \  
&& echo -n "$CPANM_SHA256 cpanm" | sha256sum -c \- \  
&& chmod +x cpanm \  
  
&& cpanm Module::Install::TestTarget \  
  
&& apt-file update \  
&& cpanm https://github.com/kak-tus/Essi.git@0.20 \  
  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& curl -L
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
-o /usr/local/bin/gosu \  
&& echo -n "$GOSU_SHA256 /usr/local/bin/gosu" | sha256sum -c \- \  
&& chmod +x /usr/local/bin/gosu \  
  
&& mkdir -p /home/www-data \  
&& chown www-data:www-data /home/www-data \  
&& usermod -d /home/www-data www-data \  
&& gosu www-data bash -c "( echo y ; echo 'manual' ; echo o conf
prerequisites_policy follow ; echo o conf commit ) | cpan" \  
  
&& rm -rf /root/.cpanm \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 9007  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
  
COPY docker.yml /etc/essi.d/docker.yml  
COPY start_essi.sh /usr/local/bin/start_essi.sh  
  
# Fix dh-make-perl cache bug  
# apt-file files have now new format, but latests versions of DhMakePerl from  
# cpan not working on debian 8 (different external utilities issues)  
COPY AptContents.pm /usr/share/perl5/Debian/AptContents.pm  
  
ENV ESSI_DEB_PATH=  
  
CMD ["/usr/local/bin/start_essi.sh"]  

