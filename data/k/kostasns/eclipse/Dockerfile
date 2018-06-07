FROM openjdk:8-jdk  
MAINTAINER Kostas <kostas@nuclearshoebox.com>  
  
#Installing TINI, the PID 1 process for sub-process reaping  
ENV TINI_VERSION v0.10.0  
ENV TINI_SHA1 03e12f4652c4afb252dbb18a305d0c3e6ec1a43d  
  
RUN curl -fsSL
https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini -o
/bin/tini && \  
chmod +x /bin/tini && echo "${TINI_SHA1} /bin/tini" | sha1sum -c -  
  
#Installing eclipse  
ENV ECLIPSE_URL
http://mirror.onet.pl/pub/mirrors/eclipse//technology/epp/downloads/release/luna/SR2/eclipse-
jee-luna-SR2-linux-gtk-x86_64.tar.gz  
ENV ECLIPSE_SHA1 df680622332c69303d23b14afe33281aca774f8e  
ENV ECLIPSE_HOME /eclipse  
  
RUN mkdir -p ${ECLIPSE_HOME} && \  
curl -fsSL ${ECLIPSE_URL} -o /tmp/eclipse.tar.gz && \  
echo "${ECLIPSE_SHA1} /tmp/eclipse.tar.gz" | sha1sum -c - && \  
tar -zxf /tmp/eclipse.tar.gz -C /tmp/ && \  
mv -f /tmp/eclipse/* ${ECLIPSE_HOME} && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/*  
  
ENTRYPOINT ["/bin/tini", "--"]  
CMD ${ECLIPSE_HOME}/eclipse

