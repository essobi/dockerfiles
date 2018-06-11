# -------------------------------------------------------------------  
# BASE NODE  
# -------------------------------------------------------------------  
# We need full node as we need git to download from some GitHub repos.  
# -------------------------------------------------------------------  
# We cannot use -alpine straight ahead since we need the git package.  
FROM node:8.4.0 as BASE  
  
WORKDIR /opt/verb  
  
RUN npm install -g verbose/verb#dev stefanwalther/verb-generate-readme#npm-fix  
  
## -------------------------------------------------------------------  
## TEST  
## -------------------------------------------------------------------  
FROM BASE as test  
  
RUN mkdir /opt/verb/test  
COPY ./test /opt/verb/test  
RUN ./test/test-verb.sh  
  
## -------------------------------------------------------------------  
## RELEASE  
## -------------------------------------------------------------------  
FROM node:8.4.0-alpine as RELEASE  
  
RUN apk update  
RUN apk add bash  
  
# Enables colored output  
ENV FORCE_COLOR=true  
  
WORKDIR /opt/verb  
  
# OK, here we have to copy the symbolic link  
# use npm config get prefix to get the node.js prefix
https://stackoverflow.com/questions/18383476/how-to-get-the-npm-global-path-
prefix  
# COPY --from=BASE /usr/local/bin/verb /usr/local/bin/verb  
# Create the symbolic link  
RUN ln -s /usr/local/lib/node_modules/verb/bin/verb.js /usr/local/bin/verb  
  
# Copy the global packages previously being installed  
COPY \--from=BASE /usr/local/lib/node_modules /usr/local/lib/node_modules  
  
CMD ["verb"]  

