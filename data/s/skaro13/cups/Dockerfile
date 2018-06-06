FROM debian:testing-slim  
  
COPY run.sh /  
RUN chmod +x run.sh  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
RUN apt-get update \  
&& apt-get install -y \  
sudo \  
dbus \  
avahi-daemon \  
whois \  
cups \  
cups-client \  
cups-bsd \  
printer-driver-all \  
hpijs-ppds \  
hp-ppd \  
hplip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /defaults && cp -r /etc/cups/* /defaults/ && rm -r /etc/cups  
RUN ln -s /config /etc/cups  
  
RUN useradd \  
\--groups=sudo,lp,lpadmin \  
\--shell=/bin/bash \  
\--password=$(mkpasswd print) \  
print \  
&& sed -i '/%sudo[[:space:]]/ s/ALL[[:space:]]*$/NOPASSWD:ALL/' /etc/sudoers  
  
VOLUME /config  
EXPOSE 631  
CMD ["/run.sh"]  

