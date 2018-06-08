FROM madlymad/android-ndk:14b  
# How to use  
# In order to use it, you need to run it with:  
# docker run -v <path to your source>:/src madlymad/android-osmo <file to run>  
# The command above mounts your directory to where the container expects the
source to be and builds it.  
# Install dependencies  
RUN apt-get -qq update && \  
apt-get -qqy install --no-install-recommends \  
gawk \  
bc \  
make \  
git \  
&&\  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "count=0" > ~/.android/repositories.cfg  
  
ENV GRADLE_USER_HOME="${GRADLE_HOME}"  

