############################################  
# Docker build file providing an Image  
# exposing differents web app scan  
# in order to use the image as command line tools  
############################################  
# Script use following best practices  
# https://docs.docker.com/articles/dockerfile_best-practices  
############################################  
FROM debian:buster  
MAINTAINER Dominique Righetto <dominique.righetto@gmail.com>  
LABEL org.label-schema.schema-version="1.0" org.label-
schema.url="https://www.righettod.eu" org.label-schema.name="webappsecscanbox"
org.label-schema.description="Docker build file providing an Image exposing
some web app scan in order to use the image as command line tools" org.label-
schema.vcs-url="https://github.com/righettod/docker-webappsecscanbox"
org.label-schema.vcs-type="Git" org.label-schema.license="GPL v3" org.label-
schema.docker.dockerfile="/Dockerfile"  
# Install dependencies  
# perl openssl libnet-ssleay-perl: Dependencies for Nikto  
# tofrodos: To fix issue when import file from Windows  
# wget: To download tools  
# testssl: aha for HTML report rendering, git for repo cloning, dnsutils for
DNS operations, bsdmainutils for hexdump utility  
RUN apt-get update && apt-get install -y aha dnsutils git bsdmainutils libnet-
ssleay-perl openssl perl procps tofrodos wget  
RUN ln -s /usr/bin/fromdos /usr/bin/dos2unix  
# Create the system non-root user that will own and run all the tools
installed  
ENV TOOLS_OWNER auditor  
ENV TOOLS_OWNER_HOME /home/$TOOLS_OWNER  
RUN echo "TOOLS_OWNER_HOME=$TOOLS_OWNER_HOME" >> /etc/environment  
RUN useradd -ms /bin/bash $TOOLS_OWNER  
# Install NIKTO from release  
ENV NIKTO_HOME /opt/nikto  
RUN echo "NIKTO_HOME=$NIKTO_HOME" >> /etc/environment  
RUN mkdir $NIKTO_HOME  
RUN wget -q -O /tmp/nikto.tgz http://www.cirt.net/nikto/nikto-2.1.5.tar.gz  
RUN tar --strip-components=1 -xzf /tmp/nikto.tgz -C $NIKTO_HOME  
RUN chown -R $TOOLS_OWNER:$TOOLS_OWNER $NIKTO_HOME  
RUN chmod -R +x $NIKTO_HOME  
# Install ARACHNI from release  
ENV ARACHNI_HOME /opt/arachni  
RUN echo "ARACHNI_HOME=$ARACHNI_HOME" >> /etc/environment  
RUN mkdir $ARACHNI_HOME  
RUN wget -q -O /tmp/arachni.tgz
https://github.com/Arachni/arachni/releases/download/v1.5.1/arachni-1.5.1-0.5.12-linux-x86_64.tar.gz  
RUN tar --strip-components=1 -xzf /tmp/arachni.tgz -C $ARACHNI_HOME  
RUN chown -R $TOOLS_OWNER:$TOOLS_OWNER $ARACHNI_HOME  
RUN chmod -R +x $ARACHNI_HOME  
# Install TestSSL from Github repository because it's always generally stable  
ENV TESTSSL_HOME /opt/testssl  
RUN echo "TESTSSL_HOME=$TESTSSL_HOME" >> /etc/environment  
RUN git clone https://github.com/drwetter/testssl.sh.git $TESTSSL_HOME  
RUN chown -R $TOOLS_OWNER:$TOOLS_OWNER $TESTSSL_HOME  
RUN chmod +x $TESTSSL_HOME/testssl.sh  
# Setup image entry point  
RUN rm -f /tmp/*.tgz  
COPY scan.sh /opt/scan.sh  
RUN dos2unix /opt/scan.sh  
RUN chmod +x /opt/scan.sh  
# Validate the whole installation  
RUN perl $NIKTO_HOME/nikto.pl -update  
RUN perl $NIKTO_HOME/nikto.pl -Version  
RUN $ARACHNI_HOME/bin/arachni --version  
RUN bash $TESTSSL_HOME/testssl.sh --version  
# Set the execution user to the dedicated one  
USER $TOOLS_OWNER  
WORKDIR $TOOLS_OWNER_HOME  
# Set the default entry point of the image  
ENTRYPOINT ["/bin/bash","/opt/scan.sh"]  

