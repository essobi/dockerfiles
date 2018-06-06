FROM ubuntu:14.04.2  
MAINTAINER Olexander Kutsenko <olexander.kutsenko@gmail.com>  
  
#install  
RUN apt-get update -y  
RUN apt-get install -y software-properties-common python-software-properties  
RUN apt-get install -y git git-core vim nano mc nginx screen curl unzip zip  
RUN mkdir /var/www  
RUN chown -R www-data:www-data /var/www  
COPY configs/nginx/default /etc/nginx/sites-available/default  
  
# SSH service  
RUN sudo apt-get install -y openssh-server openssh-client  
RUN sudo mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#configs bash start  
COPY configs/autostart.sh /root/autostart.sh  
COPY configs/android_config.sh /root/android_config.sh  
RUN chmod +x /root/*.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
  
#Ant install  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
#Install Java7  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java7-installer  
#Install Java8  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
RUN apt-get install -y ant  
  
#aliases  
RUN alias ll='ls -la'  
  
#Install Gradle  
RUN echo "Start Setup Gradle"  
RUN add-apt-repository -y ppa:cwchien/gradle  
RUN apt-get update  
RUN apt-get install -y gradle  
RUN echo "Start Setup Gradle is done"  
  
#Install TeamCity BuildAgent  
COPY buildAgent /opt/buildAgent  
RUN ls -la /opt  
RUN chmod +x /opt/buildAgent/bin/*.sh  
  
#install Android SDK  
RUN wget http://dl.google.com/android/android-sdk_r24.3.3-linux.tgz  
RUN tar -xvzf android-sdk_r24.3.3-linux.tgz  
RUN mv android-sdk-linux /opt/android-sdk-linux  
RUN rm android-sdk_r24.3.3-linux.tgz  
  
#install Android NDK  
RUN wget http://dl.google.com/android/ndk/android-ndk-r10e-linux-x86_64.bin  
RUN chmod +x android-ndk-r10e-linux-x86_64.bin  
RUN ./android-ndk-r10e-linux-x86_64.bin  
RUN mv android-ndk-r10e /opt/android-ndk-r10e  
RUN rm android-ndk-r10e-linux-x86_64.bin  
  
#Add colorful command line  
RUN echo "force_color_prompt=yes" >> .bashrc  
  
#open ports  
EXPOSE 80 22  

