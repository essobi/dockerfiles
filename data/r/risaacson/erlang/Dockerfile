FROM centos:7  
MAINTAINER Richard Isaacson <richard.c.isaacson@gmail.com>  
  
COPY i18n /etc/sysconfig/  
  
RUN echo 'LANG="en_US.utf8"' >> /etc/profile \  
&& echo "export LANG" >> /etc/profile \  
&& yum install -y \  
gcc \  
glibc-devel \  
make \  
ncurses-devel \  
openssl-devel \  
autoconf \  
git \  
&& yum clean all  
  
ENV OTP_VERSION 18.1  
ADD http://erlang.org/download/otp_src_${OTP_VERSION}.tar.gz /usr/src/  
  
RUN cd /usr/src \  
&& tar xf otp_src_${OTP_VERSION}.tar.gz \  
&& cd otp_src_${OTP_VERSION} \  
&& ./configure \  
&& LANG="en_US.UTF-8" make \  
&& make install \  
&& cd / && rm -rf /usr/src/otp_src_${OTP_VERSION}
/usr/src/otp_src_${OTP_VERSION}.tar.gz  
  
CMD ["erl"]  

