FROM tiokksar/debian  
  
MAINTAINER Tomasz Tokarski tomasz@tomasztokarski.com  
  
RUN mkdir -p /opt/jdk  
RUN wget --no-check-certificate --header="Cookie: oraclelicense=a" \  
-qO- http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.tar.gz | tar zx --directory /opt/jdk  
RUN ln -s /opt/jdk/bin/* /usr/local/bin  
  
ENV HOME /home/dev  
  
USER dev  
  
RUN wget -qO-
http://ftp.fau.de/eclipse/technology/epp/downloads/release/luna/SR2/eclipse-
java-luna-SR2-linux-gtk-x86_64.tar.gz | tar zx --directory /home/dev  
  
RUN DISPLAY=:1 $HOME/eclipse/eclipse -nosplash -consolelog -debug -application
org.eclipse.equinox.p2.director -repository
http://download.eclipse.org/releases/luna -installIU
org.eclipse.dltk.core.feature.group  
RUN DISPLAY=:1 $HOME/eclipse/eclipse -nosplash -consolelog -debug -application
org.eclipse.equinox.p2.director -repository
http://download.eclipse.org/releases/luna -installIU
org.eclipse.dltk.ruby.feature.group  
RUN DISPLAY=:1 $HOME/eclipse/eclipse -nosplash -consolelog -debug -application
org.eclipse.equinox.p2.director -repository
http://download.eclipse.org/releases/luna -installIU
org.eclipse.jdt.feature.group  
RUN DISPLAY=:1 $HOME/eclipse/eclipse -nosplash -consolelog -debug -application
org.eclipse.equinox.p2.director -repository http://download.scala-
ide.org/sdk/lithium/e44/scala211/stable/site -installIU org.scala-
ide.sdt.feature.feature.group  
  
WORKDIR /home/dev  
  
RUN wget
http://heanet.dl.sourceforge.net/project/eclim/eclim/2.4.1/eclim_2.4.1.jar &&\  
java -Dvim.files=$HOME/.nvim -Declipse.home=$HOME/eclipse -jar eclim_2.4.1.jar
install &&\  
rm eclim_2.4.1.jar  

