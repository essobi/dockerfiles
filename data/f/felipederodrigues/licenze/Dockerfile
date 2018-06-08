FROM ubuntu:14.04  
MAINTAINER felipederodrigues  
  
#------------------------------------------  
# Instalação do ImageMagick  
#------------------------------------------  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN echo "LANG=\"en_GB.UTF-8\"" > /etc/default/locale  
RUN locale-gen en_GB.UTF-8  
RUN dpkg-reconfigure locales  
  
RUN apt-get -qq update  
RUN apt-get install -y \  
wget \  
imagemagick  
  
#------------------------------------------  
# Instalação do ruby 1.8.7  
#------------------------------------------  
RUN apt-get -qq update  
RUN apt-get -qq install -y dirmngr patch make  
RUN apt-get -qq install -y libsqlite3-dev libmysqlclient-dev libxslt-dev  
RUN apt-get -qq install -y gcc curl wget libxml2-dev  
RUN apt-get -qq install -y sudo ca-certificates  
RUN apt-get -qq install -y graphicsmagick-libmagick-dev-compat libpq5  
RUN apt-get -qq install -y libsqlite3-0 bzr git mercurial openssh-client bzip2
gawk g++  
RUN apt-get -qq install -y libssl-dev libc6-dev zlib1g-dev libyaml-dev sqlite3  
RUN apt-get -qq install -y autoconf libgmp-dev libgdbm-dev libncurses5-dev
automake  
RUN apt-get -qq install -y libtool bison pkg-config libffi-dev
libreadline6-dev  
RUN apt-get -qq install -y imagemagick libmagickcore-dev libmagickwand-dev
libmagick++-dev  
RUN apt-get -y -qq install libcurl3 libxml2 libxslt1-dev libcurl4-gnutls-dev
git-core mysql-client memcached  
#------------------------------------------  
# Dependências da gem ruby-oci8 -v 1.0.2  
RUN apt-get -y -qq install build-essential libpq-dev libaio1 unzip  
#------------------------------------------  
# Build Ruby  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q install zlib1g zlib1g-dev
wget libyaml-dev bison libssl-dev libreadline6-dev autoconf subversion curl  
RUN wget -q -O ruby-1.8.7-p370.tar.gz http://cache.ruby-
lang.org/pub/ruby/1.8/ruby-1.8.7-p370.tar.gz  
RUN tar xvf ruby-1.8.7-p370.tar.gz  
RUN rm ruby-1.8.7-p370.tar.gz  
WORKDIR ruby-1.8.7-p370  
RUN ./configure  
RUN make  
RUN make install  
  
# Install RubyGems  
WORKDIR /  
RUN wget http://production.cf.rubygems.org/rubygems/rubygems-1.8.22.tgz  
RUN tar -xvzf rubygems-1.8.22.tgz  
WORKDIR /rubygems-1.8.22  
RUN sudo ruby setup.rb  
RUN gem update --system 1.7.2  
RUN ruby -v  
RUN gem list  
  
#------------------------------------------  
# Instalação de gems  
#------------------------------------------  
RUN gem install --no-rdoc --no-ri actionmailer -v 2.3.11  
RUN gem install --no-rdoc --no-ri actionmailer -v 2.3.5  
RUN gem install --no-rdoc --no-ri actionmailer -v 1.3.6  
RUN gem install --no-rdoc --no-ri actionpack -v 2.3.11  
RUN gem install --no-rdoc --no-ri actionpack -v 2.3.5  
RUN gem install --no-rdoc --no-ri actionpack -v 1.13.6  
RUN gem install --no-rdoc --no-ri actionwebservice -v 1.2.6  
RUN gem install --no-rdoc --no-ri activerecord -v 2.3.5  
RUN gem install --no-rdoc --no-ri activerecord -v 1.15.6  
RUN gem install --no-rdoc --no-ri activerecord-oracle_enhanced-adapter -v
1.3.0  
RUN gem install --no-rdoc --no-ri activeresource -v 2.3.5  
RUN gem install --no-rdoc --no-ri activesupport -v 2.3.11  
RUN gem install --no-rdoc --no-ri activesupport -v 2.3.5  
RUN gem install --no-rdoc --no-ri activesupport -v 1.4.4  
RUN gem install --no-rdoc --no-ri afm -v 0.2.0  
RUN gem install --no-rdoc --no-ri ansel_iconv -v 1.1.6  
RUN gem install --no-rdoc --no-ri Ascii85 -v 1.0.1  
RUN gem install --no-rdoc --no-ri cgi_multipart_eof_fix -v 2.5.0  
RUN gem install --no-rdoc --no-ri choice -v 0.1.4  
RUN gem install --no-rdoc --no-ri fastercsv -v 1.5.4  
RUN gem install --no-rdoc --no-ri gem_plugin -v 0.2.3  
RUN gem install --no-rdoc --no-ri gruff -v 0.3.7  
RUN gem install --no-rdoc --no-ri hashery -v 2.1.0  
RUN gem install --no-rdoc --no-ri htmldoc -v 0.2.3  
RUN gem install --no-rdoc --no-ri log4r -v 1.1.9  
RUN gem install --no-rdoc --no-ri mail -v 2.5.4  
RUN gem install --no-rdoc --no-ri mime-types -v 1.25  
RUN gem install --no-rdoc --no-ri mysql -v 2.8.1  
  
#------------------------------------------  
# Instalação de gem nokogiri -v 1.5.0  
#------------------------------------------  
# http://stackoverflow.com/questions/23510933/nokogiri-installation-error-for-
ruby-1-8-7-for-linux-os  
# apt-get install libxslt-dev libxml2-dev -y  
RUN gem install --no-rdoc --no-ri nokogiri -v 1.5.0  
  
RUN gem install --no-rdoc --no-ri oauth -v 0.4.5  
RUN gem install --no-rdoc --no-ri pdf-reader -v 1.1.1  
RUN gem install --no-rdoc --no-ri polyglot -v 0.3.3  
# http://stackoverflow.com/questions/20626408/prawn-requires-ruby-
version-1-9-3  
RUN gem install --no-rdoc --no-ri prawn -v 1.0.0.rc2  
RUN gem install --no-rdoc --no-ri rack -v 1.1.0  
RUN gem install --no-rdoc --no-ri rack -v 1.0.1  
RUN gem install --no-rdoc --no-ri rake -v 0.8.7  
RUN gem install --no-rdoc --no-ri rgl -v 0.4.0  
RUN gem install --no-rdoc --no-ri ruby-ole -v 1.2.11.2  
RUN gem install --no-rdoc --no-ri ruby-rc4 -v 0.1.5  
RUN gem install --no-rdoc --no-ri rubyzip -v 0.9.4  
RUN gem install --no-rdoc --no-ri spreadsheet -v 0.6.5.9  
RUN gem install --no-rdoc --no-ri sqlite3-ruby -v 1.3.1  
RUN gem install --no-rdoc --no-ri stream -v 0.5  
RUN gem install --no-rdoc --no-ri todonotes -v 0.1.0  
RUN gem install --no-rdoc --no-ri treetop -v 1.4.15  
RUN gem install --no-rdoc --no-ri ttfunk -v 1.0.3  
RUN gem install --no-rdoc --no-ri tzinfo -v 0.3.29  
RUN gem install --no-rdoc --no-ri mongrel_service -v 0.4.0  
RUN gem install --no-rdoc --no-ri mongrel -v 1.1.5  
RUN gem install --no-rdoc --no-ri ffi -v 0.6.3  
  
RUN gem install --no-rdoc --no-ri rmagick -v 2.12.0  
  
#--------------------  
# http://stackoverflow.com/questions/5795309/gem-install-mysql-fail  
# apt-get install libmysqlclient-dev -y  
RUN gem install --no-rdoc --no-ri mysql -v 2.8.1  
  
#------------------------------------------  
# Instalação de gem roo -v 1.10.3  
#------------------------------------------  
#RUN gem install --no-rdoc --no-ri roo -v 1.10.3  
RUN git clone https://github.com/roo-rb/roo.git
/usr/local/lib/ruby/gems/1.8/gems/roo-1.10.3  
WORKDIR /usr/local/lib/ruby/gems/1.8/gems/roo-1.10.3  
RUN git checkout v1.10.3  
RUN cp /usr/local/lib/ruby/gems/1.8/gems/roo-1.10.3/roo.gemspec
/usr/local/lib/ruby/gems/1.8/specifications/roo.gemspec  
  
#------------------------------------------  
# Instalação de gem gruff -v 1.10.3 * MODIFIED: CUSTOMIZED FOR SPECIFIC APP  
# For more info check: https://github.com/betonix/gruff  
#------------------------------------------  
#RUN rm -rf /usr/local/lib/ruby/gems/1.8/gems/gruff-0.3.7/*  
#RUN git clone https://github.com/betonix/gruff.git
/usr/local/lib/ruby/gems/1.8/gems/gruff-0.3.7  
#RUN ls -l /usr/local/lib/ruby/gems/1.8/gems/gruff-0.3.7  
#RUN cp /usr/local/lib/ruby/gems/1.8/gems/gruff-0.3.7/gruff.gemspec
/usr/local/lib/ruby/gems/1.8/specifications/gruff.gemspec  
#------------------------------------------  
# Instalação de gem ruby-oci8 -v 1.0.2  
#------------------------------------------  
RUN export HOME="/home/root"  
RUN mkdir -p /opt/oracle  
WORKDIR /opt/oracle  
COPY ./*.zip ./  
COPY ./extract.sh ./  
RUN chmod +x ./extract.sh  
RUN ./extract.sh  
RUN ls  
WORKDIR /opt/oracle/instantclient_12_2/  
RUN ln -s libclntsh.so.12.1 libclntsh.so  
ENV LD_LIBRARY_PATH /opt/oracle/instantclient_12_2  
RUN LD_LIBRARY_PATH=/opt/oracle/instantclient_12_2  
RUN export LD_LIBRARY_PATH  
RUN mkdir -p /usr/include/sys && ln -s /usr/include/linux/types.h
/usr/include/sys/types.h  
RUN gem install --no-rdoc --no-ri ruby-oci8 -v 1.0.2  
  
RUN gem uninstall afm -v 0.2.2  
RUN gem uninstall daemons -v 1.2.4  
RUN gem uninstall fastthread -v 1.0.7  
RUN gem uninstall mime-types -v 1.25.1  
RUN gem uninstall polyglot -v 0.3.5  
RUN gem uninstall rubygems-update -v 1.7.2  
RUN gem uninstall rack -v 1.1.6  
RUN gem list  
  
#------------------------------------------  
# Instalação do java  
#------------------------------------------  
# to make apt-add-repository command enabled:  
RUN apt-get install software-properties-common -y  
RUN apt-add-repository ppa:webupd8team/java  
RUN apt-get update  
# to automate installation of java8 and remove user interaction during
install:  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install oracle-java8-installer -y  
RUN java -version  
  
WORKDIR /  
ADD run.sh ./  
RUN chmod +x ./run.sh  
  
RUN gem install --no-rdoc --no-ri rails -v 2.3.5  
RUN gem install --no-rdoc --no-ri rails -v 1.2.6  
#RUN gem install --no-rdoc --no-ri google-spreadsheet-ruby -v 0.1.5  
#RUN gem install --no-rdoc --no-ri roo -v 1.10.0  
RUN gem list  
  
CMD ["sh", "-c", "./run.sh ; /bin/bash"]  

