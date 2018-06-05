FROM sunside/mono:4.3.3.97  
ENV DNX_VERSION 1.0.0-rc2-20222  
ENV DNX_USER_HOME /opt/dnx  
ENV DNX_UNSTABLE_FEED=https://www.myget.org/F/aspnetcidev/api/v2/  
  
# Hack from aspnet-docker  
ENV DNX_RUNTIME_ID debian.8.2-x64  
  
RUN apt-get -qq update && apt-get -qqy install unzip libc6-dev libicu-dev &&
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sSL https://raw.githubusercontent.com/aspnet/Home/dev/dnvminstall.sh
| DNX_USER_HOME=$DNX_USER_HOME DNX_BRANCH=v$DNX_VERSION sh  
RUN bash -c "source $DNX_USER_HOME/dnvm/dnvm.sh \  
&& dnvm install -u $DNX_VERSION -p -alias default \  
&& dnvm alias default | xargs -i ln -s $DNX_USER_HOME/runtimes/{}
$DNX_USER_HOME/runtimes/default"  
  
# Install libuv for Kestrel from source code (binary is not in wheezy and one
in jessie is still too old)  
RUN LIBUV_VERSION=1.4.2 \  
&& apt-get -qq update \  
&& apt-get -qqy install autoconf automake build-essential libtool \  
&& curl -sSL https://github.com/libuv/libuv/archive/v${LIBUV_VERSION}.tar.gz |
tar zxfv - -C /usr/local/src \  
&& cd /usr/local/src/libuv-$LIBUV_VERSION \  
&& sh autogen.sh && ./configure && make && make install \  
&& rm -rf /usr/local/src/libuv-$LIBUV_VERSION \  
&& ldconfig \  
&& apt-get -y purge autoconf automake build-essential libtool \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV PATH $PATH:$DNX_USER_HOME/runtimes/default/bin  
  
# Prevent `dnu restore` from stalling (gh#63, gh#80)  
ENV MONO_THREADS_PER_CPU 50  

