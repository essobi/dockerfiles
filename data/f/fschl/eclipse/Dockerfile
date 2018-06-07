FROM java:8  
MAINTAINER Frieder Schlesier <fschl.code@gmail.com>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
openjfx \  
ssh \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV ECLIPSE_SHA512
3ebeaab354116aba06d08ccb2df81bfb148ddc3c145b53ac0c5f9fffe15e45e5ede1bac37acc9381b239d19dd766bb86c5e1122e02628e47ca1181a9178cb4ef  
  
RUN wget http://ftp.halifax.rwth-
aachen.de/eclipse//technology/epp/downloads/release/mars/1/eclipse-java-
mars-1-linux-gtk-x86_64.tar.gz -O /tmp/eclipse.tar.gz -q \  
&& echo "$ECLIPSE_SHA512 /tmp/eclipse.tar.gz" | sha512sum -c - \  
&& echo 'Installing eclipse' \  
&& tar -xf /tmp/eclipse.tar.gz -C /opt \  
&& rm /tmp/eclipse.tar.gz  
  
ENV INSTALL_DIR /usr/local/bin  
  
ADD run $INSTALL_DIR/eclipse  
RUN chmod +x $INSTALL_DIR/eclipse  
  
RUN adduser --disabled-password --quiet --gecos '' eclipse \  
&& chown -R root:eclipse $INSTALL_DIR/eclipse \  
&& chmod -R 775 $INSTALL_DIR/eclipse  
  
USER eclipse  
WORKDIR /home/eclipse/workspace  
  
CMD ["/usr/local/bin/eclipse"]  

