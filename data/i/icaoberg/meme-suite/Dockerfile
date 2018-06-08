FROM ubuntu:artful  
  
RUN apt-get update && apt-get install -y \  
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
RUN mkdir /opt/meme  
ADD http://meme-suite.org/meme-software/4.11.1/meme_4.11.1.tar.gz /opt/meme  
WORKDIR /opt/meme/  
RUN tar zxvf meme_4.11.1.tar.gz && rm -fv meme_4.11.1.tar.gz  
RUN cd /opt/meme/meme_4.11.1 && \  
./configure --prefix=/opt --enable-build-libxml2 --enable-build-libxslt
--with-url=http://meme-suite.org && \  
make && \  
make install  
ENV PATH="/opt/bin:${PATH}"  

