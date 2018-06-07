FROM alpine:3.6  
  
ENV OTP_VERSION 20.0  
  
RUN apk add --no-cache ncurses \  
&& apk add --virtual build-deps --no-cache build-base ncurses-dev openssl-dev
perl \  
&& wget http://erlang.org/download/otp_src_${OTP_VERSION}.tar.gz \  
&& tar xf otp_src_${OTP_VERSION}.tar.gz \  
&& cd otp_src_${OTP_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -r otp_src_${OTP_VERSION}* \  
&& apk del build-deps  

