#
===========================================================================================  
# Dockerfile for building AOSP [Android Open Source Project]  
#  
# References:  
# http://source.android.com/source/index.html  
#
===========================================================================================  
  
FROM ubuntu:14.04  
  
ENV GOSU_VERSION=1.10  
  
ENV USER=aosp  
ENV USER_ID_DEFAULT=1000  
ENV GROUP_ID_DEFAULT=1000  
ENV WORKDIR=/aosp  
  
MAINTAINER Sebastian Weisgerber <sweisgerber.dev@gmail.com>  
  
# See https://github.com/docker/docker/issues/4032  
#ENV DEBIAN_FRONTEND noninteractive  
  
# Make sure the package repository is up to date  
RUN sed -i 's/main$/main universe/' /etc/apt/sources.list  
RUN dpkg --add-architecture i386  
RUN apt-get -qq update && apt-get -qqy dist-upgrade  
  
RUN apt-get update && apt-get install -y \  
bison \  
build-essential \  
ca-certificates \  
ccache \  
curl \  
flex \  
git \  
git-core \  
gnupg \  
gperf \  
gcc-multilib \  
g++-multilib \  
lib32ncurses5-dev \  
lib32z-dev \  
libc6-dev-i386 \  
libgl1-mesa-dev \  
libx11-dev \  
libxml2-utils \  
python \  
rsync \  
screen \  
tig \  
unzip \  
x11proto-core-dev \  
xsltproc \  
zip \  
zlib1g-dev  
#  
# Note: To use SELinux tools for policy analysis, also install the python-
networkx package.  
# RUN apt-get -y install python-networkx  
#  
# See https://source.android.com/source/initializing.html  
#  
# The master branch of Android in the Android Open Source Project (AOSP)  
# requires Java 8. On Ubuntu, use OpenJDK.  
# RUN apt-get -y install openjdk-8-jdk  
#  
# To develop older versions of Android, download and install the corresponding
version of the Java JDK:  
#  
# - Java 7: for Lollipop through Marshmallow  
# - Java 6: for Gingerbread through KitKat  
# - Java 5: for Cupcake through Froyo  
#  
RUN apt-get update && apt-get install -y openjdk-7-jdk  
#  
# Update the default Java version - optional  
#  
RUN update-alternatives --config java \  
&& update-alternatives --config javac  
  
# Add "gosu" tool
######################################################################################################  
RUN set -ex; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
gosu nobody true; \  
\  
apt-get purge -y --auto-remove $fetchDeps  
  
# Add "repo" tool
######################################################################################################  
RUN curl https://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo  
RUN chmod a+x /usr/local/bin/repo  
  
# Create a non-root user that will perform the actual build  
RUN id ${USER} 2>/dev/null || useradd --uid ${USER_ID_DEFAULT} --create-home
--shell /bin/bash ${USER}  
RUN echo "${USER} ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers  
  
RUN su -c 'git config --global user.email "user@example.org"' ${USER}  
RUN su -c 'git config --global user.name "User"' ${USER}  
  
COPY config/.bashrc /home/${USER}/.bashrc  
RUN chown ${USER}:${USER} /home/${USER}/.bashrc  
COPY config/entrypoint.sh /usr/local/bin/entrypoint.sh  
  
# EXPOSE
###############################################################################################################  
RUN mkdir "/aosp"  
VOLUME ["/aosp"]  
WORKDIR ${WORKDIR}  
  
#RUN chown ${USER}:${USER} /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
CMD ["/bin/bash"]  

