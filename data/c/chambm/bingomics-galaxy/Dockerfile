# Galaxy - Bingomics  
#  
# VERSION Galaxy-central  
FROM chambm/docker-galaxy-stable  
  
MAINTAINER Matt Chambers, matt.chambers@vanderbilt.edu  
  
# Install various tool and development requirements  
# 1. Add R-dev PPA and its public key (then 'apt-get update')  
# 2. Install linuxbrew requirements  
# 3. Install python-h5py (for mz5 support in Galaxy)  
# 4. Install R-3.2 from R-dev PPA  
# 5. Cleanup  
RUN codename=$(lsb_release -c -s) && \  
echo "deb http://mirrors.nics.utk.edu/cran/bin/linux/ubuntu $codename/" | tee
-a /etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \  
echo "deb http://ppa.launchpad.net/marutter/rdev/ubuntu $codename main" | tee
-a /etc/apt/sources.list.d/marutter-rdev-$codename.list && \  
apt-get -qq update && \  
apt-get install -y --no-install-recommends r-base cabextract build-essential
curl git m4 ruby texinfo libbz2-dev libcurl4-openssl-dev libxml2-dev libexpat-
dev libncurses-dev zlib1g-dev libhdf5-dev python-h5py libreadline-dev && \  
sudo -u galaxy ruby -e "$(curl -fsSL
https://raw.githubusercontent.com/Homebrew/linuxbrew/go/install)" && \  
echo export PATH=$PATH:/home/galaxy/.linuxbrew/bin >> /home/galaxy/.bashrc &&
\  
apt-get purge -y software-properties-common && \  
apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
  
### WINE support currently not working  
# Add i386 architecture and run apt-get update  
# Install wine and xvfb (console frame buffer for X11)  
# Download winetricks from their site and make it executable  
#RUN dpkg --add-architecture i386 && apt-get -qq update && \  
# apt-get install -y --no-install-recommends wine xvfb && \  
# wget
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
&& chmod ugo+rx winetricks && chown galaxy:galaxy winetricks && mv winetricks
/usr/local/bin && \  
# apt-get purge -y software-properties-common && \  
# apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  
# Install BioConductor and proBAMr  
RUN R --vanilla -e 'source("http://bioconductor.org/biocLite.R");
biocLite(ask=F)' && \  
R --vanilla -e 'source("http://bioconductor.org/biocLite.R");
biocLite(c("RGalaxy", "proBAMr"), ask=F)'  
  
# /etc/ssl/private can't be accessed from within container for some reason  
# (@andrewgodwin says it's something AUFS related) - taken from
https://github.com/orchardup/docker-postgresql/blob/master/Dockerfile  
# MCC: this seems necessary for the Docker Hub build, which must be using
AUFS; my local builds using devicemapper work without this  
RUN cp -r /etc/ssl /tmp/ssl-copy/ && \  
chmod -R 0700 /etc/ssl && \  
chown -R postgres /tmp/ssl-copy && \  
rm -r /etc/ssl && \  
mv /tmp/ssl-copy /etc/ssl  
  
# Install Bingomics tools into Galaxy  
RUN add-tool-shed --url 'http://testtoolshed.g2.bx.psu.edu/' \--name 'Test
Tool Shed' && \  
install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name
myrimatch" \  
"--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name idpqonvert" \  
"--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name idpassemble" \  
"--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name idpquery" \  
"--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name msconvert" \  
"--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp --name psm_to_sam" \  
"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name sam_to_bam" \  
"--url http://toolshed.g2.bx.psu.edu/ -o devteam --name sam_merge"  
  
RUN install-repository "--url http://testtoolshed.g2.bx.psu.edu/ -o galaxyp
--name msgfplus"  
  
# The following commands will be executed as user galaxy  
USER galaxy  
  
# BASH_ENV tells bash what to do for non-interactive logins  
ADD .bashrc /home/galaxy/.bashrc  
ENV PATH=$PATH:/home/galaxy/.linuxbrew/bin BASH_ENV=/home/galaxy/.bashrc  
  
# Install planemo (will be installed in linuxbrew's bin directory)  
RUN brew tap galaxyproject/tap && brew install planemo --HEAD  
  
ENV GALAXY_CONFIG_BRAND="Bingomics" \  
GALAXY_CONFIG_JOB_WORKING_DIRECTORY=/export/galaxy-
cluster/job_working_directory \  
GALAXY_CONFIG_FILE_PATH=/export/galaxy-central/database/files \  
GALAXY_CONFIG_NEW_FILE_PATH=/export/galaxy-central/database/files \  
GALAXY_CONFIG_TEMPLATE_CACHE_PATH=/galaxy-central/database/compiled_templates
\  
GALAXY_CONFIG_CITATION_CACHE_DATA_DIR=/galaxy-central/database/citations/data
\  
GALAXY_CONFIG_CLUSTER_FILES_DIRECTORY=/export/galaxy-cluster/pbs \  
GALAXY_CONFIG_FTP_UPLOAD_DIR=/export/galaxy-central/database/ftp \  
GALAXY_CONFIG_FTP_UPLOAD_SITE=192.168.33.10 \  
ENABLE_TTS_INSTALL=True  
  
WORKDIR /galaxy-central  
  
# set WINEPREFIX and WINEARCH for galaxy user  
ENV WINEPREFIX=$HOME/.wine32 WINEARCH=win32  
  
#RUN xvfb-run winetricks -q winxp vcrun2005 win7 vcrun2008 vcrun2010 vcrun2012
vcrun2013  
#RUN xvfb-run winetricks -q dotnet35sp1 dotnet40  
USER root  
  
RUN mkdir /export/galaxy-cluster && chown galaxy:galaxy /export/galaxy-cluster  
  
# Updating genome informations from UCSC  
#RUN export GALAXY=/galaxy-central && sh ./cron/updateucsc.sh.sample  
# Container Style  
#ADD GalaxyDocker.png $GALAXY_CONFIG_DIR/web/welcome_image.png  
#ADD welcome.html $GALAXY_CONFIG_DIR/web/welcome.html  
# Mark folders as imported from the host.  
VOLUME ["/export/", "/data/", "/var/lib/docker"]  
  
# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy), 9009 (toolshed)  
EXPOSE :80 :21 :8800 :9009  
# Autostart script that is invoked during container start  
CMD ["/usr/bin/startup"]

