FROM phase2/devtools-build  
MAINTAINER Mike Potter  
  
# Install packages  
RUN yum -y install \  
java-1.7.0-openjdk \  
firefox-31.6.0-2.el7.centos \  
Xvfb \  
libXfont \  
xorg-x11-utils \  
x11vnc  
  
# This is needed on CentOs for Firefox to communicate with dbus  
# Without this, Selenium won't be able to connect to Firefox  
RUN dbus-uuidgen --ensure  
  
# Create "behat" user with password crypted "behat"  
# Add "behat" to "sudoers"  
RUN useradd -d /home/behat -m -s /bin/bash behat \  
&& echo "behat:behat" | chpasswd \  
&& chown -R behat:behat /home/behat \  
&& echo "behat ALL=(ALL:ALL) ALL" >> /etc/sudoers  
  
USER behat  
WORKDIR /home/behat  
ENV HOME /home/behat  
ENV PATH $PATH:/home/behat  
  
# Install selenium  
RUN mkdir /home/behat/selenium \  
&& curl -O "http://selenium-release.storage.googleapis.com/2.48/selenium-
server-standalone-2.48.2.jar" \  
&& mv selenium-server-standalone-2.48.2.jar /home/behat/selenium  
  
# VNC Setup  
RUN mkdir /home/behat/.vnc \  
&& x11vnc -storepasswd behat /home/behat/.vnc/passwd  
EXPOSE 5900  
# Install Behat stuff  
RUN mkdir /home/behat/composer  
WORKDIR /home/behat/composer  
COPY composer.json /home/behat/composer/composer.json  
RUN composer install  
  
ENV TESTS /home/behat  
ENV CONFIG behat.yml  
ENV GEOMETRY "2280x1024x8"  
COPY root /  
  
ENTRYPOINT ["/opt/bin/entry_point.sh"]  
CMD /bin/bash  
  
# RUN container with:  
# docker run -it --rm -h phase2/behat --link support_db_1:db -e
"TESTS=/data/docroot/profiles/openatrium/modules/contrib/oa_test/tests" -e
"CONFIG=behat.local.yml" -v $(pwd):/data:rw phase2/behat  

