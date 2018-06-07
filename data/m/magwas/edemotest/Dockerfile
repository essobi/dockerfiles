FROM ubuntu:trusty  
  
RUN locale-gen en_US en_US.UTF-8 && \  
dpkg-reconfigure locales  
  
RUN apt-get update  
  
RUN apt-get -o Dpkg::Options::="--force-confold" \--force-yes -fuy upgrade  
  
RUN apt-get -y install software-properties-common  
RUN apt-add-repository -y ppa:openjdk-r/ppa  
RUN apt-key adv --keyserver keys.gnupg.net --recv B761AA278C7AB952  
RUN echo deb http://repos.demokracia.rulez.org/apt/debian/ unstable main
>/etc/apt/sources.list.d/repos.demokracia.rulez.org.list  
  
RUN apt-get update  
RUN apt-get -y install openjdk-8-jdk wget git xvfb unzip docbook-xsl make
firefox tightvncserver dblatex libwebkitgtk-3.0-0 libswt-webkit-gtk-3-jni
python-yaml python-pip python-dateutil zip debhelper devscripts zenta-tools  
  
RUN useradd develop  
RUN mkdir /home/develop  
RUN chown develop:develop /home/develop  
  
RUN mkdir /home/develop/lib; cd /home/develop/lib ; wget -q
http://downloads.sourceforge.net/project/saxon/Saxon-
HE/9.4/SaxonHE9-4-0-2J.zip;unzip SaxonHE9-4-0-2J.zip ; rm -f
SaxonHE9-4-0-2J.zip  
  
RUN mkdir /home/develop/build;cd /home/develop/build; git clone
https://github.com/expath/xspec.git  
  
RUN mkdir /opt;cd /opt ; wget -q
http://downloads.sourceforge.net/project/zenta/Zenta-linux.gtk.x86_64.zip ;
unzip Zenta-linux.gtk.x86_64.zip ; rm -f Zenta-linux.gtk.x86_64.zip  
  
RUN wget
"http://search.maven.org/remotecontent?filepath=net/sourceforge/saxon/saxon/9.1.0.8/saxon-9.1.0.8.jar"
-O /usr/local/lib/saxon9.jar  
  
RUN pip install jira  
  
RUN ln -s /home/develop/lib /root/lib  
  
RUN ln -s /home/develop/build /root/build  
  
RUN git config --global user.email "mag+xsltbuilder@magwas.rulez.org"  
RUN git config --global user.name "magwas/edemotest:xslt docker image"  
  
CMD sudo su - develop  
  

