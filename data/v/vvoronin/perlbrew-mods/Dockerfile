FROM vvoronin/perlbrew  
MAINTAINER Viktor Voronin <voronin@x12.su>  
  
  
RUN /tools/apt libevent1-dev libssl-dev libpq-dev libmysqlclient-dev
libreadline-dev  
RUN cpanm -n Catalyst::Devel Module::Install JSON::XS Class::XSAccessor
Class::Accessor::Inherited::XS Cache::Memcached::Fast \  
Catalyst::Plugin::Authorization::Roles \  
Event::Lib Exception::Class Net::Patricia
Catalyst::Plugin::ConfigLoader::MultiState
Catalyst::Authentication::Credential::HTTP \  
Catalyst::Authentication::Store::DBIx::Class DBIx::RetryOverDisconnects
URI::Escape::XS NetAddr::IP::Lite Sys::HostAddr \  
Term::Size Term::ANSIScreen IO::Socket::SSL MIME::Entity Digest::SHA1
Crypt::OpenSSL::X509 Crypt::OpenSSL::RSA XML::Fast \  
lib::abs Data::Alias Set::IntSpan::Fast Statistics::LineFit
SQL::Abstract::Complete \  
Spreadsheet::DataToExcel Spreadsheet::ParseExcel DBD::Pg DBD::mysql
Term::ReadLine::Gnu \  
Catalyst::View::TT Template::Provider::Encoding DBIx::Class::FrozenColumns
DBIx::Class::DynamicSubclass Class::Date \  
Text::CSV_XS JSON::WebToken

