## BUILD: docker build --no-cache -f Dockerfile -t mctdhb-user .  
## RUN MCTDHB through docker: docker run --hostname mctdhb-user --rm -it -v
$(pwd):/base mctdhb-user  
## RESTART: sudo service docker restart  
## ADD DNS to sudo vim /etc/default/docker  
## DOCKER_OPTS="--dns 141.xx.x.x --dns 8.8.8.8 --dns 8.8.4.4"  
##rm all images ..  
## sudo docker ps -a | awk '{print $1}' | grep -v CONTAINER | xargs sudo
docker rmi  
## sudo docker images | grep "<none>" | awk '{print $3}' | xargs sudo docker
rmi  
## sudo vim /etc/resolv.conf and put:  
## nameserver 141.xx.x.x  
## nameserver 8.8.8.8  
## nameserver 8.8.4.4  
# apt-get install make  
# apt-get install openmpi-bin libopenmpi-dev  
# apt-get install fftw3 fftw3-dev  
# apt-get install libblas-dev liblapack-dev  
#FROM ubuntu:16.04  
#MAINTAINER Alexej I. Streltsov <u128str@gmail.com>  
#RUN apt-get update && apt-get install -y vim make openmpi-bin libopenmpi-dev
fftw3 fftw3-dev libblas-dev liblapack-dev  
# Version: 0.1.0  
FROM mctdhb/minunix:latest  
MAINTAINER Alexej I. Streltsov <u128str@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y wget unzip autoconf sudo curl  
  
#RUN adduser user && \  
# echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && \  
# chmod 0440 /etc/sudoers.d/user  
#RUN useradd -ms /bin/bash user  
RUN useradd --create-home --shell /bin/bash user  
  
#Here I copy hi-script printing basic help for user  
COPY ./inst_run_bash/hi /tmp/hi  
RUN su - user  -c "cd && \  
cp /tmp/hi . &&\  
chmod +x ./hi"  
RUN su - user  -c "cd && \  
wget --no-check-certificate --content-disposition
https://github.com/u128str/MCTDHB/archive/master.zip && \  
unzip MCTDHB-master.zip && \  
cd MCTDHB-master &&\  
ls -ltr &&\  
make mk_file=Ubuntu_gnu.mk &&\  
mkdir ../TEST &&\  
cp -rf Templates/PRA_86_063606_Table_1 ../TEST/. "  
#CMD ["su", "-", "user", "-s","/bin/bash", "-c", "/bin/bash"]  
ENV HOME /home/user  
USER  user  
ENTRYPOINT cd; /home/user/hi; /bin/bash  

