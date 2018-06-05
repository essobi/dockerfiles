FROM monolit/framework  
MAINTAINER Kristoffer Andersen <ka@openmono.com>  
RUN export GCC_DIR="$HOME/gcc-arm-none-eabi-4_8-2014q1" && \  
export GCC_ARCHIVE="$HOME/gcc-arm-none-eabi-4_8-2014q1-20140314-linux.tar.bz2"
&& \  
export GCC_URL="https://launchpad.net/gcc-arm-
embedded/4.8/4.8-2014-q1-update/+download/gcc-arm-none-
eabi-4_8-2014q1-20140314-linux.tar.bz2" && \  
wget $GCC_URL -O $GCC_ARCHIVE; tar xfvj $GCC_ARCHIVE -C $HOME  
RUN apt-get update -qq && apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs  
ENV ARDUINO_URL "https://github.com/getopenmono/arduino_comp.git"  
ENV MONOPROG_RELEASE 0.9.3.1  
ENV MONOPROG_MAC_URL
"https://github.com/getopenmono/arduino_comp/releases/download/1.7.0/monoprog0.9.3.1.tar.bz2"  
ENV MONOPROG_WIN_URL
"https://github.com/getopenmono/arduino_comp/releases/download/1.7.0/monoprog_win0.9.3.1.tar.bz2"  
ENV ARDUINO_BRANCH master  
ENV FRAMEWORK_BRANCH production  
ENV MONOPROG_BRANCH master  
ENV FRM_RELEASE_TYPE release  
CMD export PATH=$PATH:$HOME/gcc-arm-none-eabi-4_8-2014q1/bin && \  
if [ $TRAVIS_BRANCH ]; then ARDUINO_BRANCH=$TRAVIS_BRANCH; fi && \  
echo "Using branch: $ARDUINO_BRANCH" && \  
git clone -b $ARDUINO_BRANCH $ARDUINO_URL && \  
cd arduino_comp && \  
if [ $TRAVIS_COMMIT ]; then echo "Using commit: $TRAVIS_COMMIT"; git checkout
-qf $TRAVIS_COMMIT; fi && \  
bash build_release.sh $RELEASE_VERSION

