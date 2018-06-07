FROM openjdk:slim  
  
# install xvfb and jni  
RUN apt-get update && apt-get install -y libswt-gtk2-4-jni xvfb && rm -rf
/var/lib/apt/lists/*  
  
# clear cache to conserve space  
RUN apt-get clean  
  
# disable assistive technologies  
RUN sed -i 's/^assistive_technologies=/#&/'
/etc/java-8-openjdk/accessibility.properties  
  
COPY xvfb /etc/init.d/xvfb  
RUN chmod +x /etc/init.d/xvfb  
  
RUN echo "service xvfb start" >> /etc/bash.bashrc  
ENV DISPLAY :99  
RUN mkdir -p /katalon  
WORKDIR /katalon  
  
COPY katalon_studio_linux_64 /katalon  
  
RUN ln -s /docker-java-home/jre jre  
RUN ln -s /katalon/katalon /usr/bin/katalon  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  

