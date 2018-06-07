# WebApollo  
# VERSION 1.0  
FROM tomcat:7  
MAINTAINER Eric Rasche <esr@tamu.edu>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update --fix-missing && \  
apt-get --no-install-recommends -y install git nodejs-legacy \  
build-essential maven2 openjdk-7-jdk libpq-dev postgresql-common \  
postgresql-client xmlstarlet netcat  
  
RUN curl -L http://cpanmin.us | perl - App::cpanminus && \  
cpanm --force Term::ReadKey && \  
cpanm DateTime Text::Markdown DBI DBD::Pg Crypt::PBKDF2 JSON \  
Digest::Crc32 Hash::Merge PerlIO::gzip Heap::Simple
Bio::GFF3::LowLevel::Parser \  
File::Next && \  
cpanm --force Devel::Size Heap::Simple::XS && \  
rm -rf /root/.cpanm/  
  
RUN mkdir -p /webapollo/ && git clone https://github.com/gmod/Apollo
/webapollo/ && \  
cd /webapollo/ && \  
git checkout 1.0 && \  
cp sample_config.properties config.properties && \  
cp sample_config.xml config.xml && \  
cp sample_hibernate.xml hibernate.xml && \  
cp sample_log4j2.json log4j2.json && \  
cp sample_log4j2-test.json log4j2-test.json && \  
cp default_canned_comments.xml canned_comments.xml && \  
cp default_fasta_config.xml fasta_config.xml && \  
cp default_gff3_config.xml gff3_config.xml && \  
./apollo deploy  
  
# TODO: Chado  
# TODO: GOLR_URL: This is *extremely* fragile, needs to be re-worked, but the  
# deploy step is much too slow for startup.  
ENV APOLLO_ORGANISM="Pythium ultimum" \  
APOLLO_AUTHENTICATION=org.bbop.apollo.web.user.encryptedlocaldb.EncryptedLocalDbUserAuthentication
\  
DB_IS_CHADO=false \  
APOLLO_USERNAME=web_apollo_admin \  
APOLLO_PASSWORD=password \  
APOLLO_TRANSLATION_TABLE=1 \  
GOLR_URL=http://golr.berkeleybop.org/  
  
RUN mkdir -p $CATALINA_HOME/webapps/apollo/ && \  
cp /webapollo/target/apollo-1.0.5-SNAPSHOT.war $CATALINA_HOME/webapps/apollo/
&& \  
cd $CATALINA_HOME/webapps/apollo/ && \  
jar xvf apollo-1.0.5-SNAPSHOT.war  
  
ADD common.sh /bin/  
ADD startup.sh /bin/  
ADD autodetect.sh /bin/  
RUN chmod +x /bin/common.sh /bin/startup.sh /bin/autodetect.sh && mkdir -p
/data  
  
VOLUME "/data"  
CMD ["/bin/startup.sh"]  

