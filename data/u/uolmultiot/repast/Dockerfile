#Since this is a Dev container, for enabling sharing volumes with host is
required to build this way:  
#docker build --build-arg UID={YOUR HOST UID} -t uolmultiot/repast .  
FROM openjdk:8 as builder  
  
ARG USER=ruser  
ARG UID=1000  
ENV
ECP_URL=http://www.mirrorservice.org/sites/download.eclipse.org/eclipseMirror/technology/epp/downloads/release/oxygen/1a/  
ENV ECP_PKG=eclipse-committers-oxygen-1a-linux-gtk-x86_64.tar.gz  
ENV GRECLIPSE=http://dist.springsource.org/snapshot/GRECLIPSE/e4.7/  
ENV REPAST=https://repocafe.cels.anl.gov/repos/repast  
  
RUN useradd -u $UID -ms /bin/bash $USER  
  
#eclipse  
WORKDIR /root/  
RUN wget "$ECP_URL$ECP_PKG" \  
&& tar -xf $ECP_PKG \  
&& rm $ECP_PKG \  
&& sed -i
's/"-Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel"//g'
/root/eclipse/eclipse  
  
#repast  
RUN ./eclipse/eclipse -nosplash -application org.eclipse.equinox.p2.director
-repository http://download.eclipse.org/releases/neon/,$GRECLIPSE -installIU
org.codehaus.groovy.eclipse.feature.feature.group \  
&& ./eclipse/eclipse -nosplash -application org.eclipse.equinox.p2.director
-repository http://download.eclipse.org/releases/neon/,$REPAST -installIU
repast.simphony.feature.feature.group  
  
FROM openjdk:8  
#Default user  
ARG USER=ruser  
ARG UID=1000  
RUN apt-get update && apt-get install -y \  
# For eclipse  
libx11-6 libxext-dev libxrender-dev libxtst-dev libcanberra-gtk-module \  
\--no-install-recommends \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
#Add user for enabling sharing of volume with host  
&& useradd -u $UID -s /bin/bash $USER \  
&& mkdir -p /home/$USER/workspace \  
&& chown -R $USER:$USER /home/$USER  
USER $USER  
WORKDIR /home/$USER  
COPY \--from=builder /root/eclipse ./eclipse  

