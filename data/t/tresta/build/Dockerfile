FROM tresta/core6:latest  
# prepare the directories  
# install git from source; because the highest version of git supported is
1.7.1, and we need 1.7.10+  
COPY ./git-2.6.3.tar.gz /opt/installs-src/git-2.6.3.tar.gz  
COPY ./installGit.sh /opt/tresta-installs/installGit.sh  
RUN ["chmod", "+x", "/opt/tresta-installs/installGit.sh"]  
RUN ["/opt/tresta-installs/installGit.sh"]  
  
# install erlang R15b03, which is not part of any repo  
RUN ["yum", "install", "-y", "mesa-libGL", "mesa-libGLU", "unixODBC",
"wxBase", "wxGTK", "wxGTK-gl"]  
COPY ./esl-erlang_15.b.3-1-centos-6_amd64.rpm /opt/tresta-installs/esl-
erlang_15.b.3-1-centos-6_amd64.rpm  
RUN ["rpm", "-Uvh", "/opt/tresta-installs/esl-
erlang_15.b.3-1-centos-6_amd64.rpm"]  
  
# Install 3rd party build dependencies  
RUN ["yum", "install", "-y", "zip", "unzip", "libxslt", "expat-devel",
"gcc-c++", "zlib-devel", "libxml2-devel", "make", "nc"]  
  
# Install tresta build dependencies  
RUN ["yum", "install", "-y", "rpm-build"]  
RUN ["gem", "install", "sass", "-v", "3.3.8"]  
RUN ["npm", "install", "-g", "grunt-cli"]  

