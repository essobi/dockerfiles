FROM debian:jessie  
MAINTAINER r.szkup@auckland.ac.nz  
  
## Add repository for R  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 381BA480 && \  
echo "deb http://cran.stat.auckland.ac.nz/bin/linux/debian jessie-cran3/" |
tee -a /etc/apt/sources.list.d/R.list  
## unhash if you want to check available versions  
#RUN apt-cache show r-base-core | grep Version && exit 1  
# Install wget, libssl, r-base-core and shiny's libs  
RUN apt-get update && \  
apt-get -y -q install wget \  
libcurl4-openssl-dev libxml2-dev libssl-dev libssl1.0.0 sudo && \  
wget
http://ftp.us.debian.org/debian/pool/main/o/openssl/libssl0.9.8_0.9.8o-4squeeze14_amd64.deb
&& \  
dpkg -i ./libssl0.9.8_0.9.8o-4squeeze14_amd64.deb && \  
rm -f ./libssl0.9.8_0.9.8o-4squeeze14_amd64.deb --  
  
RUN apt-get -y -q install r-base-core && \  
R -e "install.packages(c('devtools', 'shiny', 'DT', 'rmarkdown', 'GGally'),
repos='http://cran.rstudio.com/', lib='/usr/lib/R/site-library')" && \  
R -e "devtools::install_github('ramnathv/rCharts')" && \  
rm -rf /var/lib/apt/lists/* --  
  
# Install Shiny server  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.4.0.756-amd64.deb && \  
dpkg -i shiny-server-1.4.0.756-amd64.deb && \  
rm shiny-server-1.4.0.756-amd64.deb -- && \  
sed -i '1s/^/access_log \/var\/log\/shiny-server\/access.log default; \n/'
/etc/shiny-server/shiny-server.conf  
  
## Download from git and install application  
RUN R -e "install.packages(c('iNZightMR', 'iNZightTS', 'iNZightRegression',
'iNZightPlots'), \  
repos = c('http://docker.stat.auckland.ac.nz/R',
'http://cran.stat.auckland.ac.nz'))"  
  
EXPOSE 3838  
CMD ["sudo", "-u", "shiny", "/usr/bin/shiny-server"]  

