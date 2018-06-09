FROM alpine:3.3  
MAINTAINER Stan <teftin@gmail.com>  
  
RUN apk -U add bash openjdk8-jre git-gitweb perl-cgi git  
  
ADD https://www.gerritcodereview.com/download/gerrit-2.12.4.war /  
RUN java -jar /gerrit-2.12.4.war init --batch --no-auto-start \  
\--site-path /gerrit-app \  
\--install-plugin replication \  
\--install-plugin reviewnotes \  
\--install-plugin singleusergroup  
  
ADD https://www.bouncycastle.org/download/bcprov-jdk15on-155.jar /gerrit-
app/lib/  
ADD https://www.bouncycastle.org/download/bcpkix-jdk15on-155.jar /gerrit-
app/lib/  
ADD https://www.bouncycastle.org/download/bcpg-jdk15on-155.jar /gerrit-
app/lib/  
ADD http://repo2.maven.org/maven2/mysql/mysql-connector-java/5.1.39/mysql-
connector-java-5.1.39.jar /gerrit-app/lib/  
  
ADD https://github.com/davido/gerrit-oauth-
provider/releases/download/v2.12.4/gerrit-oauth-provider.jar /gerrit-
app/plugins/  
ADD https://gerrit-ci.gerritforge.com/job/plugin-delete-project-
stable-2.12/lastSuccessfulBuild/artifact/buck-out/gen/plugins/delete-
project/delete-project.jar /gerrit-app/plugins/  
ADD https://gerrit-ci.gerritforge.com/job/plugin-gitiles-
stable-2.12/lastSuccessfulBuild/artifact/buck-
out/gen/plugins/gitiles/gitiles.jar /gerrit-app/plugins/  
  
ADD run.sh /run.sh  
  
VOLUME /gerrit  
  
EXPOSE 8080 29418  
  
CMD exec bash /run.sh  

