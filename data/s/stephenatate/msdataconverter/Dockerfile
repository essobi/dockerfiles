FROM ubuntu:16.04  
# Let apt-get know we are running in noninteractive mode  
#ENV DEBIAN_FRONTEND noninteractive  
## Make sure image is up-to-date  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
## Download and compile the mono modified LLVM  
RUN apt-get -y install build-essential  
RUN apt-get -y install autoconf  
RUN apt-get -y install libtool  
RUN apt-get -y install gettext  
RUN apt-get -y install git  
RUN apt-get -y install wget  
RUN apt-get -y install cmake  
RUN apt-get -y install python  
RUN apt-get -y install unzip  
  
RUN wget http://download.mono-project.com/repo/xamarin.gpg  
RUN apt-key add xamarin.gpg  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
--append /etc/apt/sources.list.d/mono-xamarin.list  
RUN apt-get -y update  
RUN apt-get -y install mono-complete  
  
#RUN certmgr -ssl -m https://go.microsoft.com  
#RUN certmgr -ssl -m https://nugetgallery.blob.core.windows.net  
#RUN certmgr -ssl -m https://nuget.org  
RUN mozroots --import --sync  
  
## Add in the Mono Build of DataConverter  
ADD /output/WiffConverter/bin/ /usr/local/bin/sciex/wiffconverter  
ADD . /data  
ADD . /output  
  
#ADD msconvert /usr/local/bin/msconvert  
RUN ZIP=pwiz-bin-linux-x86_64-gcc48-release-3_0_9740.zip && \  
wget https://github.com/BioDocker/software-
archive/releases/download/proteowizard/$ZIP -O /tmp/$ZIP && \  
unzip /tmp/$ZIP -d /usr/local/bin/pwiz/ && \  
chmod -R 755 /usr/local/bin/pwiz/* && \  
rm /tmp/$ZIP  
  
ENV PATH /usr/local/pwiz/:$PATH  
  
# Installing DIA-Umpire  
RUN ZIP=v2.1.2.zip && \  
wget https://github.com/Nesvilab/DIA-Umpire/releases/download/v2.1.2/$ZIP -O
/tmp/$ZIP && \  
unzip /tmp/$ZIP -d /usr/local/bin/DIA-Umpire/ && \  
chmod -R 755 /usr/local/bin/DIA-Umpire/ && \  
rm /tmp/$ZIP

