FROM ubuntu:14.04  
MAINTAINER Frank Lemanschik @ DirektSPEED Europe <frank@dspeed.eu>  
# Adding new ubuntu 14.04 Mirror sources to speed the things up  
RUN rm -rf /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted
universe multiverse" > /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main
restricted universe multiverse" >> /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main
restricted universe multiverse" >> /etc/apt/sources.list  
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main
restricted universe multiverse" >> /etc/apt/sources.list  
# Update APT Source  
RUN apt-get -y update #makesure  
RUN apt-get install -y --no-install-recommends docker.io git make  
RUN git clone git://github.com/docker/docker  
# TODO: Make it auto Create the File  
#RUN wget https://raw.githubusercontent.com/DirektSPEED/docker-nightly-
build/master/run  
# Make Symbolic link to Ubuntu Docker Package  
RUN ln -s /usr/bin/docker.io /usr/bin/docker  
# Make build & upload script execute able  
# TODO: Rename to /build-binary --upload ftp://user:pass@host.tld
git://user:pass@github.com/username/repo s3://username:pass  
#RUN chmod +x /run.1  
# Clean up apt-get to save some space.  
RUN apt-get -y clean  
CMD cd /docker && \  
git fetch origin && \  
git reset --hard origin/master && \  
make cross  
  
#/build-binary --upload ftp://user:pass@host.tld
git://user:pass@github.com/username/repo s3://username:pass  
# Self Update  
#rm -rf run.1  
#wget https://raw.githubusercontent.com/DirektSPEED/docker-nightly-
build/master/run  
#chmod +x /run.1  
#ln -s /run.1 /build-binary  
#TODO: Check if /var/run/docker.sock exists else  
#echo "The Docker Socket needs to be bound to /var/run/docker.sock else this
don't works!"  
#cd /docker  
#git pull origin master  
#make -C /docker binary  
#echo For Copyring the created docker execute able to the host simply run
this: \n  
#echo docker run --name=build-docker-nightly -v
/var/run/docker.sock:/var/run/docker.sock dspeed/docker-nightly-build /run.1
\n  
#ls -ao /docker/bundels/  
#echo docker cp build-docker-nightly docker cp build-docker-
nightly:/docker/bundles/docker /usr/bin/docker.nightly  
#echo rm -rf /usr/bin/docker  
#echo ln -s /usr/bin/docker.nightly /usr/bin/docker  
#echo "The Docker Socket needs to be bound to /var/run/docker.sock else this
don't works!"  
# Now Uploading the Result to AMAZON S3 Via CURL  

