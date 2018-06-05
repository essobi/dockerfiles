FROM opensuse:42.2  
  
# Install build-deps (source-install is way overkill here, oh well)  
RUN zypper -q addrepo obs://windows:mingw:win32/openSUSE_42.2 mingw32 && \  
zypper -q addrepo obs://Emulators/openSUSE_Leap_42.2 Emulators  
# wine depends on samba which depends on krb5 which conflicts with krb5-mini  
RUN zypper -n -q --gpg-auto-import-keys install git make flex tar curl \  
wine -krb5-mini dejagnu autogen && \  
zypper -n -q source-install -d mingw32-cross-gcc-c++  
  
RUN git clone git://github.com/gcc-mirror/gcc --depth=1 -b gcc-6-branch
/opt/gccsrc && \  
cd /opt/gccsrc && curl
https://gist.githubusercontent.com/anonymous/4621fc4aba09827c7bde0e8acb9d2a88/raw/-
| git apply -C2 && \  
git log -1 && rm -rf .git && \  
mkdir -p /opt/gcc6-patched/build && \  
cd /opt/gcc6-patched/build && \  
/opt/gccsrc/configure --prefix=/opt/gcc6-patched/usr \  
\--target=i686-w64-mingw32 --enable-languages="c,c++,fortran,lto,objc,obj-c++"
\  
\--disable-multilib --enable-threads=posix \  
\--with-sysroot=/usr/i686-w64-mingw32/sys-root \  
\--with-as=/usr/bin/i686-w64-mingw32-as && \  
make -j`nproc` > build.log 2>&1 && make check  
# cd .. && rm -rf build && rm -rf /opt/gccsrc  

