FROM debian:stretch  
MAINTAINER Freelock john@freelock.com  
  
  
# Install Perl, Tex, Starman, psql client, and all dependencies  
# Without libclass-c3-xs-perl, everything grinds to a halt;  
# add it, because it's a 'recommends' it the dep tree, which  
# we're skipping, normally  
# 'master' and common dependency install:  
RUN echo -n "APT::Install-Recommends \"0\";\nAPT::Install-Suggests \"0\";\n" \  
>> /etc/apt/apt.conf && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install curl ca-certificates \  
wget gnupg2 && \  
curl -L https://deb.nodesource.com/setup_6.x -o ./setup && \  
bash ./setup && rm ./setup && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
libcgi-emulate-psgi-perl libconfig-inifiles-perl \  
libdbd-pg-perl libdbi-perl libdatetime-perl \  
libspreadsheet-writeexcel-perl \  
libdatetime-format-strptime-perl libfile-mimeinfo-perl \  
libhtml-parser-perl libio-stringy-perl libjson-maybexs-perl \  
libcpanel-json-xs-perl liblist-moreutils-perl \  
liblocale-maketext-perl liblocale-maketext-lexicon-perl \  
liblog-log4perl-perl libwww-perl libmime-lite-perl \  
libmodule-runtime-perl libmath-bigint-gmp-perl libmoose-perl \  
libmoosex-nonmoose-perl libnumber-format-perl \  
libole-storage-lite-perl libparse-recdescent-perl \  
libpgobject-perl libpgobject-simple-perl libpgobject-simple-role-perl \  
libpgobject-type-bigfloat-perl libpgobject-type-bytestring-perl \  
libpgobject-type-datetime-perl libpgobject-util-dbmethod-perl \  
libplack-perl libplack-middleware-reverseproxy-perl \  
libspreadsheet-writeexcel-perl libtemplate-perl \  
libtry-tiny-perl libtext-csv-perl libtext-csv-xs-perl libxml-simple-perl \  
libnamespace-autoclean-perl libdata-uuid-perl \  
libtemplate-plugin-latex-perl libtex-encode-perl \  
libmoosex-nonmoose-perl libclass-c3-xs-perl \  
texlive-latex-recommended fonts-liberation2 \  
libx12-parser-perl \  
texlive-xetex \  
starman \  
libxml-twig-perl libopenoffice-oodoc-perl \  
postgresql-client \  
ssmtp \  
git cpanminus make gcc nodejs libperl-dev lsb-release libcarp-always-perl \  
gettext procps libtap-parser-sourcehandler-pgtap-perl \  
libtest-dependencies-perl libtest-exception-perl libtest-trap-perl \  
libperl-critic-perl libmodule-cpanfile-perl libfile-util-perl \  
libclass-trigger-perl libclass-accessor-lite-perl libtest-requires-perl \  
libmodule-install-perl python-setuptools \  
python-pip python-urllib3 python-six && \  
pip install transifex-client && \  
pip install --upgrade urllib3 && \  
npm install -g uglify-js@">=2.0 <3.0" && \  
echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg
main" > /etc/apt/sources.list.d/pgdg.list && \  
(wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add -) && \  
DEBIAN_FRONTEND="noninteractive" apt-get -y update && \  
DEBIAN_FRONTEND="noninteractive" apt-get -y install postgresql-client  
  
# 1.5 additional dependency install:  
# JRE is for running the dojo build process using ClosureCompiler  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \  
libcgi-simple-perl libhttp-exception-perl default-jre-headless  
  
# Build time variables  
ENV NODE_PATH /usr/lib/node_modules  
ARG CACHEBUST  
  
# Install LedgerSMB  
RUN cd /srv && \  
git clone -b master https://github.com/ledgersmb/LedgerSMB.git ledgersmb && \  
cd ledgersmb && \  
cpanm --quiet --notest \  
\--with-develop \  
\--with-feature=starman \  
\--with-feature=latex-pdf-images \  
\--with-feature=latex-pdf-ps \  
\--with-feature=openoffice \  
\--with-feature=xls \  
\--with-feature=edi \  
\--installdeps . && \  
git checkout -b 1.5 origin/1.5 && \  
cpanm --quiet --notest \  
\--with-develop \  
\--with-feature=starman \  
\--with-feature=latex-pdf-ps \  
\--with-feature=openoffice \  
\--with-feature=edi \  
\--installdeps . && \  
cpanm --quiet --notest Pod::ProjectDocs && \  
cpanm --quiet --notest DBD::Mock && \  
rm -rf ~/.cpanm && \  
cd .. && rm -rf ledgersmb && mkdir ledgersmb  
  
# Configure outgoing mail to use host, other run time variable defaults  
## sSMTP  
ENV SSMTP_ROOT ar@example.com  
ENV SSMTP_MAILHUB 172.17.0.1  
ENV SSMTP_HOSTNAME 172.17.0.1  
#ENV SSMTP_USE_STARTTLS  
#ENV SSMTP_AUTH_USER  
#ENV SSMTP_AUTH_PASS  
ENV SSMTP_FROMLINE_OVERRIDE YES  
#ENV SSMTP_AUTH_METHOD  
ENV POSTGRES_HOST postgres  
ENV POSTGRES_PORT 5432  
ENV DEFAULT_DB lsmb  
  
COPY start.sh /usr/local/bin/start.sh  
COPY update_ssmtp.sh /usr/local/bin/update_ssmtp.sh  
  
RUN chown www-data /etc/ssmtp /etc/ssmtp/ssmtp.conf && \  
chmod +x /usr/local/bin/update_ssmtp.sh /usr/local/bin/start.sh && \  
mkdir -p /var/www  
  
# Work around an aufs bug related to directory permissions:  
RUN mkdir -p /tmp && \  
chmod 1777 /tmp  
  
# Internal Port Expose  
EXPOSE 5762  
# If ledgersmb.conf does not exist, www-data user needs to be able to create
it.  
RUN chown www-data /srv/ledgersmb  
USER www-data  
  
WORKDIR /srv/ledgersmb  
  
CMD ["start.sh"]  

