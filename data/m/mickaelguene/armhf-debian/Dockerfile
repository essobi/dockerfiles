FROM scratch  
MAINTAINER Mickael Guene <mickael.guene@st.com>  
  
ADD armhf-debian-testing.tgz /  
ADD configure.sh /configure.sh  
RUN ["/usr/bin/umeq-arm", "-execve", "-0", "bash", "/bin/bash", "-c",
"/configure.sh"]  
  
CMD ["/usr/bin/umeq-arm", "-execve", "-0", "bash", "/bin/bash"]  

