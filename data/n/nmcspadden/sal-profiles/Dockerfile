FROM macadmins/sal  
  
MAINTAINER Nick McSpadden <nmcspadden@gmail.com>  
  
ENV PROFILE_PATH /home/docker/profiles  
  
ADD https://github.com/nmcspadden/SalProfileGenerator/tarball/master
/home/docker/master.tar.gz  
RUN mkdir -p $PROFILE_PATH && mkdir -p /usr/local/salprofilegenerator/ && tar
-zxvf /home/docker/master.tar.gz --strip-components=1 -C
/usr/local/salprofilegenerator/ && rm /home/docker/master.tar.gz  

