# Pull the Ubuntu CUDA development image  
FROM nvidia/cuda:9.0-devel-ubuntu16.04  
  
# Update repos  
RUN apt-get -qq update  
  
# We will need Git to pull the repo  
RUN apt-get -qq -y install --no-install-recommends git  
  
# The packages mentioned in the INSTALL phase, plus gcc-5 and g++-5  
RUN apt-get -qq -y install --no-install-recommends ca-certificates
libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-
essential gcc-5 g++-5  
  
# Create a user to do the build  
ENV BUILD_FOLDER=/minerbuild  
ENV APP_FOLDER=/app  
ENV APP_USER=minerbuilder  
ENV REPO_BRANCH=cuda-9  
ENV REPO_URL=https://github.com/tpruvot/ccminer.git  
  
RUN adduser $APP_USER && \  
mkdir $BUILD_FOLDER && \  
chown $APP_USER.users $BUILD_FOLDER  
# Now switch to the builder and check out the git repo  
USER $APP_USER  
# Clone from the git repo  
RUN cd $BUILD_FOLDER && \  
git clone $REPO_URL \--branch $REPO_BRANCH \--single-branch  
  
# Run the build  
RUN cd $BUILD_FOLDER/ccminer && \  
./build.sh  
  
# Copy the ccminer binary to a /app folder  
USER root  
  
RUN mkdir $APP_FOLDER && \  
chown $APP_USER.users $APP_FOLDER && \  
cp $BUILD_FOLDER/ccminer/ccminer $APP_FOLDER  
# Switch to a multistage build with the runtime image  
FROM nvidia/cuda:9.0-runtime-ubuntu16.04  
  
# Redefine the app user and folder - note app folder must be the same as the
first stage  
ENV APP_FOLDER=/app  
ENV APP_USER=miner  
  
# Copy the stuff that we built  
COPY \--from=0 $APP_FOLDER $APP_FOLDER  
COPY \--from=0 /usr/local/lib /usr/local/lib  
  
# Get the non-devel versions of the libraries that we need  
RUN apt-get -qq update && \  
apt-get -qq -y install --no-install-recommends libcurl3 libgomp1 libjansson4
&& \  
apt-get clean autoclean && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
# Symlink the app to /usr/local/bin  
RUN ln -s $APP_FOLDER/ccminer /usr/local/bin/ccminer && \  
chown -R root.root $APP_FOLDER  
# Recreate and switch to the app user for this build  
RUN adduser $APP_USER  
USER $APP_USER  
# Set the entrypoint for all comsole connections  
ENTRYPOINT ["ccminer"]  
  
# Set the default command  
CMD [ "-h" ]  

