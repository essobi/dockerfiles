# Pull base image.  
FROM fedora  
MAINTAINER Alexis Jeandet "alexis.jeandet@member.fsf.org"  
# Install.  
RUN dnf install -y qemu-kvm genisoimage unzip xonsh  
  
# Add files.  
RUN mkdir -p /macos/iso/buildAgent  
ADD start_osx.xsh /macos/  
ADD start.sh /macos/iso/  
ADD tc.sh /macos/iso/  
ADD enoch_rev2883_boot /macos  
  
ADD https://teamcity.jetbrains.com/update/buildAgent.zip /macos/  
RUN unzip /macos/buildAgent.zip -d /macos/iso/buildAgent/ && \  
chmod +x /macos/start_osx.xsh && \  
chmod +x /macos/iso/start.sh && \  
chmod +x /macos/iso/tc.sh && \  
echo "system.osx=true" >>
/macos/iso/buildAgent/conf/buildAgent.dist.properties && \  
echo "system.os=OSX" >> /macos/iso/buildAgent/conf/buildAgent.dist.properties  
  
# Define working directory.  
WORKDIR /macos  
  
# Ports open.  
EXPOSE 22 5800 5900 5901  
# Define default command.  
CMD ./start_osx.xsh  

