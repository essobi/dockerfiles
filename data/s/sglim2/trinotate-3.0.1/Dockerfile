FROM sglim2/centos7  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: trinotate  
# Software Version: 3.0.1  
# Software Website: https://trinotate.github.io  
# Description: Annotation suite designed for automatic functional annotation
of transcriptomes  
##############################################################  
  
ENV APP_NAME=Trinotate  
ENV VERSION=v3.0.1  
ENV GIT=https://github.com/Trinotate/Trinotate.git  
ENV DEST=/software/applications/$APP_NAME/  
ENV PATH=$DEST/$VERSION/:$PATH  
  
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
CMD ["/bin/bash"]  
  

