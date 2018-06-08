FROM rapi/rapidapp-base:1.3100  
MAINTAINER Henry Van Styn <vanstyn@cpan.org>  
  
# Install drivers and packages needed to access the 3 main  
# RDBMS backends (besides SQLite which is already baked in):  
#  
# * MySQL  
# * PostgreSQL  
# * Microsoft SQL Server  
#  
# system packages : unixodbc-dev tdsodbc (for MSSQL)  
# CPAN modules : DBD::mysql DBD::Pg DBD::ODBC  
  
  
# Install misc system packages needed to support common modules  
RUN apt-get update && apt-get install -y \  
unixodbc-dev tdsodbc \  
libgd-dev \  
sqlite \  
&& rm -fr /var/lib/apt/lists/*  
  
COPY etc/odbcinst.ini /etc/  
  
# This is a dep module of the following which randomly fails due  
# to issues with lack of interactive terminal, install it with  
# no tests:  
RUN cpanm -n Parallel::Prefork && rm -rf .cpanm/  
  
# Install common/useful CPAN modules:  
RUN cpanm \  
Gazelle \  
DBD::mysql DBD::Pg DBD::ODBC \  
Image::Resize \  
Devel::Confess \  
YAML::XS \  
DBIx::Class::Helpers \  
&& rm -rf .cpanm/  

