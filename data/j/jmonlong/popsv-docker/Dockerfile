## Pull base image  
FROM ubuntu:14.04  
# ______________________ _____ __ _________ __  
# / _/ ____/ ____/ ____/ / ___// /_____ _________ _____ ____ / ____/ (_)__
____ / /_  
# / // / / / __/ / \\__ \/ __/ __ \/ ___/ __ `/ __ `/ _ \ / / / / / _ \/ __ \/
__/  
# _/ // /___/ /_/ / /___ ___/ / /_/ /_/ / / / /_/ / /_/ / __/ / /___/ / / __/
/ / / /_  
# /___/\\____/\\____/\\____/ /____/\\__/\\____/_/ \\__,_/\\__, /\\___/
\\____/_/_/\\___/_/ /_/\\__/  
# /____/  
# Banner @ http://goo.gl/VCY0tD  
WORKDIR /  
  
#  
# Update apt, add FUSE support and basic command line tools  
#  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y libfuse-dev fuse curl wget software-properties-common  
  
#  
# Install Oracle JDK 8  
#  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update && apt-get upgrade -y  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#  
# Install latest version of storage client distribution  
#  
RUN mkdir -p /icgc/icgc-storage-client && \  
cd /icgc/icgc-storage-client && \  
wget -qO- https://dcc.icgc.org/api/v1/ui/software/icgc-storage-client/latest |
\  
tar xvz --strip-components 1  
  
## Install OpenStack/AWS Command Line Interface  
RUN apt-get update && \  
apt-get install -y python-dev python-pip  
  
RUN mkdir -p /root/.aws && \  
pip install awscli python-openstackclient  
  
## Install Emacs  
RUN apt-get update && \  
apt-get install -y emacs  
  
## Install R  
RUN add-apt-repository "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/"
&& \  
gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \  
gpg -a --export E084DAB9 | apt-key add - && \  
apt-get update && \  
apt-get install -y r-base r-base-dev r-cran-rcurl libreadline-dev && \  
apt-get install -y r-cran-getopt littler && \  
apt-get install -y libcurl4-openssl-dev libxml2-dev && \  
echo 'options(repos=structure(c(CRAN="http://cran.rstudio.com")))' >>
/usr/lib/R/etc/Rprofile.site && \  
echo "PKG_CXXFLAGS = '-std=c++11'" >> /usr/lib/R/etc/Makeconf.site && \  
echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-
library:/usr/local/lib/R/library:/usr/lib/R/library'}" >>
/usr/lib/R/etc/Renviron && \  
ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r &&
\  
ln -s /usr/share/doc/littler/examples/installGithub.r
/usr/local/bin/installGithub.r && \  
ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r && \  
echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r && \  
install.r docopt && \  
rm -rf /tmp/downloaded_packages/ /tmp/*.rds /var/tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean  
  
# ____ _____ _ __  
# / __ \ ____ ____ / ___/| | / /  
# / /_/ // __ \ / __ \ \\__ \ | | / /  
# / ____// /_/ // /_/ /___/ / | |/ /  
# /_/ \\____// .___//____/ |___/  
# /_/  
#  
# Banner at
http://patorjk.com/software/taag/#p=display&h=1&v=2&f=Slant&t=PopSV  
## Install required packages  
RUN install2.r --error \  
-r "https://cran.rstudio.com" \  
-r "http://www.bioconductor.org/packages/release/bioc" \  
devtools \  
Rsamtools \  
DNAcopy \  
BatchJobs \  
&& installGithub.r jmonlong/PopSV \  
&& rm -rf /tmp/downloaded_packages/ /tmp/*.rds  
  
## Set working directory  
WORKDIR /root  
  
## Copy useful genome binning (in order to avoid installing heavy
BSgenome.Hsapiens.UCSC.hg19)  
COPY bins-500bp.RData ./  
COPY bins-1kbp.RData ./  
COPY bins-2kbp.RData ./  
COPY bins-5kbp.RData ./  
  
## Clone GitHub Repo  
RUN apt-get update \  
&& apt-get install -y git \  
&& git clone https://github.com/jmonlong/PopSV.git -b icgc  
  
## Install ESS mode  
RUN git clone https://github.com/emacs-ess/ESS.git /root/.emacs.d/lisp/ess  
COPY .emacs /root/  

