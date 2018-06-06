# ----------------------------------------------------------------------  
# Dockerfile for installing most commonly use languages / packages  
# for DataScience  
# To be used with a Spark pre-built binary  
# ----------------------------------------------------------------------  
FROM ubuntu:14.04  
MAINTAINER Karen Ng <karen.yyng@gmail.com>  
  
RUN echo "\n\n---------- Downloading and building all OS level tools-----\n\n"  
RUN apt update  
# -y flag bypasses all questions  
RUN apt install -y build-essential software-properties-common git  
RUN echo "\n\n---------- Finished building all OS level tools----------- \n\n"  
  
# ----- Install R by adding suitable download mirrors to apt package
listings--  
RUN echo "\n\n---------- Downloading and building R ---------------------\n\n"  
RUN echo 'deb http://cran.cnr.berkeley.edu/bin/linux/ubuntu trusty/' >>
/etc/apt/sources.list  
# Add the GPG key for R  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
# Must update software indices again  
RUN apt update  
RUN apt install -y r-base r-base-dev  
# Supply a Rscript here to install R packages  
RUN echo "\n\n---------- Finished building R --------------------------- \n\n"  
  
# ----- Python 3.4 is installed by default ----------------------------  
RUN echo "---------- Downloading and building Python 3 packages ------------ "  
# All essential Python debugger, installation utilities  
RUN apt install -y python3-ipdb python3-pip python3-pytest python3-dev  
# Install all the Python Data Science packages  
RUN apt install -y python3-matplotlib python3-pandas python3-h5py  
RUN pip3 install sklearn  
RUN pip3 install bokeh  
RUN pip3 install jupyter  
RUN echo "\n\n---------- Finished building Python 3 -------------------- \n\n"  
  
RUN echo "---------- Downloading and building Java 7 packages ------------ "  
RUN apt install -y python-software-properties  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt update  
# Bypass license agreement  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
RUN apt install -y oracle-java7-installer  
RUN apt install libjansi-java libjansi-native-java libhawtjni-runtime-java  
RUN echo "\n\n---------- Finished building Java 7 -------------------- \n\n"  
  
RUN echo "---------- Downloading and building Scala 2.10 packages ------------
"  
RUN wget www.scala-lang.org/files/archive/scala-2.10.4.deb  
RUN dpkg -i scala-2.10.4.deb  
RUN rm scala-2.10.4.deb  
RUN echo "\n\n---------- Finished building Scala 2.10 --------------------
\n\n"  
  

