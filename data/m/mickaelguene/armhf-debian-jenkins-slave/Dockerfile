FROM mickaelguene/armhf-debian-dev:testing  
  
MAINTAINER Mickael Guene <mickael.guene@st.com>  
  
ADD build.sh /build.sh  
RUN ["/usr/bin/umeq-arm", "-execve", "-0", "bash", "/bin/bash", "-c",
"/build.sh"]  
  
EXPOSE 22  
CMD ["/usr/bin/umeq-arm", "-execve", "-0", "/usr/sbin/sshd", "/usr/sbin/sshd",
"-D"]  

