FROM canmet/docker-openstudio  
  
MAINTAINER Phylroy Lopez phylroy.lopez@canada.ca  
  
ARG DISPLAY=local  
ENV DISPLAY ${DISPLAY}  
  
#Repository utilities add on list.  
ARG repository_utilities='ca-certificates software-properties-common python-
software-properties dpkg-dev debconf-utils'  
#Basic software  
ARG software='git vim curl zip lynx xemacs21 nano unzip xterm terminator
midori diffuse silversearcher-ag openssh-client'  
#Netbeans Dependancies (requires $java_repositories to be set)  
ARG netbeans_deps='oracle-java8-installer libxext-dev libxrender-dev libxtst-
dev oracle-java8-set-default'  
#VCCode Dependancies  
ARG vscode_deps='curl libc6-dev libasound2 libgconf-2-4 libgnome-keyring-dev
libgtk2.0-0 libnss3 libpci3 libxtst6 libcanberra-gtk-module libnotify4 libxss1
wget'  
#Java repositories needed for Netbeans  
#D3 parallel coordinates deps due to canvas deps  
ARG d3_deps='libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-
essential g++'  
#Purge software  
ARG intial_purge_software='openjdk*'  
#set Java ENV  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $JAVA_HOME/bin:$PATH  
  
#Ubuntu install commands  
ARG apt_install='apt-get install -y --no-install-recommends --force-yes'  
#Ubuntu install clean up command  
ARG clean='rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /downloads/*'  
#Create folder for downloads  
RUN mkdir /downloads  
#Install software packages  
RUN apt-get update && $apt_install $software $d3_deps $r_deps
$repository_utilities \  
&& apt-get clean && $clean  
  
  
#### Build sqlite with json support  
RUN curl -fSL -o sqlite.tar.gz https://www.sqlite.org/2017/sqlite-
autoconf-3160200.tar.gz \  
&& mkdir /usr/src/sqlite3 \  
&& tar -xzf sqlite.tar.gz -C /usr/src/sqlite3 \  
&& rm sqlite.tar.gz \  
&& cd /usr/src/sqlite3/sqlite-autoconf-3160200 \  
&& ./configure --prefix=/usr/local --enable-json1 --enable-readline \  
&& make \  
&& make install \  
&& make clean  
  
# MongoDB:  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 \  
&& apt-get install -y --no-install-recommends software-properties-common \  
&& echo "deb http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-release | grep
DISTRIB_CODENAME | cut -d= -f2)/mongodb-org/3.2 multiverse" | tee
/etc/apt/sources.list.d/mongodb-org-3.2.list  
# Update apt-get sources AND install MongoDB  
RUN apt-get update && apt-get install -y mongodb-org  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
# Expose port 27017 from the container to the host  
EXPOSE 27017  
#Update NodeJS and express  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash - \  
&& apt-get install -y nodejs nodejs build-essential \  
&& npm install -g express-generator nodemon bower  
EXPOSE 3000  
#install Amazon AWS CLI and packer  
RUN wget
https://releases.hashicorp.com/packer/1.0.0/packer_1.0.0_linux_amd64.zip \  
&& unzip packer_1.0.0_linux_amd64.zip -d /usr/bin/ \  
&& rm packer_1.0.0_linux_amd64.zip  
RUN curl -O http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip \  
&& mkdir /usr/local/ec2 \  
&& unzip ec2-api-tools.zip -d /usr/local/ec2 \  
&& mv `find /usr/local/ec2/ec2-api-tools-* -maxdepth 0`
/usr/local/ec2/ec2-api-tools \  
&& rm ec2-api-tools.zip  
ENV EC2_HOME=/usr/local/ec2/ec2-api-tools  
  
  
USER osdev  
WORKDIR /home/osdev  
  
# Install RubyMine  
RUN wget https://download.jetbrains.com/ruby/RubyMine-2017.2.3.tar.gz \  
&& tar -xzf RubyMine-2017.2.3.tar.gz \  
&& rm RubyMine-2017.2.3.tar.gz  
  
#create symbolic link to rubymine and set midori to default browser  
USER root  
RUN ln -s /home/osdev/RubyMine-2017.2.3/bin/rubymine.sh
/usr/local/sbin/rubymine \  
&& ln -s /usr/bin/midori /bin/xdg-open  
  
USER osdev  
RUN echo 'PATH="~/btap_utilities:$PATH"' >> ~/.bashrc \  
&& git clone https://github.com/canmet-energy/btap_utilities.git \  
&& cd ~/btap_utilities && chmod 774 * \  
&& /bin/bash -c "source /etc/user_config_bashrc" \  
&& cd ~/btap_utilities && ./configure_user.sh  
  
CMD ["/bin/bash"]  
  

