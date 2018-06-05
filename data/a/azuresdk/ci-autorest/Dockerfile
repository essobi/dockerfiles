FROM ubuntu:14.04  
# Install base prerequisites  
RUN apt-get update && \  
apt-get -qqy install \  
curl \  
wget \  
unzip \  
git  
  
# Install DNX prerequisites  
RUN apt-get -qqy install \  
libunwind8 \  
gettext \  
libssl-dev \  
libcurl4-gnutls-dev \  
zlib1g \  
libicu-dev \  
uuid-dev  
  
# Install Java and Node prerequisites  
RUN apt-get -qqy install \  
openjdk-7-jre-headless \  
libc6-i386 \  
lib32stdc++6 \  
lib32gcc1 \  
lib32ncurses5 \  
lib32z1 \  
nodejs \  
npm \  
python-pip \  
libgmp-dev \  
python3-pip  
  
# Install RVM  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 \  
&& curl -sSL https://get.rvm.io | bash -s stable --ruby && echo 'source
/etc/profile.d/rvm.sh' >> ~/.bashrc  
  
# Install Mono  
# We can't just use the default mono image because that's based on Debian.  
RUN apt-get update \  
&& apt-get install -y curl \  
&& rm -rf /var/lib/apt/lists/*  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF  
RUN echo "deb http://download.mono-project.com/repo/debian wheezy main" >
/etc/apt/sources.list.d/mono-xamarin.list \  
&& apt-get update \  
&& apt-get install -y mono-devel ca-certificates-mono fsharp mono-vbnc nuget \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Android  
ENV ANDROID_USER_HOME /.android  
ENV ANDROID_HOME $ANDROID_USER_HOME/android-sdk-linux  
ENV ANDROID_VERSION 23.0.2  
RUN mkdir $ANDROID_USER_HOME \  
&& wget -qO- "http://dl.google.com/android/android-sdk_r$ANDROID_VERSION-
linux.tgz" | tar -zxv -C $ANDROID_USER_HOME \  
&& echo y | $ANDROID_USER_HOME/android-sdk-linux/tools/android update sdk
--all --filter platform-tools,android-23,build-tools-23.0.1,extra-android-
support,extra-android-m2repository,extra-google-m2repository --no-ui --force  
  
# Install DNVM  
ENV DNX_VERSION 1.0.0-rc1-final  
ENV DNX_USER_HOME /opt/dnx  
RUN curl -sSL https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh
| DNX_USER_HOME=$DNX_USER_HOME DNX_BRANCH=v$DNX_VERSION sh  
RUN bash -c "source $DNX_USER_HOME/dnvm/dnvm.sh \  
&& dnvm install $DNX_VERSION -r coreclr -alias default \  
&& dnvm alias default | xargs -i ln -s $DNX_USER_HOME/runtimes/{}
$DNX_USER_HOME/runtimes/default"  
  
# Set PATH variable  
ENV PATH
$PATH:$DNX_USER_HOME/runtimes/default/bin:/usr/local/rvm/scripts:~/.local/bin  
  
# Configure GULP  
RUN ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g gulp  

