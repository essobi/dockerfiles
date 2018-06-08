FROM mickaelguene/arm64-debian-dev:jessie  
  
MAINTAINER Mickael Guene <mickael.guene@st.com>  
  
ADD build.sh /build.sh  
RUN ["/usr/bin/umeq-arm64", "-execve", "-0", "bash", "/bin/bash", "-c",
"/build.sh"]  
  
EXPOSE 22  
CMD ["/usr/bin/umeq-arm64", "-execve", "-0", "/usr/sbin/sshd",
"/usr/sbin/sshd", "-D"]  

