FROM ubuntu:14.10  
RUN apt-get update -qq \  
&& apt-get install -y \  
build-essential \  
git \  
libncurses5-dev \  
openssl \  
libssl-dev \  
fop \  
xsltproc \  
unixodbc-dev  
  
ENV OTP_VERSION 17.3  
ENV REBAR_VERSION 2.5.1  
ADD http://erlang.org/download/otp_src_${OTP_VERSION}.tar.gz /usr/src/  
RUN cd /usr/src \  
&& tar xf otp_src_${OTP_VERSION}.tar.gz \  
&& cd otp_src_${OTP_VERSION} \  
&& ./configure \  
&& make \  
&& make install  
  
ADD https://github.com/rebar/rebar/archive/${REBAR_VERSION}.tar.gz
/usr/src/rebar-${REBAR_VERSION}.tar.gz  
RUN cd /usr/src \  
&& tar zxf rebar-${REBAR_VERSION}.tar.gz \  
&& cd rebar-${REBAR_VERSION} \  
&& make \  
&& cp rebar /usr/bin/rebar  

