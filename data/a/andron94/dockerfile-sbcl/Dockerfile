FROM alpine:3.7  
MAINTAINER Andrii Tymchuk <makedonsky94@gmail.com>  
  
# ================================ Install SBCL
================================  
# 1. SBCL compilation requires another Common Lisp implementation.  
# I found only 'sbcl' and 'clisp' packages  
# on testing branch of Alpine edge repository.  
ENV ALPINE_EDGE_REPOSITORY http://dl-4.alpinelinux.org/alpine/edge/testing  
  
# 2. Convenient definitions.  
ENV SBCL_VERSION 1.4.5  
ENV SBCL_DIR sbcl  
  
ENV ALPINE_REPOSITORIES /etc/apk/repositories  
  
# 3. Official SBCL sources don't compile under Musl.  
# I will use my own repository with fixes.  
ENV SBCL_URL https://github.com/andron94/sbcl  
  
ENV SBCL_RELEASE ${SBCL_DIR}-${SBCL_VERSION}-musl  
  
# 4. 'sb-bsd-sockets' contribution requires 'NETDB_INTERNAL'  
# and 'NETDB_SUCCESS' macros which Musl doesn't define.  
# This patch will fix the issue.  
ENV NETDB_PATCH "\n#define NETDB_INTERNAL -1\n#define NETDB_SUCCESS 0"  
# 5. Installation:  
# 1. Backup Alpine repositories.  
# 2. Add Alpine edge repository.  
# 3. Update package list.  
# 4. Install build dependencies:  
# 1. Necessary libraries: linux-headers, musl-dev;  
# 2. Compilers and build tool: gcc, sbcl and make;  
# 3. Download tool: git.  
# 5. Apply 'netdb' patch.  
# 6. Create and move to temp directory which will be used for the build.  
# 7. Download and move to SBCL sources.  
# 8. Choose correct SBCL version.  
# 9. Configure and install SBCL.  
# 10. Remove unnecessary SBCL documentation files.  
# 11. Remove unnecessary SBCL sources.  
# 12. Remove unnecessary build dependencies.  
# 13. Restore Alpine repositories.  
# 14. Clean package list.  
RUN cp ${ALPINE_REPOSITORIES} ${ALPINE_REPOSITORIES}.backup &&\  
echo ${ALPINE_EDGE_REPOSITORY} >> ${ALPINE_REPOSITORIES} &&\  
apk update &&\  
apk add --no-cache --virtual build-deps \  
linux-headers \  
musl-dev \  
gcc \  
make \  
sbcl \  
git &&\  
sed -i "s/.*OVERFLOW.*/&\n${NETDB_PATCH}/" /usr/include/netdb.h &&\  
mkdir /home/temp && cd /home/temp &&\  
git clone ${SBCL_URL} && cd ${SBCL_DIR} &&\  
git checkout ${SBCL_RELEASE} &&\  
sh make.sh && sh install.sh &&\  
rm -fr /usr/local/share/* &&\  
cd /home && rm -rf temp &&\  
apk del build-deps &&\  
cp ${ALPINE_REPOSITORIES}.backup ${ALPINE_REPOSITORIES} &&\  
rm ${ALPINE_REPOSITORIES}.backup &&\  
rm -fr /var/cache/apk/*  
  
#
==============================================================================  
CMD ["sbcl"]  

