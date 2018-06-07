FROM debian:jessie  
  
MAINTAINER Correl Roush <correl@gmail.com>  
  
ENV OTP_VERSION 17.5  
ENV REBAR_VERSION 2.5.1  
ENV RELX_VERSION v1.2.0  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update -qq \  
&& apt-get install -y \  
build-essential \  
git \  
libncurses5-dev \  
openssl \  
libssl-dev \  
fop \  
xsltproc \  
unixodbc-dev  
  
ADD http://erlang.org/download/otp_src_${OTP_VERSION}.tar.gz /usr/src/  
RUN cd /usr/src \  
&& tar xf otp_src_${OTP_VERSION}.tar.gz \  
&& cd otp_src_${OTP_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& cd / && rm -rf /usr/src/otp_src_${OTP_VERSION}  
  
ADD https://github.com/rebar/rebar/archive/${REBAR_VERSION}.tar.gz
/usr/src/rebar-${REBAR_VERSION}.tar.gz  
RUN cd /usr/src \  
&& tar zxf rebar-${REBAR_VERSION}.tar.gz \  
&& cd rebar-${REBAR_VERSION} \  
&& make \  
&& cp rebar /usr/bin/rebar \  
&& cd / && rm -rf /usr/src/rebar-${REBAR_VERSION}  
  
ADD https://github.com/erlware/relx/archive/${RELX_VERSION}.tar.gz
/usr/src/relx-${RELX_VERSION}.tar.gz  
RUN cd /usr/src \  
&& tar zxf relx-${RELX_VERSION}.tar.gz \  
&& cd relx-${RELX_VERSION#v} \  
&& make \  
&& cp relx /usr/bin/relx \  
&& cd / && rm -rf /usr/src/relx-${RELX_VERSION#v}  
  
CMD ["erl"]  

