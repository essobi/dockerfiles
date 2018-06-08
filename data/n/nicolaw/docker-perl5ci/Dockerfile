FROM perl:latest  
ENV DEBIAN_FRONTEND noninteractive  
LABEL author="Nicola Worthington <nicolaw@tfb.net>"  
RUN apt-get -qq -o Dpkg::Use-Pty=0 update \  
&& apt-get -qq -o Dpkg::Use-Pty=0 install -y rpm \  
&& rm -rf /var/lib/apt/lists/*  
RUN curl -sSL http://cpanmin.us | /usr/bin/perl - App::cpanminus  
RUN cpanm Module::Build LWP && rm -rf ~/.cpanm  
RUN curl -sSL
http://search.cpan.org/CPAN/authors/id/B/BB/BBB/cpan2rpm-2.028_02.tar.gz \  
| tar -C /usr/bin --strip=1 -zvx cpan2rpm-2.028_02/cpan2rpm  

