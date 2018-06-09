FROM fedora:25  
LABEL maintainer="Tonnerre LOMBARD <tonnerre@ancient-solutions.com>"  
  
RUN ["/usr/bin/rpm", "-iv", "http://rpm.ancient-
solutions.com/ancientsolutions-release-25-1.fc25.noarch.rpm"]  
RUN ["/usr/bin/dnf", "install", "-y", "rpm-build", "rpm-sign", "createrepo",
"fakeroot"]  
RUN ["/usr/bin/dnf", "install", "-y", "@development-tools", "fedora-packager"]  
RUN ["/usr/sbin/groupadd", "-g", "1000", "builder"]  
RUN ["/usr/sbin/useradd", "-c", "build user", "-d", "/build", "-g", "1000",
"-M", "-N", "-u", "1000", "builder"]  
COPY run-build.sh /usr/local/bin/run-build.sh  
  
VOLUME ["/build"]  
WORKDIR "/build"  
USER root  
ENTRYPOINT ["/bin/sh", "-x", "/usr/local/bin/run-build.sh"]  

