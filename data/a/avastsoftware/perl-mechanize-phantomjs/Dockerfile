FROM ubuntu:14.04  
  
RUN apt-get update \  
&& apt-get install -y libfreetype6 libfontconfig bzip2 perl curl libxml2-dev
build-essential make libssl-dev libexpat1-dev \  
&& apt-get clean  
  
RUN \curl -L http://install.perlbrew.pl | bash  
RUN ~/perl5/perlbrew/bin/perlbrew install --notest --noman -j 2 \--switch
perl-5.20.3 || tail -n 50 /root/perl5/perlbrew/build.perl-5.20.3.log \  
&& ~/perl5/perlbrew/bin/perlbrew install-cpanm  
ENV PATH /root/perl5/perlbrew/perls/perl-5.20.3/bin/:$PATH  
  
COPY phantomjs-1.9.8 /usr/bin/phantomjs  
  
RUN ~/perl5/perlbrew/bin/cpanm -v --notest WWW::Mechanize::PhantomJS  

