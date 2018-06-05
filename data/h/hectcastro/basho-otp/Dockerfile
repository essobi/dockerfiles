# basho-otp  
#  
# VERSION 0.1.2  
FROM phusion/baseimage:0.9.11  
MAINTAINER Hector Castro hector@basho.com  
  
# Environmental variables  
ENV DEBIAN_FRONTEND noninteractive  
ENV ERLANG_VERSION R16B02_basho5  
  
# Install dependencies  
RUN apt-get -qq update && apt-get install -y \  
git \  
wget \  
libxml2-dev \  
build-essential \  
autoconf \  
libncurses5-dev \  
libssl-dev \  
libpam0g-dev \  
software-properties-common \  
python-software-properties  
RUN apt-add-repository ppa:webupd8team/java -y && apt-get update && \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java7-installer -y  
  
# Install OTP  
ADD https://github.com/basho/otp/archive/OTP_${ERLANG_VERSION}.tar.gz /  
RUN (cd / && tar xzf OTP_${ERLANG_VERSION}.tar.gz)  
RUN (cd /otp-OTP_${ERLANG_VERSION} && sed -i 's/unset ${sys_erl_flags}/#unset
${sys_erl_flags}/' otp_build)  
RUN (cd /otp-OTP_${ERLANG_VERSION} && ./otp_build autoconf && ./configure \  
\--disable-hipe --enable-smp-support --without-odbc --enable-m64-build \  
&& make && make install)  
  
# Enable insecure SSH key  
# See: https://github.com/phusion/baseimage-
docker#using_the_insecure_key_for_one_container_only  
RUN /usr/sbin/enable_insecure_key  
  
# Cleanup  
RUN rm "/OTP_${ERLANG_VERSION}.tar.gz" \  
rm -rf "/otp-OTP_${ERLANG_VERSION}"  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Leverage the baseimage-docker init system  
CMD ["/sbin/my_init", "--quiet"]  

