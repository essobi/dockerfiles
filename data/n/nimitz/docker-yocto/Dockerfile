FROM ubuntu:16.04  
# Some environment variables  
ENV TERM=linux  
ENV LC_ALL=en_US.utf-8  
ENV DOCKER_USER_NAME=worker  
ENV DOCKER_WORK_DIR=/home/${DOCKER_USER_NAME}/work  
ENV DOCKER_BUILD_DIR=build  
ENV DOCKER_UID=1000  
ENV DOCKER_YOCTO_VERSION=0.5.1  
# Update the systeam and install packages we need for smooth Yocto builds  
RUN apt-get update && apt-get -y upgrade && \  
apt-get install -y \  
build-essential chrpath curl diffstat \  
gcc-multilib gawk git-core libsdl1.2-dev \  
texinfo unzip wget python3 cpio nano tree \  
bzip2 dosfstools mtools parted syslinux sudo  
  
# Install Google's "repo" tool and make it executable  
RUN curl http://storage.googleapis.com/git-repo-downloads/repo >
/usr/local/bin/repo  
RUN chmod +x /usr/local/bin/repo  
  
# Create a non-root user we can use for build*.  
# Let user be in sudoers list  
# (*) Idealy it should fit host machne user Id.  
# So you can pass user ID via cmd line and make it on-flight in container  
RUN id ${DOCKER_USER_NAME} 2>/dev/null || \  
useradd --uid ${DOCKER_UID} \--create-home ${DOCKER_USER_NAME} && \  
echo "${DOCKER_USER_NAME} ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers  
  
# Fix error "Please use a locale setting which supports utf-8."  
# See https://wiki.yoctoproject.org/wiki/TipsAndTricks/ResolvingLocaleIssues  
RUN apt -y install locales && \  
dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8  
  
# Here is a small helper for build automation  
COPY ./docker_build_helper.sh /usr/bin/build_helper.sh  
  
# Switch to actual user and finalize  
USER ${DOCKER_USER_NAME}  
RUN sudo mkdir -p ${DOCKER_WORK_DIR} && \  
sudo chown -R $(id -u):$(id -g) ${DOCKER_WORK_DIR}  
  
WORKDIR /home/${DOCKER_USER_NAME}  
  
# Do initial git configuration in order to prevent repo fails  
RUN git config --global user.name "John Doe" && \  
git config --global user.email "jd@umbrellacorp.com" && \  
git config --global color.ui false  
  
USER root  
  
ENTRYPOINT ["build_helper.sh"]  
CMD ["entry"]  
  
# EOF  

