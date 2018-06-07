  
FROM fedora:28  
MAINTAINER Denis Arnaud <denis.arnaud_fedora@m4x.org>  
  
# Maintainer details (full name and email address)  
ARG full_name="Fedora Packager"  
ARG email_address="fedora.packager@fedoraproject.org"  
#  
ENV HOME /home/build  
ENV FULL_NAME $full_name  
ENV EMAIL_ADDRESS $email_address  
  
# Update of the OS  
RUN dnf -y clean all  
RUN dnf -y update || echo "Issue with RPM DB, that's fine"  
  
# Basic, convenient  
RUN dnf -y install less htop net-tools which sudo keychain man || echo "Issue
with installing less. That's fine"  
ADD resources/bashrc /root/  
RUN cat /root/bashrc >> /root/.bashrc && rm -f /root/bashrc  
  
# Fedora/CentOS/RedHat packaging  
RUN dnf -y install fedora-packager keyutils rpmconf dnf-utils git-all bash-
completion Lmod || echo "Issue with installing fedora-packager. That's fine"  
  
# Specific to C++-based packages (with Python bindings)  
RUN dnf -y install gcc-c++ boost-devel cmake python-devel python3-devel
bzip2-devel m4 python3-numpy mpich-devel openmpi-devel || echo "Issue with
installing boost-devel. That's fine"  
  
# Documentation tools  
RUN dnf -y install "tex(latex)" || echo "Issue with installing Latex. That's
fine"  
RUN dnf -y install doxygen ghostscript || echo "Issue with installing
documentation tools. That's fine"  
  
# SOCI, ZeroMQ  
RUN dnf -y install zeromq-devel czmq-devel soci-mysql-devel soci-sqlite3-devel
readline-devel || echo "Issue with installing zeromq. That's fine"  
  
# Create the 'build' user (for the package maintainer)  
RUN adduser -m -G mock build  
RUN echo "build ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/build && \  
chmod 0440 /etc/sudoers.d/build  
# Copy the SSH keys  
RUN mkdir -p $HOME/.ssh && chmod 700 $HOME/.ssh  
RUN ssh-keyscan pkgs.fedoraproject.org > $HOME/.ssh/known_hosts  
ADD resources/ssh-config $HOME/.ssh/config  
RUN chmod 600 $HOME/.ssh/config $HOME/.ssh/known_hosts  
  
# Set up the packaging environment  
ADD resources/rpmmacros resources/bashrc resources/gitconfig $HOME/  
RUN cat $HOME/bashrc >> $HOME/.bashrc && rm -f $HOME/bashrc && \  
chown -R build.build $HOME  
RUN echo "[user]" > $HOME/.gitconfig && \  
echo " name = $FULL_NAME" >> $HOME/.gitconfig && \  
echo " email = $EMAIL_ADDRESS" >> $HOME/.gitconfig && \  
cat $HOME/gitconfig >> $HOME/.gitconfig && rm -f $HOME/gitconfig && \  
chown -R build.build $HOME  
RUN echo "%packager $FULL_NAME $EMAIL_ADDRESS" > $HOME/.rpmmacros && \  
echo "%_gpg_name $FULL_NAME $EMAIL_ADDRESS" >> $HOME/.rpmmacros && \  
cat $HOME/rpmmacros >> $HOME/.rpmmacros && rm -f $HOME/rpmmacros && \  
chown -R build.build $HOME  
  
# Switch to the 'build' user  
WORKDIR $HOME  
  
USER build  
RUN rpmdev-setuptree  
  
# Check out the Fedora review helper project  
RUN mkdir -p $HOME/dev/fedora_packaging  
WORKDIR $HOME/dev  
RUN git clone https://github.com/fedorapackaging/fedorareviews.git  
WORKDIR $HOME/dev/fedora_packaging  
  
# Entry point  
CMD ["/bin/bash"]  
  

