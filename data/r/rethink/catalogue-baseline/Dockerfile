FROM rethink/dev-catalogue  
MAINTAINER marc.emmelmann@fokus.fraunhofer.de  
  
#  
# common commands for all catalogue docker images.  
#  
# Attention: do not put the "git clone" command here as cloning the source  
# code outside the final image might cause syncronization issues when using  
# the automated build system of docker hub (docker hub builds all images  
# depending on the repository in parallel and you might build a derived image  
# before the parent image that provides the source code is updated)  
  
RUN apt-get update -y && apt-get install -y maven git default-jre default-jdk
openjdk-7-jre openjdk-7-jdk  
  
  
# The dev-catalogue repository has been made public. Hence, copying selected  
# code at a "parent docker image" is not necessary any more and should in fact  
# be avoided. Instead, the final docker image should directly obtain  
# its required code via git clone.  
#  
# As such, we do not need to move the copyied code into it the final location  
# any more. This image is only kept as a placeholder to demonstrate for
private  
# docker images on how to build the image hierarchy.  
  
# RUN cd /opt/reTHINK && mkdir catalogue  
  
  
  
# Note, we should directly pull from github, but this requires that the repo
becomes publically visible  
# Right now, we include a static snapshot  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-
catalogue/catalogue_broker .  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-
catalogue/catalogue_database .  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-
catalogue/catalogue_objects .  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-
catalogue/catalogue_test .  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-catalogue/model .  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-catalogue/data .  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-catalogue/pom.xml
.  
# RUN cd /opt/reTHINK/catalogue && cp -r ../GitHubRepos/dev-catalogue/ssl .  
  
# RUN cd /opt/reTHINK/catalogue && mvn install  
  
  
ENTRYPOINT ["echo", "This image (rethink/catalogue-baseline) is not intended
to be invoked directly. If you derived your own image, you will need to
specify a docker ENTRYPOINT."]  
  
  

