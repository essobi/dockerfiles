# ninjaben/rtb-support  
#  
# Create an image with enough dependencies to support a mounted-in Matlab and
calling Docker from Matlab.  
#  
# This includes the ability to let Matlab launch Docker containers. This works
by building the Docker  
# executable into this image, and then mounting in the port to the Docker
daemon running on the Docker host.  
# Thaks to Jérôme Petazzoni for advice on this style of launching "peer"
containers in Docker  
# https://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/  
#  
# Here's an example that runs Matlab in the container, then launches a Docker
container from Matlab:  
#  
# docker run \  
# --rm \  
# -v "/usr/local/MATLAB/R2016a":/usr/local/MATLAB/from-host \  
# -v /var/run/docker.sock:/var/run/docker.sock \  
# --net="host" \  
# -e "COMMAND=system('docker run hello-world')" \  
# ninjaben/rtb-support"  
#  
# This also includes the ability to read and write data in AWS S3 buckets.
This works through the "aws s3 cp"  
# command. The input and output scratch folders and S3 buckets can be
specified with "-e". Here's an example  
# that would copy all the input files to the output:  
#  
# docker run \  
# --rm \  
# -v "/usr/local/MATLAB/R2016a":/usr/local/MATLAB/from-host \  
# -v /var/run/docker.sock:/var/run/docker.sock \  
# --net="host" \  
# -e "INPUT_SCRATCH=/test/input-scratch" \  
# -e "INPUT_BUCKET=s3://my-input-bucket" \  
# -e "OUTPUT_SCRATCH=/test/output-scratch" \  
# -e "OUTPUT_BUCKET=s3://my-output-bucket" \  
# -e "COMMAND=system('cp -r /test/input-scratch/* /test/output-scratch/)" \  
# ninjaben/rtb-support  
FROM ninjaben/matlab-support  
  
MAINTAINER Ben Heasly <benjamin.heasly@gmail.com>  
  
# general dependencies  
RUN apt-get update && apt-get install -y \  
git \  
docker.io \  
libboost-all-dev \  
openexr \  
cmake \  
pkg-config  
  
# Assimp  
WORKDIR /assimp  
RUN git clone https://github.com/assimp/assimp.git  
WORKDIR /assimp/assimp  
RUN git checkout v3.3.1  
RUN cmake CMakeLists.txt -G 'Unix Makefiles' && make && make install &&
ldconfig  
  
# yas3fs  
RUN apt-get install -y \  
fuse \  
python-pip  
RUN pip install yas3fs  
RUN sed -i'' 's/^# *user_allow_other/user_allow_other/' /etc/fuse.conf  
RUN chmod a+r /etc/fuse.conf  
  
# awscli  
RUN apt-get install -y python-pip  
RUN pip install awscli  
  
# job helper  
WORKDIR /rtb  
COPY rtb-job.sh /rtb/  
ENTRYPOINT ["/rtb/rtb-job.sh"]  
  

