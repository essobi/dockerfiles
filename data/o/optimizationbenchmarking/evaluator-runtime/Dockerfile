#  
# optimizationbenchmarking/evaluator-runtime  
#  
# This is the image of the basic runtime components needed  
# by the elements of the optimizationBenchmarking evaluator.  
#  
#  
FROM debian:8.4  
MAINTAINER Thomas Weise <tweise@ustc.edu.cn>  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list.d/jessie-backports.list &&\  
echo 'deb http://cloud.r-project.org/bin/linux/debian jessie-cran3/' >>
/etc/apt/sources.list &&\  
echo 'deb http://cran.cnr.berkeley.edu/bin/linux/debian jessie-cran3/' >>
/etc/apt/sources.list &&\  
echo 'deb http://cran.uni-muenster.de/bin/linux/debian jessie-cran3/' >>
/etc/apt/sources.list &&\  
echo 'deb http://mirrors.opencas.cn/cran/bin/linux/debian jessie-cran3/' >>
/etc/apt/sources.list &&\  
apt-key adv --keyserver keys.gnupg.net --recv-key 381BA480 &&\  
export LANG=C.UTF-8 &&\  
apt-get clean &&\  
apt-get update &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get update &&\  
apt-get install -f -y apt-utils &&\  
apt-get install -f -y ca-certificates-java \  
ghostscript=9.06* \  
libicu-dev \  
openjdk-8-jdk \  
pkg-config \  
r-base=3.3.* \  
r-base-dev=3.3.* \  
texlive-base \  
texlive-fonts-recommended \  
texlive-luatex \  
texlive-xetex &&\  
/var/lib/dpkg/info/ca-certificates-java.postinst configure &&\  
cd /tmp/ &&\  
R_params="repos=c(\"http://cran.us.r-project.org\",
\"http://cran.uk.r-project.org\", \"http://mirrors.ustc.edu.cn/CRAN\",
\"http://cran.wu.ac.at/\", \"http://cran.utstat.utoronto.ca/\",
\"http://cran.rstudio.com/\", \"https://cran.uni-muenster.de/\",
\"http://ftp.iitm.ac.in/cran/\" ), dependencies=TRUE, clean=TRUE" &&\  
Rscript -e "update.packages(ask=FALSE, ${R_params})" &&\  
Rscript -e "if(!(require(\"apcluster\"))) install.packages(\"apcluster\",
${R_params})" &&\  
Rscript -e "if(!(require(\"cluster\"))) install.packages(\"cluster\",
${R_params})" &&\  
Rscript -e "if(!(require(\"fpc\"))) install.packages(\"fpc\", ${R_params})"
&&\  
Rscript -e "if(!(require(\"mclust\"))) install.packages(\"mclust\",
${R_params})" &&\  
Rscript -e "if(!(require(\"NbClust\"))) install.packages(\"NbClust\",
${R_params})" &&\  
Rscript -e "if(!(require(\"stats\"))) install.packages(\"stats\",
${R_params})" &&\  
Rscript -e "if(!(require(\"vegan\"))) install.packages(\"vegan\",
${R_params})" &&\  
apt-get purge -f -y g++ \  
gcc \  
gfortran \  
libicu-dev \  
make \  
pkg-config \  
r-base-dev \  
texlive-fonts-extra-doc \  
texlive-fonts-recommended-doc \  
texlive-humanities-doc \  
texlive-latex-base-doc \  
texlive-latex-extra-doc \  
texlive-latex-recommended-doc \  
texlive-metapost-doc \  
texlive-pictures-doc \  
texlive-pstricks-doc \  
texlive-science-doc &&\  
apt-get clean &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/ssh/ssh_host_*  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

