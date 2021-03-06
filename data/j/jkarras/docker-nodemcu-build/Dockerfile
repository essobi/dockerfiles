FROM ubuntu  
MAINTAINER marcelstoer  
  
# If you want to tinker with this Dockerfile on your machine do as follows:  
# - git clone https://github.com/marcelstoer/docker-nodemcu-build  
# - vim docker-nodemcu-build/Dockerfile  
# - docker build -t docker-nodemcu-build docker-nodemcu-build  
# - cd <nodemcu-firmware>  
# - docker run --rm -ti -v `pwd`:/opt/nodemcu-firmware docker-nodemcu-build  
RUN apt-get update && apt-get install -y --no-install-recommends wget unzip
git mkdocs s3cmd curl && \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash && \  
apt-get install git-lfs && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir /opt/nodemcu-firmware  
WORKDIR /opt/nodemcu-firmware  
  
# Config options you may pass via Docker like so 'docker run -e
"<option>=<value>"':  
# - IMAGE_NAME=<name>, define a static name for your .bin files  
# - INTEGER_ONLY=1, if you want the integer firmware  
# - FLOAT_ONLY=1, if you want the floating point firmware  
#  
# What the commands do:  
# - use the Git branch and the current time stamp to define image name if
IMAGE_NAME not set  
# - unpack esp-open-sdk.tar.gz in a directory that is NOT the bound mount
directory (i.e. inside the Docker image)  
# - remove all files in <firmware-dir>/bin  
# - make a float build if !only-integer  
# - copy and rename the mapfile to bin/  
# - make an integer build  
# - copy and rename the mapfile to bin/  
CMD if [ -z "$IMAGE_NAME" ]; then \  
BRANCH="$(git rev-parse --abbrev-ref HEAD | sed -r 's/[\/\\\\]+/_/g')" && \  
BUILD_DATE="$(date +%Y%m%d-%H%M)" && \  
IMAGE_NAME=${BRANCH}_${BUILD_DATE}; \  
else true; fi && \  
cp tools/esp-open-sdk.tar.* ../ && \  
cd .. && \  
if [ -f ./esp-open-sdk.tar.xz ]; then \  
tar -Jxvf esp-open-sdk.tar.xz; \  
else \  
tar -zxvf esp-open-sdk.tar.gz; \  
fi && \  
export PATH=$PATH:$PWD/esp-open-sdk/sdk:$PWD/esp-open-sdk/xtensa-lx106-elf/bin
&& \  
cd nodemcu-firmware && \  
if [ -z "$INTEGER_ONLY" ]; then \  
(make clean all && \  
cd bin && \  
srec_cat -output nodemcu_float_"${IMAGE_NAME}".bin -binary 0x00000.bin -binary
-fill 0xff 0x00000 0x10000 0x10000.bin -binary -offset 0x10000 && \  
cp ../app/mapfile nodemcu_float_"${IMAGE_NAME}".map && \  
cd ../); \  
else true; fi && \  
if [ -z "$FLOAT_ONLY" ]; then \  
(make EXTRA_CCFLAGS="-DLUA_NUMBER_INTEGRAL" clean all && \  
cd bin && \  
srec_cat -output nodemcu_integer_"${IMAGE_NAME}".bin -binary 0x00000.bin
-binary -fill 0xff 0x00000 0x10000 0x10000.bin -binary -offset 0x10000 && \  
cp ../app/mapfile nodemcu_integer_"${IMAGE_NAME}".map); \  
else true; fi  

