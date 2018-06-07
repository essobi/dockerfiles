FROM alpine  
  
  
#RUN wget http://circos.ca/distribution/lib/libpng-1.6.14.tar.gz  
#9:RUN curl -sSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
RUN apk update && \  
apk add libpng libpng-dev jpeg jpeg-dev freetype freetype-dev gd gd-dev perl
perl-dev make gcc g++ && \  
cpan App::cpanminus  
  
RUN cpanm --no-wget --notest List::MoreUtils Math::Bezier Math::Round
Math::VecStat \  
Params::Validate Readonly Regexp::Common SVG Set::IntSpan Statistics::Basic \  
Text::Format Clone Config::General Font::TTF::Font GD  
  
ENV CIRCOS_VERSION 0.69-2  
RUN mkdir /opt && cd /opt && \  
wget http://circos.ca/distribution/circos-${CIRCOS_VERSION}.tgz && \  
tar xfz circos-${CIRCOS_VERSION}.tgz && \  
rm circos-${CIRCOS_VERSION}.tgz  
  
ENV PATH /opt/circos-${CIRCOS_VERSION}/bin:$PATH  
  
ADD entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

