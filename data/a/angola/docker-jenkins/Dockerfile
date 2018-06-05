FROM jenkins:2.32.1  
USER root  
ARG user=root  
  
# chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
  
# apt install && update  
RUN apt-get update && apt-get install -y google-chrome-stable xvfb sudo fonts-
vlgothic  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
#font  
RUN mkdir -p /usr/lib/jvm/java-8-openjdk-amd64/jre/font/fallback  
RUN ln -s /usr/share/fonts/truetype/vlgothic/VL-PGothic-Regular.ttf
/usr/lib/jvm/java-8-openjdk-amd64/jre/font/fallback/  
  
# sudo  
RUN sed -i -e 's/%sudo\s*ALL=(ALL:ALL)\sALL/%sudo ALL=(ALL:ALL) NOPASSWD:
ALL/g' /etc/sudoers  
RUN usermod -aG sudo ${user}  
  
# jenkins plugin  
USER ${user}  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  

