FROM maven:3.3.9  
RUN dpkg --add-architecture i386 && apt-get update  
RUN apt-get install -y zlib1g:i386 libncurses5: libbz2-1.0:i386  
ADD upload-to-bitbucket.sh .  
RUN chmod 755 upload-to-bitbucket.sh

