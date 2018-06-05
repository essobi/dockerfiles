# Debian Stretch docker build with En Australia and En US locales  
FROM debian:stretch  
  
# Space separated list of first part encoding type in /etc/locale.gen.  
# Locale should be in format: < locale_name.encoding >.  
ENV LOCALES_DEF en_AU.UTF-8 en_US.UTF-8  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -o Dpkg::Options::='--force-confnew' install locales gnupg -y  
  
RUN set \-- junk $LOCALES_DEF \  
shift; \  
for THE_LOCALE in $LOCALES_DEF; do \  
set \-- $(echo $THE_LOCALE | awk -F'.' '{ print $1, $2 }'); \  
INPUT_FILE=$1; \  
CHARMAP_FILE=$2; \  
localedef --no-archive -c -i $INPUT_FILE -f $CHARMAP_FILE $THE_LOCALE; \  
done ; \  
locale-gen  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["/bin/bash"]  

