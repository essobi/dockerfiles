FROM robertprince/ubuntu-base:latest  
  
MAINTAINER Robert Prince "rprince@opuslogica.com"  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
zlibc \  
openjdk-9-jre \  
libboost-dev \  
libncursesw5-dev \  
libncurses5 \  
ncurses-dev \  
libboost-thread-dev \  
python3-pip \  
samtools \  
libopenmpi-dev \  
openmpi-bin \  
ghostscript \  
libgs-dev \  
libgd-dev \  
libexpat1-dev \  
zlib1g-dev \  
libxml2-dev \  
libhtml-template-compiled-perl \  
libxml-opml-simplegen-perl \  
libxml-libxml-debugging-perl  
  
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Log::Log4perl'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install Math::CDF'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install CGI'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::PullParser'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install HTML::Template'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Simple'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Parser::Expat'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::LibXML::Simple'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::SOAP11'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install XML::Compile::WSDL11'  
RUN PERL_MM_USE_DEFAULT=1 perl -MCPAN -e 'install
XML::Compile::Transport::SOAPHTTP'  
  
RUN mkdir /opt/software  
  
ADD http://meme-suite.org/meme-software/4.11.1/meme_4.11.1.tar.gz
/opt/software  
  
WORKDIR /opt/software  
RUN tar zxvf meme_4.11.1.tar.gz  
  
WORKDIR /opt/software/meme_4.11.1  
RUN ./configure --prefix=/opt --enable-build-libxml2 --enable-build-libxslt
--with-url=http://meme-suite.org  
RUN make  
# RUN make test  
RUN make install  
  
ENV PATH /opt/bin:$PATH  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
#ENV CURRENT_USER=memeuser \  
# CURRENT_UID=1555 \  
# CURRENT_GID=1555 \  
# CURRENT_DATA=/Data  
#ADD ./startup.sh /usr/bin/startup  
#RUN chmod +x /usr/bin/startup  
ENV PATH /opt/bin:$PATH  
# ENTRYPOINT ["/usr/bin/startup"]  

