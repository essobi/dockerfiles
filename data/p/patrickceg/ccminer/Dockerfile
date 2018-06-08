# The official install talks about Fedora packages, so let's see  
# if Centos is close enough...  
FROM nvidia/cuda:9.0-devel-centos7  
  
# We will need Git to pull the repo  
RUN yum -y -q install git  
  
# The packages mentioned in the INSTALL phase, except:  
# jansson-devel - We're going to build our own since the version 2.4.x doesn't
have json_array_foreach  
# make - Added it because Centos doesn't have it even after getting
autoconf/automake  
RUN yum -y -q install gcc gcc-c++ make wget autoconf automake install openssl-
devel libcurl-devel zlib-devel  
  
# Create a user to do the build  
ENV BUILD_FOLDER=/minerbuild  
ENV APP_FOLDER=/app  
ENV APP_USER=minerbuilder  
ENV CCMINER_VERSION=2.2.4-tpruvot  
  
RUN adduser $APP_USER && \  
mkdir $BUILD_FOLDER && \  
chown $APP_USER.users $BUILD_FOLDER  
  
# We'll build jansson as regular user  
USER $APP_USER  
  
# Download jansson and verify signature (since we're downloading over HTTP)  
RUN cd $BUILD_FOLDER && \  
wget http://www.digip.org/jansson/releases/jansson-2.10.tar.gz && \  
gpg --keyserver pgp.mit.edu --recv-keys D058434C && \  
wget http://www.digip.org/jansson/releases/jansson-2.10.tar.gz.asc && \  
gpg --verify jansson-2.10.tar.gz.asc jansson-2.10.tar.gz  
  
# Extract jasson  
RUN cd $BUILD_FOLDER && \  
tar -xvf jansson-2.10.tar.gz && \  
rm jansson-2.10.tar.gz && \  
rm jansson-2.10.tar.gz.asc  
  
# Build Jansson  
RUN cd $BUILD_FOLDER/jansson-2.10 && \  
./configure && \  
make && \  
make check  
  
# Install Jansson (need root for this)  
USER root  
RUN cd $BUILD_FOLDER/jansson-2.10 && \  
make install  
  
# Now switch to the builder and check out the git repo  
USER $APP_USER  
  
# Clone from the git repo  
RUN cd $BUILD_FOLDER && \  
git clone https://github.com/tpruvot/ccminer.git --branch $CCMINER_VERSION
\--single-branch  
  
ENV CCMINER_FOLDER=$BUILD_FOLDER/ccminer  
  
# Uncomment all the architectures  
ENV CCMINER_FOLDER=$BUILD_FOLDER/ccminer  
  
# Replace uncomment all the old architectures  
RUN cd $CCMINER_FOLDER && \  
sed \  
-e 's/#nvcc_ARCH += -gencode=arch=compute_61/nvcc_ARCH += -gencode=arch=compute_61/' \  
-e 's/#nvcc_ARCH += -gencode=arch=compute_35/nvcc_ARCH += -gencode=arch=compute_35/' \  
-e 's/#nvcc_ARCH += -gencode=arch=compute_30/nvcc_ARCH += -gencode=arch=compute_30/' \  
Makefile.am > Makefile2.am  
RUN cd $CCMINER_FOLDER && \  
cp Makefile2.am Makefile.am && \  
rm Makefile2.am  
  
# RUN cd $CCMINER_FOLDER && \  
# cat Makefile.am  
# Run the build  
RUN cd $CCMINER_FOLDER && \  
./build.sh  
  
# Run the build  
RUN cd $CCMINER_FOLDER && \  
./build.sh  
  
# Copy the ccminer binary to a /app folder  
USER root  
  
RUN mkdir $APP_FOLDER && \  
chown $APP_USER.users $APP_FOLDER && \  
cp $CCMINER_FOLDER/ccminer $APP_FOLDER  
  
# Switch to a multistage build with the runtime image  
FROM nvidia/cuda:9.0-runtime-centos7  
  
# Redefine the app user and folder - note app folder must be the same as the
first stage  
ENV APP_FOLDER=/app  
ENV APP_USER=miner  
  
# Copy the stuff that we built  
COPY \--from=0 $APP_FOLDER $APP_FOLDER  
COPY \--from=0 /usr/local/lib /usr/local/lib  
  
# Get the non-devel versions of the libraries that we need  
RUN yum -y -q install openssl libcurl zlib libgomp && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
# Load the Jansson library that's now built  
RUN echo /usr/local/lib > /etc/ld.so.conf.d/userlocal.conf && \  
ldconfig  
  
# Symlink the app to /usr/local/bin  
RUN ln -s $APP_FOLDER/ccminer /usr/local/bin/ccminer && \  
chown -R root.root $APP_FOLDER  
  
# Recreate and switch to the app user for this build  
RUN adduser $APP_USER  
USER $APP_USER  
  
CMD [ ccminer ]  

