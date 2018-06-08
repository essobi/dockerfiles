FROM slaves/cmake:llvm  
  
# Apt packages  
ADD apt_requirements.txt apt_requirements.txt  
RUN apt-get update  
RUN apt-get install -y $(grep -vE "^\s*#" apt_requirements.txt | tr "\n" " ")  
  
# Install clion  
RUN wget https://download.jetbrains.com/cpp/CLion-2017.2.3.tar.gz -O
clion.tar.gz && \  
tar zxvf clion.tar.gz && \  
rm -fv clion.tar.gz  
  
# System settings  
RUN echo "fs.inotify.max_user_watches = 524288" >> /etc/sysctl.conf  
RUN sysctl -p --system  

