FROM silvavlis/kde-runtime:latest  
MAINTAINER Silvano Cirujano Cuesta <silvanociru@gmx.net>  
  
RUN apt-get update && \  
apt-get install -y \  
\--no-install-recommends \  
okular=4:15.08.2-0ubuntu1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV HOME /home/user-ok  
RUN useradd --create-home --home-dir $HOME user-ok && \  
chown -R user-ok:user-ok $HOME  
  
RUN echo "QT_X11_NO_MITSHM=1" >> /etc/environment  
  
USER user-ok  
  
ENV QT_X11_NO_MITSHM=1  
ENTRYPOINT ["/usr/bin/okular"]  
  

