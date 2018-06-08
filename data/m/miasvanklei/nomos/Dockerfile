FROM heichblatt/archlinux-yaourt:latest  
  
LABEL version "1.0"  
LABEL description "Docker image with certain tools"  
LABEL homepage "https://github.com/miasvanklei/Nomos"  
LABEL repository "https://github.com/miasvanklei/Nomos"  
  
USER user  
RUN echo "LC_ALL=en_US.UTF-8" | sudo tee -a /etc/environment  
RUN echo "en_US.UTF-8 UTF-8" | sudo tee -a /etc/locale.gen  
RUN echo "LANG=en_US.UTF-8" | sudo tee /etc/locale.conf  
RUN sudo locale-gen en_US.UTF-8  
RUN yaourt --noconfirm -Syu --devel --aur  
RUN yaourt --noconfirm -S jdk8-openjdk npm yarn ffmpeg libepoxy libreoffice
ttf-dejavu ttf-liberation  
RUN yaourt --noconfirm -S frog  
RUN yaourt --noconfirm -S chromium  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk  

