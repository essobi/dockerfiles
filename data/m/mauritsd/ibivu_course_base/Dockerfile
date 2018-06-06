FROM debian:jessie  
MAINTAINER "Maurits Dijkstra" <m.j.j.dijkstra@vu.nl>  
  
# Environment variables.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages.  
RUN apt-get update && apt-get -y install \  
openssh-server \  
locales \  
sudo \  
nano \  
shellinabox  
  
# Add startup scripts and make them executable.  
ADD run.sh /run.sh  
ADD copy_workspace.sh /copy_workspace.sh  
ADD run_sshd.sh /run_sshd.sh  
  
# Add shellinabox configuration  
ADD shellinabox_default /etc/default/shellinabox  
  
RUN chmod +x /*.sh  
  
# Add workspace template dir.  
COPY /workspace_template /workspace_template  
  
# Setup sshd and modify its default config.  
RUN mkdir -p /var/run/sshd \  
&& sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config \  
&& true  
  
# Configure timezone and locale  
RUN echo "Europe/Amsterdam" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
sed -i -e 's/# nl_NL.UTF-8 UTF-8/nl_NL.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
# Add a user for the student, with a home directory and a group.  
RUN useradd student -d /workspace \  
&& echo "student:student" | chpasswd \  
&& chsh -s /bin/bash student \  
&& mkdir /workspace \  
&& chown -R student:student /workspace \  
&& addgroup student sudo \  
&& true  
  
# Tell Docker that we're exposing a service on port 22 and 4200.  
EXPOSE 22  
EXPOSE 4200  
# Start the init script once the container is initialized.  
ENTRYPOINT ["/run.sh"]  

