FROM centos:7  
#copy tools  
RUN mkdir -p /opt/tools /root/.android  
COPY tools /opt/tools  
COPY config /root/.android  
  
#keystore args  
ARG KS_ALIAS=androiddebug  
ARG KS_NAME=AG  
ARG KS_UNIT=AeroGear  
ARG KS_ORG=RedHat  
ARG KS_LOC=Waterford  
ARG KS_STATE=WD  
ARG KS_COUNTRY=IRL  
ARG KS_PATH=/etc/digger  
ARG KS_STOREPASS=android  
ARG KS_KEYPASS=android  
  
#gradle cache folder  
RUN mkdir /gradle-cache  
  
#env vars  
ENV GRADLE_USER_HOME=/gradle-cache  
ENV AG_MOBILE_SDK /opt/mobile-sdk  
ENV JAVA_HOME /etc/alternatives/java_sdk_1.8.0  
ENV ANDROID_HOME ${AG_MOBILE_SDK}  
ENV AG_KEYSTORE_PATH ${KS_PATH}/debug.keystore  
ENV AG_KEYSTORE_KEYPASS ${KS_KEYPASS}  
ENV AG_KEYSTORE_STOREPASS ${KS_STOREPASS}  
ENV AG_KEYSTORE_ALIAS ${KS_ALIAS}  
  
RUN yum install -y \  
wget \  
tar \  
unzip \  
zlib.i686 \  
ncurses-libs.i686 \  
bzip2-libs.i686 \  
epel-release \  
openssh-clients \  
git \  
gcc-c++ \  
make \  
java-1.8.0-openjdk-devel \  
java-1.8.0-openjdk \  
ant  
  
#Install Python 3.4  
RUN yum install -y python34  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python3.4 /get-pip.py  
RUN rm /get-pip.py  
  
# install node 4.x  
RUN curl --silent --location https://rpm.nodesource.com/setup_4.x | bash -  
RUN yum -y install nodejs  
  
# install Cordova CLI  
RUN npm install -g cordova@6  
  
#install cli  
RUN /opt/tools/install-cli  
  
#configure sdk volume  
RUN mkdir -p /opt/mobile-sdk  
VOLUME /opt/mobile-sdk  
  
#android tools  
ENV PATH ${PATH}:${AG_MOBILE_SDK}/tools  
  
#default keystore  
RUN mkdir -p /etc/digger  
RUN /opt/tools/gen-keystore ${KS_ALIAS} ${KS_NAME} ${KS_UNIT} ${KS_ORG}
${KS_LOC} ${KS_STATE} ${KS_COUNTRY} ${KS_PATH} ${KS_STOREPASS} ${KS_KEYPASS}  
  
ENTRYPOINT ["abcd"]  
CMD ["--help"]  
  

