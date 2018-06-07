#------------------------------------------------#  
# * Copyright 2017 Flyability SA  
# * Alex Pabouctsidis  
#  
# * This docker file is used to create our eclipse buildbot image  
# which is used by bitbucket pipelines. The image is based on ubuntu,  
# to which we add the GCC ARM toolchain & Eclipse + Plugins.  
#  
# The eclipse download link is specific to the eclipse version and  
# must be changed manually after each no release. The link may  
# also break at any time.  
#------------------------------------------------#  
# Pull base image.  
FROM ubuntu  
  
# add GCC PAA  
RUN apt-get update && apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:team-gcc-arm-embedded/ppa  
  
# install required toolchains  
RUN apt-get update && apt-get install -y \  
gcc-arm-embedded \  
build-essential \  
gcc-multilib \  
gcc-4.9-multilib \  
g++-4.9-multilib \  
git \  
default-jre \  
sshpass && \  
mkdir /home/build/  
  
  
# download eclipse  
ADD http://eclipse.bluemix.net/packages/oxygen/data/eclipse-cpp-oxygen-R-
linux-gtk-x86_64.tar.gz /home  
  
# extract and delete zip  
RUN tar xvf /home/eclipse-cpp-oxygen-R-linux-gtk-x86_64.tar.gz -C /home && \  
rm /home/eclipse-cpp-oxygen-R-linux-gtk-x86_64.tar.gz  
  
# install eclipse GNU ARM Eclipse plugin  
RUN /home/eclipse/eclipse -application org.eclipse.equinox.p2.director
-noSplash \  
-repository http://gnuarmeclipse.sourceforge.net/updates \  
-installIU ilg.gnuarmeclipse.managedbuild.cross.feature.group   
  
# Define working directory.  
WORKDIR /home  
  
# Define default command.  
CMD ["bash"]

