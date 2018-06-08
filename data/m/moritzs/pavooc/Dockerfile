FROM python:3  
RUN sh -c 'curl -sL https://deb.nodesource.com/setup_8.x | bash -'  
RUN apt-get update  
RUN apt-get install -y nodejs mongodb-clients  
  
# install java8 with webupd8 repository  
RUN \  
echo "===> add webupd8 repository..." && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
apt-get update && \  
\  
\  
echo "===> install Java" && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes oracle-
java8-installer oracle-java8-set-default && \  
\  
\  
echo "===> clean up..." && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# workaround for scikit-bio  
RUN pip install numpy requests  
ADD requirements.txt /usr/app/requirements.txt  
WORKDIR /usr/app  
RUN pip install -r requirements.txt  
  
RUN wget
https://github.com/aaronmck/FlashFry/releases/download/1.7.5/FlashFry-
assembly-1.7.5.jar  
ADD . /usr/app  
  
# download data, do all preprocessing  
CMD ["python", "-m", "pavooc.server.main"]  

