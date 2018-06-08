FROM scaldwell/ubuntu  
  
RUN mkdir /var/local/src && \  
wget http://www.cpan.org/src/5.0/perl-5.16.3.tar.gz -O
/var/local/src/perl-5.16.3.tar.gz && \  
tar -C /var/local/src -xzf /var/local/src/perl-5.16.3.tar.gz && \  
cd /var/local/src/perl-5.16.3 && \  
./Configure -des -Dprefix=/usr/local && \  
make && \  
make install && \  
(curl -L http://cpanmin.us | perl - App::cpanminus) && \  
cpanm Module::CPANfile  

