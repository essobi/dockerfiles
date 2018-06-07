### docker container for ensembl webcode  
FROM ubuntu:xenial  
  
ADD localfonts.conf /etc/fonts/local.conf  
  
ARG ENSEMBL_SERVERNAME=89.45.233.99  
ENV ENSEMBL_SERVERNAME=$ENSEMBL_SERVERNAME  
  
# session db args  
ARG SESSION_HOST=192.168.1.8  
ARG SESSION_PORT=3306  
ARG SESSION_USER=ensrw  
ARG SESSION_PASS=ensrw  
  
ENV SESSION_HOST=$SESSION_HOST  
ENV SESSION_PORT=$SESSION_PORT  
ENV SESSION_USER=$SESSION_USER  
ENV SESSION_PASS=$SESSION_PASS  
  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
file \  
g++ \  
git \  
locales \  
make \  
sudo \  
nano \  
python \  
uuid-runtime \  
apt-transport-https && \  
echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true" | debconf-set-selections && \  
apt-get install -y --no-install-recommends fontconfig ttf-mscorefonts-
installer && \  
chown -R _apt:root /var/lib/update-notifier/package-data-downloads/partial &&
\  
rm -rf /var/lib/update-notifier/package-data-downloads/partial/*.FAILED && \  
apt install --reinstall update-notifier-common ttf-mscorefonts-installer && \  
apt-get clean && \  
localedef -i en_US -f UTF-8 en_US.UTF-8 && \  
useradd -m -s /bin/bash linuxbrew && \  
echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers && \  
mkdir -p /home/linuxbrew//utils && \  
curl -s http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/hubCheck >
/home/linuxbrew/utils/hubCheck && \  
chmod ugo+x /home/linuxbrew/utils/hubCheck && \  
fc-cache -f -v  
  
USER linuxbrew  
WORKDIR /home/linuxbrew  
  
ENV PATH=/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin:$PATH
\  
SHELL=/bin/bash  
  
ENV ENSEMBL_MOONSHINE_ARCHIVE $HOME/ENSEMBL_MOONSHINE_ARCHIVE  
ENV PERL5LIB /home/linuxbrew/.linuxbrew/opt/bioperl-169/libexec  
ENV HTSLIB_DIR=/home/linuxbrew/.linuxbrew/opt/htslib
KENT_SRC=/home/linuxbrew/.linuxbrew/opt/kent MACHTYPE=x86_64
SHARE_PATH=/home/linuxbrew/paths  
  
RUN git clone https://github.com/Linuxbrew/brew.git .linuxbrew && \  
brew doctor && \  
brew analytics off && \  
mkdir -p $HOME/ENSEMBL_MOONSHINE_ARCHIVE && \  
brew tap homebrew/science && \  
brew tap ensembl/ensembl && \  
brew tap ensembl/web && \  
brew tap ensembl/moonshine && \  
brew tap ensembl/cask && \  
brew update && \  
sed -i s/'"-i"'/'"-M" , "http:\/\/ftp.acc.umu.se\/mirror\/CPAN\/", "-i"'/
/home/linuxbrew/.linuxbrew/Library/Taps/homebrew/homebrew-core/Formula/perl.rb
&& \  
brew install perl && \  
sed -i s/'http:\/\/www.cpan.org\/'/'http:\/\/ftp.acc.umu.se\/mirror\/CPAN\/'/
.cpan/CPAN/MyConfig.pm && \  
brew install python && \  
brew install ensembl/ensembl/ensembl-git-tools && \  
brew install ensembl/cask/web-base && \  
brew install ensembl/cask/web-perllibs && \  
brew install ensembl/cask/web-gui && \  
brew install ensembl/ensembl/blast --with-static && \  
brew install homebrew/science/emboss --without-x11 && \  
brew install ensembl/cask/web-bifo && \  
brew install homebrew/homebrew-science/vcftools && \  
brew install jdk && \  
mkdir -p $HOME/fonts && \  
ln -s $HOME/fonts $HOME/.fonts && \  
cpanm --mirror http://ftp.acc.umu.se/mirror/CPAN/ --mirror
https://cpan.metacpan.org --installdeps --with-recommends --notest --cpanfile
ensembl/cpanfile . && \  
curl -s
https://raw.githubusercontent.com/Ensembl/cpanfiles/master/web/cpanfile >
cpanfile && \  
cpanm --mirror http://ftp.acc.umu.se/mirror/CPAN --mirror
https://cpan.metacpan.org --notest HTML::Formatter && \  
cpanm --mirror http://ftp.acc.umu.se/mirror/CPAN --mirror
https://cpan.metacpan.org --installdeps --with-recommends --notest --cpanfile
cpanfile . && \  
echo >> $HOME/.profile && \  
echo PATH=$HOME/paths:$HOME/.linuxbrew/bin:\$PATH >> $HOME/.profile && \  
echo MANPATH=$HOME/.linuxbrew/share/man:\$MANPATH >> $HOME/.profile && \  
echo INFOPATH=$HOME/.linuxbrew/share/info:\$INFOPATH >> $HOME/.profile && \  
echo export PATH >> $HOME/.profile && \  
echo export MANPATH >> $HOME/.profile && \  
echo export INFOPATH >> $HOME/.profile && \  
echo export PERL5LIB=${PERL5LIB} >> $HOME/.profile && \  
echo export SHARE_PATH=$HOME/paths >> $HOME/.profile && \  
echo export ENSEMBL_MOONSHINE_ARCHIVE=${ENSEMBL_MOONSHINE_ARCHIVE}} >>
$HOME/.profile && \  
mkdir -p paths/apache && \  
ln -s $HOME/.linuxbrew/opt/emboss $SHARE_PATH/emboss && \  
ln -s $HOME/.linuxbrew/opt/genewise $SHARE_PATH/genewise && \  
ln -s $HOME/.linuxbrew/opt/jdk/bin/java $SHARE_PATH/java && \  
ln -s $HOME/.linuxbrew/opt/r2r/bin/r2r $SHARE_PATH/r2r && \  
ln -s $HOME/.linuxbrew/opt/htslib/include $SHARE_PATH/htslib && \  
ln -s $HOME/.linuxbrew/opt/kent/bin/gfClient $SHARE_PATH/gfClient && \  
ln -s $HOME/.linuxbrew/opt/blast/bin $SHARE_PATH/ncbi-blast && \  
ln -s $HOME/.linuxbrew/opt/repeatmasker/bin/RepeatMasker
$SHARE_PATH/RepeatMasker && \  
ln -s $HOME/.linuxbrew/opt/htslib/bin/bgzip $SHARE_PATH/bgzip && \  
ln -s $HOME/.linuxbrew/opt/samtools/bin/samtools $SHARE_PATH/samtoools && \  
ln -s $HOME/.linuxbrew/opt/htslib/bin/tabix $SHARE_PATH/tabix && \  
ln -s /home/linuxbrew/.linuxbrew/opt/httpd22/bin/httpd paths/apache/httpd && \  
ln -s /home/linuxbrew/.linuxbrew/opt/httpd22/libexec paths/apache/modules && \  
ln -s /home/linuxbrew/.linuxbrew/opt/bioperl-169/libexec paths/bioperl && \  
ln -s /home/linuxbrew/.linuxbrew/opt/vcftools/lib/perl5/site_perl
paths/vcftools_perl_lib && \  
rm -rf $(brew --cache) && \  
rm -rf .cpanm/work && \  
rm -rf .cpan/build && \  
mkdir -p website/tmp && \  
git-ensembl \--dir website --clone ensembl ensembl-compara ensembl-funcgen
ensembl-io ensembl-orm ensembl-tools ensembl-variation ensembl-webcode && \  
git clone --single-branch -b experimental/docker
https://github.com/NBISweden/Ensembl-public-plugins.git website/public-plugins
&& \  
cp website/public-plugins/docker-demo/conf/Plugins.pm-dist website/ensembl-
webcode/conf/Plugins.pm && \  
cp website/public-plugins/docker-demo/conf/httpd.conf website/ensembl-
webcode/conf/  
  
  
RUN $HOME/website/ensembl-webcode/ctrl_scripts/build_inline_c && \  
$HOME/website/ensembl-webcode/ctrl_scripts/init  
CMD $HOME/website/ensembl-webcode/ctrl_scripts/start_server -D FOREGROUND  
  
EXPOSE 8080  

