# Dockerfile that builds a minimal container for IPython + narrative  
#  
# Copyright 2013 The Regents of the University of California,  
# Lawrence Berkeley National Laboratory  
# United States Department of Energy  
# The DOE Systems Biology Knowledgebase (KBase)  
# Made available under the KBase Open Source License  
#  
FROM kbase/runtime:latest  
MAINTAINER Shane Canon scanon@lbl.gov  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get update;apt-get -y upgrade;apt-get
install -y \  
# mercurial bzr gfortran subversion tcsh cvs mysql-client libgd2-dev tcl-dev
tk-dev \  
# libtiff-dev libpng12-dev libpng-dev libjpeg-dev libgd2-xpm-dev libxml2-dev \  
# libwxgtk2.8-dev libdb5.1-dev libgsl0-dev libxslt1-dev libfreetype6-dev
libreadline-dev \  
# libpango1.0-dev libx11-dev libxt-dev libcairo2-dev zlib1g-dev libgtk2.0-dev
python-dev \  
# libmysqlclient-dev libmysqld-dev libssl-dev libpq-dev libexpat1-dev libzmq-
dev libbz2-dev \  
# libncurses5-dev libcurl4-gnutls-dev uuid-dev git wget uuid-dev build-
essential curl \  
# libsqlite3-dev libffi-dev  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python-pip libcurl4-gnutls-dev python-dev ncurses-dev software-properties-
common  
  
RUN echo ''|add-apt-repository ppa:nginx/stable; apt-get update; apt-get
install -y nginx nginx-extras  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
lua5.1 luarocks liblua5.1-0 liblua5.1-0-dev liblua5.1-json liblua5.1-lpeg2 \  
nodejs-dev npm nodejs-legacy docker.io;\  
npm install -g grunt-cli  
  
RUN luarocks install luasocket;\  
luarocks install luajson;\  
luarocks install penlight;\  
luarocks install lua-spore;\  
luarocks install luacrypto  
  
#mysystem("usermod www-data -G docker");  
ADD ./ /root/dt  
WORKDIR /root/dt  
ENV TARGET /kb/deployment  
ENV PATH
${TARGET}/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
# Remove Old List if List is installed  
RUN perl -e 'use List::Util' && rm perl/List/Util.pm  
  
# Incremental package updates not yet in the run-time  
RUN cpanm -i REST::Client && cpanm -i Time::ParseDate && \  
cd /kb/bootstrap/kb_seed_kmers/ && \  
./build.seed_kmers /kb/runtime/ && \  
cd /kb/bootstrap/kb_glpk/ && \  
./glpk_build.sh /kb/runtime/  
  
# Generate the cluster.ini and hash. Cleanup sensitive files  
RUN cp cluster.ini.docker cluster.ini && ./deploy_cluster mkhashfile tagfile
&& \  
rm -f site.cfg && rm -rf ssl && mkdir -p /kb/deployment/services/meme  
  
# Deploy using awe as the service definition  
RUN MYSERVICES=awe ./deploy_cluster -s deploy local tagfile && \  
find /kb/dev_container/modules -iname ".git" | xargs rm -rf && \  
rm -rf /kb/dev_container/modules/trees/data  
  
# Make things run in the foreground and spit out logs -- hacky  
RUN \  
sed -i 's/--daemonize [^ ]*log//'
/kb/deployment/services/Transform/start_service;\  
sed -i 's/--daemonize//' /kb/deployment/services/*/start_service;\  
sed -i 's/--error-log [^ "]*//' /kb/deployment/services/*/start_service;\  
sed -i 's/--pid [^ "]*//' /kb/deployment/services/*/start_service;\  
[ -e /kb/deployment//services/fbaModelServices/start_service ] && sed -i
's/starman -D/starman/'
/kb/deployment/services/fbaModelServices/start_service;\  
sed -i 's/\/kb\/runtime\/sbin\/daemonize .*\/kb/\/kb/'
/kb/deployment/services/*/start_service;\  
sed -i 's/>.*//' /kb/deployment//services/*/start_service;\  
sed -i 's/nohup //' /kb/deployment//services/*/start_service;\  
sed -i 's/start_service &/start_service/' /root/dt/perl/KBDeploy.pm  
  
RUN \  
cd /kb/dev_container/modules;\  
git clone https://github.com/kbase/ui-common -b staging;\  
git clone \--recurse-submodules https://github.com/kbase/narrative -b docker;\  
rm -rf /kb/dev_container/modules/ui-common/.git
/kb/dev_container/modules/narrative/.git  
  
ONBUILD ENV USER root  
  
ONBUILD ADD cluster.ini /root/dt/cluster.ini  
ONBUILD ADD ssl /root/dt/ssl  
  
# Add the ssl certs into the certificate tree  
ONBUILD RUN cat ssl/proxy.crt >> /etc/ssl/certs/ca-certificates.crt && \  
cat ssl/proxy.crt > /etc/ssl/certs/`openssl x509 -noout -hash -in
ssl/proxy.crt`.0 && \  
cat ssl/narrative.crt >> /etc/ssl/certs/ca-certificates.crt && \  
cat ssl/narrative.crt > /etc/ssl/certs/`openssl x509 -noout -hash -in
ssl/narrative.crt`.0  
  
# This run command does several things including:  
# - Changing the memory size for the workspace  
# - Change memory for other glassfish services  
# - Deploy the nginx config (setup_www)  
# - Run postporcess for shock and awe  
# - Clones special versions of ui-common and narrative  
# cd modules/auth_service;cat /root/dt/auth.fix |patch -p0;make deploy;\  
ONBUILD RUN cp ./cluster.ini /kb/deployment/deployment.cfg;\  
cd /kb/dev_container/;. ./user-env.sh;\  
cd /root/dt; \  
sed -i 's/10000/256/' /kb/deployment/services/workspace/start_service && \  
sed -i 's/15000/384/' /kb/deployment/services/workspace/start_service && \  
sed -i 's/--Xms 1000 --Xmx 2000/--Xms 384 --Xmx 512/'
/kb/deployment/services/*/start_service && \  
cd config;NOSTART=1 MYSERVICES=www ./setup_www;cd ../;\  
./config/postprocess_shock;\  
./config/postprocess_awe;\  
sed -i 's/ssl_verify = True/ssl_verify = False/'
/kb/deployment/lib/biokbase/Transform/script_utils.py;\  
MYSERVICES=Transform ./config/postprocess_Transform;\  
[ -e /mnt/Shock/logs ] || mkdir -p /mnt/Shock/logs;  
  
# We need to refix start  
ONBUILD RUN sed -i 's/start_service &/start_service/'
/root/dt/perl/KBDeploy.pm  
  
# Fix up URLs in clients  
ONBUILD RUN PUBLIC=$(grep baseurl= cluster.ini|sed 's/baseurl=//'|sed
's/:.*//') && \  
sed -i "s|public.hostname.org|$PUBLIC|"
/kb/deployment/lib/biokbase/*/Client.py && \  
sed -i "s|public.hostname.org|$PUBLIC|"
/kb/deployment/lib/Bio/KBase/*/Client.pm && \  
sed -i "s|public.hostname.org|$PUBLIC|"
/kb/deployment/lib/javascript/*/Client.js  
  
ONBUILD ENTRYPOINT [ "./scripts/entrypoint.sh" ]  
ONBUILD CMD [ ]  

