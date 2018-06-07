# This is a Dockerfile to run a guiHive server in a container  
#  
# docker build -t guihive .  
#  
# docker run --name guihive_server -p 8081:8080 -d guihive ## Start the
server. Port mapping = external:internal  
# docker run -p 8082:8080 -it guihive bash ## If you need to do any prior
maintenance/tuning - do it in bash, then manually run the CMD below.  
  
FROM ensemblorg/ensembl-hive  
  
# Install know Perl dependencies with apt (faster than CPAN)  
RUN apt-get update -y \  
&& apt-get install libhtml-parser-perl libhtml-template-perl libjson-perl
libjson-pp-perl liburi-perl -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ARG DEPLOY_LOCATION=/repo/guiHive  
RUN curl -L https://raw.githubusercontent.com/Ensembl/guiHive/server/guihive-
deploy.sh | bash  
  
# Wrap the cpan and compilation phases with apt-get install/purge to keep the
image small  
RUN buildDeps=' \  
golang \  
cpanminus \  
build-essential \  
' \  
&& apt-get update -y \  
&& apt-get install -y $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& cpanm --installdeps --with-recommends /repo/guiHive \  
&& cd /repo/guiHive/server && go build \  
&& apt-get purge -y --auto-remove $buildDeps  
  
EXPOSE 8080  
  
CMD [ "/repo/guiHive/server/server" ]  

