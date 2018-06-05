FROM ubuntu:16.04  
MAINTAINER Montreal Neurological Institute (https://github.com/BIC-MNI)  
  
#Installation of minc-toolkit  
RUN apt-get update && \  
apt-get install -y \  
bzip2 \  
freeglut3 \  
git \  
gcc \  
imagemagick \  
libc6 \  
libexpat1 \  
libgl1 \  
libjpeg62 \  
libstdc++6 \  
libtiff5 \  
libuuid1 \  
libxau6 \  
libxcb1 \  
libxdmcp6 \  
libxext6 \  
libx11-6 \  
make \  
perl \  
sudo \  
wget  
  
RUN apt-get dist-upgrade -y && \  
apt-get install -y software-properties-common && \  
apt-get install -y octave && \  
apt-get install -y rubygems && \  
apt-get remove -y software-properties-common  
  
RUN sudo dpkg --add-architecture amd64 && \  
sudo apt-get update  
  
RUN wget http://packages.bic.mni.mcgill.ca/minc-toolkit/Debian/minc-
toolkit-1.9.15-20170529-Ubuntu_16.04-x86_64.deb -P /tmp  
RUN dpkg -i /tmp/minc-toolkit-1.9.15-20170529-Ubuntu_16.04-x86_64.deb  
RUN rm /tmp/minc-toolkit-1.9.15-20170529-Ubuntu_16.04-x86_64.deb  
  
RUN git clone git://github.com/rbenv/rbenv.git /usr/local/rbenv \  
&& git clone git://github.com/rbenv/ruby-build.git
/usr/local/rbenv/plugins/ruby-build \  
&& git clone git://github.com/jf/rbenv-gemset.git
/usr/local/rbenv/plugins/rbenv-gemset \  
&& /usr/local/rbenv/plugins/ruby-build/install.sh  
ENV PATH /usr/local/rbenv/bin:$PATH  
ENV RBENV_ROOT /usr/local/rbenv  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /etc/profile.d/rbenv.sh \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /etc/profile.d/rbenv.sh \  
&& echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh  
  
RUN echo 'export RBENV_ROOT=/usr/local/rbenv' >> /root/.bashrc \  
&& echo 'export PATH=/usr/local/rbenv/bin:$PATH' >> /root/.bashrc \  
&& echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
  
ENV CONFIGURE_OPTS --disable-install-doc  
ENV PATH /usr/local/rbenv/bin:/usr/local/rbenv/shims:$PATH  
  
RUN eval "$(rbenv init -)"; rbenv install 2.4.2 \  
&& eval "$(rbenv init -)"; rbenv global 2.4.2 \  
&& eval "$(rbenv init -)"; gem update --system \  
&& eval "$(rbenv init -)"; gem install bundler  
  
RUN git clone https://github.com/vfonov/build_average_model.git
/usr/local/build_average_model  
  
ENV RUBYLIB ${RUBYLIB}:/usr/local/build_average_model  
  
#Folder to add the minc files  
RUN mkdir -p /opt/minc/1.9.15/share/icbm152_model_09a  
  
ADD ./mni_icbm152_t1_tal_nlin_sym_09a_mask.mnc
/opt/minc/1.9.15/share/icbm152_model_09a  
  
ADD ./mni_icbm152_t1_tal_nlin_sym_09a.mnc
/opt/minc/1.9.15/share/icbm152_model_09a  
  
ADD ./command-line-script.sh /bin  
  
RUN chmod +x /opt/minc/1.9.15/minc-toolkit-config.sh  
  
RUN /bin/bash -c "source /opt/minc/1.9.15/minc-toolkit-config.sh"  
  
RUN apt-get autoclean && apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#Fix for octave issue  
RUN apt-get remove -y libopenblas-base  

