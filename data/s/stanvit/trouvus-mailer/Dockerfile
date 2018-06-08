FROM ubuntu:16.04  
MAINTAINER Stanislav Vitkovskiy <stas.vitkovsky@gmail.com>  
  
# Don't consider sources and choose the fastest mirrors  
RUN sed -i 's|^deb-src |# deb-src |' /etc/apt/sources.list && \  
sed -i 's|^deb \S\\+ |deb mirror://mirrors.ubuntu.com/mirrors.txt |'
/etc/apt/sources.list  
  
# Install Exim4  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
exim4-daemon-light && \  
mkfifo /var/log/exim4/mainlog /var/log/exim4/paniclog && \  
chmod 0666 /var/log/exim4/mainlog /var/log/exim4/paniclog && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY exim4.conf /etc/exim4/exim4.conf  
COPY entrypoint /bin/entrypoint  
  
ENV EXIM_SMTP_BANNER="Docker SMTP Relay" \  
EXIM_ALLOWED_NETS=":127.0.0.1"  
ENTRYPOINT ["/bin/entrypoint"]  
CMD ["-bdf", "-q5m"]  

