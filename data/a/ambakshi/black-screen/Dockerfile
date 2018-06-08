FROM node:latest  
MAINTAINER Amit Bakshi <ambakshi@gmail.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update -y && apt-get
install -y notify-osd libgtk2.0-dev libgtk2.0-cil curl x11-apps xvfb openssh-
server libgconf2-dev libgconf2.0-cil-dev libnss3 ruby-notify libasound2  
RUN curl -sSL https://github.com/just-
containers/s6-overlay/releases/download/v1.14.0.4/s6-overlay-amd64.tar.gz |
tar zxf - -C /  
RUN rm -rf /usr/src && useradd -m -s /bin/bash -d /usr/src user  
USER user  
RUN git clone https://github.com/black-screen/black-screen /usr/src/black-
screen  
WORKDIR /usr/src/black-screen  
RUN npm install  
### Dont modify above!  
USER root  
WORKDIR /  
RUN mkdir -m 0700 -p /usr/src/.ssh  
ADD ./id_bs.pub /usr/src/.ssh/authorized_keys  
RUN chmod 0400 /usr/src/.ssh/authorized_keys && mkdir -p -m 0700 /var/run/sshd
&& chown -R user:user /usr/src/.ssh  
#RUN mkdir -p /etc/services.d/sshd && mkdir -p -m 0700 /var/run/sshd && printf
'%s\n%s\n' '#!/usr/bin/execlineb -P' '/usr/sbin/sshd -De' >
/etc/services.d/sshd/run && chmod +x /etc/services.d/sshd/run  
EXPOSE 22  
ENTRYPOINT ["/init"]  
CMD ["/usr/sbin/sshd","-D","-e"]  
  

