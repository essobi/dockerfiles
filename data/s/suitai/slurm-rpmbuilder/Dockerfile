FROM centos  
MAINTAINER suitai <suitai@outlook.jp>  
# environment variables  
ENV URL git://github.com/SchedMD/slurm.git  
ENV DIR slurm  
# update  
RUN yum update -y  
RUN yum install -y epel-release  
# install  
RUN yum install -y git gcc make rpm-build \  
readline-devel openssl openssl-devel perl-ExtUtils-MakeMaker munge-devel
munge-libs pam-devel  
# git clone  
RUN useradd -m rpmbuilder  
USER rpmbuilder  
WORKDIR /home/rpmbuilder  
RUN git clone $URL  
# edit spec file  
RUN NAME=`perl -na -e '/Name:/ and print $F[1]' $DIR/META` && \  
VERSION=`perl -na -e '/Version:/ and print $F[1]' $DIR/META` && \  
RELEASE=`perl -na -e '/Release:/ and print $F[1]' $DIR/META` && \  
perl -pi -e "s/^Name: see META file/Name: $NAME/g" $DIR/$NAME.spec && \  
perl -pi -e "s/^Version: see META file/Version: $VERSION/g" $DIR/$NAME.spec &&
\  
perl -pi -e "s/^Release: see META file/Release: $RELEASE/g" $DIR/$NAME.spec &&
\  
mv $DIR $NAME-$VERSION-$RELEASE && \  
tar zcf $NAME-$VERSION-$RELEASE.tgz $NAME-$VERSION-$RELEASE  
RUN mkdir -p rpmbuild/RPMS/  
VOLUME /home/rpmbuilder/rpmbuild/RPMS  
CMD rpmbuild -ta $DIR*.tgz  

