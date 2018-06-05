FROM sglim2/centos7  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Software: -  
# Software Version: -  
# Software Website: -  
# Description: Kille group full pipeline of software  
##############################################################  
# MODULES  
RUN yum install -y environment-modules ; \  
grep "^/software/modules/" /usr/share/Modules/init/.modulespath || echo
/software/modules >> /usr/share/Modules/init/.modulespath ; \  
. /etc/profile.d/modules.sh  
  
# SAMTOOLS 1.1  
ENV APP_NAME=samtools  
ENV VERSION=1.1  
ENV GIT=https://github.com/BenLangmead/samtools.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
RUN yum install -y zlib-devel \  
ncurses-devel ; \  
curl -L -o htslib-1.1.tar.gz
https://github.com/samtools/htslib/archive/1.1.tar.gz ; \  
curl -L -o samtools-1.1.tar.gz
https://github.com/samtools/samtools/archive/1.1.tar.gz ; \  
tar xzf htslib-1.1.tar.gz ; \  
tar xzf samtools-1.1.tar.gz ; \  
rm -rf htslib-1.1.tar.gz ; \  
rm -rf samtools-1.1.tar.gz ; \  
mv htslib-1.1 htslib ; \  
cd samtools-1.1 ; \  
make -j HTSDIR=../htslib ; \  
make prefix=$DEST/$VERSION install ; \  
cd ../ ; \  
rm -rf htslib samtools-1.1  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
# BOWTIE 2.2.9  
ENV APP_NAME=bowtie2  
ENV VERSION=v2.2.9  
ENV GIT=https://github.com/BenLangmead/bowtie2.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
RUN git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
make -j ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
mv $APP_NAME $DEST/$VERSION  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
# BOWTIE 1.1.1  
ENV APP_NAME=bowtie  
ENV VERSION=v1.1.1  
ENV GIT=https://github.com/BenLangmead/bowtie.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
ENV BOWTIE_INDEXES=$DEST/$VERSION/indexes  
RUN git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
make -j ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
mv $APP_NAME $DEST/$VERSION  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
# BOWTIE 1.1.2  
ENV APP_NAME=bowtie  
ENV VERSION=v1.1.2  
ENV GIT=https://github.com/BenLangmead/bowtie.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
ENV BOWTIE_INDEXES=$DEST/$VERSION/indexes  
RUN git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
make -j ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
mv $APP_NAME $DEST/$VERSION  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
# TRIMMOMATIC 0.36  
ENV APP_NAME=trimmomatic  
ENV VERSION=0.36  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
RUN yum install -y \  
java \  
unzip ; \  
curl -L -o Trimmomatic-0.36.zip \  
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
; \  
unzip Trimmomatic-0.36.zip ; \  
mkdir -p $DEST ; \  
mv Trimmomatic-0.36 $DEST/$VERSION ; \  
rm -rf Trimmomatic-0.36.zip  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
# TRINITYRNASEQ 2.2.0  
ENV APP_NAME=trinityrnaseq  
ENV VERSION=v2.2.0  
ENV GIT=https://github.com/trinityrnaseq/trinityrnaseq.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
RUN yum install -y bzip2 ; \  
git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
make -j ; \  
make trinity_essentials ; \  
make plugins ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
cd ../ ; \  
mv $APP_NAME $DEST/$VERSION  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
# TRINOTATE 3.0.1  
ENV APP_NAME=Trinotate  
ENV VERSION=v3.0.1  
ENV GIT=https://github.com/Trinotate/Trinotate.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV MOD_DEST=/software/modules/$APP_NAME/  
RUN yum install -y \  
lighttpd \  
perl-CGI \  
perl-DBI \  
perl-DBD-SQLite \  
perl-HTML-Template \  
perl-URI \  
; \  
git clone $GIT ; \  
cd $APP_NAME ; \  
git checkout tags/$VERSION ; \  
mkdir -p /usr/share/licenses/$APP_NAME-$VERSION ; \  
cp LICENSE.txt /usr/share/licenses/$APP_NAME-$VERSION/ ; \  
cd ../ ; \  
mkdir -p $DEST ; \  
mv $APP_NAME $DEST/$VERSION  
COPY $APP_NAME-$VERSION.module $MOD_DEST/$VERSION  
  
CMD ["/bin/bash"]  

