FROM inorton/debian-squeeze-i386  
  
RUN apt-get update -qq && apt-get install -yqq --force-yes apt-utils \  
git-core \  
apache2 \  
apache2-mpm-prefork \  
libapache2-mod-perl2 \  
libgd2-xpm \  
libxpm4 \  
htmldoc \  
libaspell15 \  
ntpdate \  
libhttp-oai-perl \  
libxml-sax-writer-perl \  
libxml-libxslt-perl \  
libspreadsheet-xlsx-perl \  
libspreadsheet-writeexcel-perl \  
libspreadsheet-read-perl \  
libspreadsheet-parseexcel-perl \  
libyaml-perl \  
mysql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Modulo que no existe en el repo de debian squeeze  
RUN perl -MCPAN -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1,
autoconfig => 1); $c->edit(prerequisites_policy => "follow");
$c->edit(build_requires_install_policy => "yes"); $c->commit'  
RUN cpan -i HTML::StripTags  
  
RUN git clone -b 0.10.7 https://github.com/Desarrollo-CeSPI/meran.git
/usr/local/share/meran/main  
  
# Configuracion del volumen  
ENV ID main  
  
ENV DB_NAME ${DB_NAME:-meran}  
ENV DB_HOST ${DB_HOST:-mysql}  
ENV DB_USER ${DB_USER:-meran}  
ENV DB_PASS ${DB_PASS:-meranpass}  
  
ENV MERAN_PATH /usr/local/share/meran  
ENV MERAN_CONFIG /etc/meran/meranmain.conf  
ENV MERAN_CONF /etc/meran/meranmain.conf  
ENV SPHINX_CONFIG /etc/meran/sphinx.conf  
ENV TPL_MAIN_CONFIG /tmp/meran.conf  
  
ENV PERL5LIB
/opt/modules/Share/share/perl/5.10.1/:/opt/modules/Share/lib/perl/5.10.1/:/opt/modules/Share/share/perl/5.10/:/opt/modules/C4/Share/share/perl/5.10.1/:/opt/modules/Share/lib/perl/5.10/:/opt/modules/Share/lib/perl5/  
  
ADD files/meran.conf /tmp/  
ADD files/sphinx32.tar.gz /opt/  
ADD files/jaula32.tar.gz /opt/modules  
ADD files/apache-opac /opt/  
ADD files/apache-ssl /opt/  
ADD files/iniciandomain.pl /etc/meran/  
ADD files/sphinx.conf /etc/meran/  
  
VOLUME [ "/meran/config", "/meran/logs", "/meran/files", "/meran/apache",
"/meran/ssl", "/usr/local/share/meran/" ]  
  
EXPOSE 80  
EXPOSE 443  
COPY entrypoint /entrypoint  
ENTRYPOINT ["/entrypoint"]  

