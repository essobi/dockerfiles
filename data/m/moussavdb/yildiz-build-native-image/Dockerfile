FROM moussavdb/yildiz-build-image  
  
LABEL maintainer="Grégory Van den Borre vandenborre.gregory@hotmail.fr"  
  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
RUN apt-get install -y -q build-essential mingw-w64 cmake unzip python3
libxaw7-dev  
COPY build-wrapper-linux-x86.zip /home/build-wrapper-linux-x86.zip  
RUN unzip /home/build-wrapper-linux-x86.zip -d /home  
RUN cp /home/build-wrapper-linux-x86/* /usr/local/bin  
RUN rm -R /home/build-wrapper-linux-x86  
RUN apt-get purge -y -q unzip  

