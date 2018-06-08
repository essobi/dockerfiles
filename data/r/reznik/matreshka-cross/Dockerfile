FROM fedora:24  
RUN dnf install --assumeyes dnf-plugins-core &&\  
dnf config-manager --add-repo http://download.opensuse.org/repositories\  
/home:reznik/Fedora_24/home:reznik.repo &&\  
dnf --assumeyes install make gcc-gnat gprbuild bitten-slave svn valgrind\  
mingw32-gcc-gnat mingw64-gcc-gnat &&\  
dnf clean all  

