FROM vuminhtuan/tomcat  
  
ENV CRM_HOME /work  
RUN mkdir -p "$CRM_HOME"  
WORKDIR $CRM_HOME  
  
# Get the source code from Github  
RUN \  
git clone https://github.com/axelor/axelor-development-kit.git -b master
$CRM_HOME/axelor-development-kit && \  
git clone https://github.com/axelor/abs-webapp.git -b master $CRM_HOME/abs-
webapp && \  
git clone https://github.com/axelor/axelor-business-suite.git -b master
$CRM_HOME/abs-webapp/modules/abs  
# Delete unused modules  
RUN \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-account && \  
# rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-admin && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-bank-payment && \  
# rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-base && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-business-production && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-business-project && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-cash-management && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-client-portal && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-contract && \  
# rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-crm && \  
# rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-exception && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-fleet && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-helpdesk && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-human-resource && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-marketing && \  
# rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-message && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-production && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-project && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-purchase && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-quality && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-sale && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-stock && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-studio && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-supplier-management && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-supplychain && \  
rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-talent  
# rm -rf $CRM_HOME/abs-webapp/modules/abs/axelor-tool && \  
  
COPY ./axelor-development-kit $CRM_HOME/axelor-development-kit  
COPY ./abs-webapp $CRM_HOME/abs-webapp  
COPY ./.m2 /root/.m2  
  
RUN \  
rm $CATALINA_HOME/webapps/* -R && \  
cd $CRM_HOME/axelor-development-kit && ./gradlew clean publishToMavenLocal
--no-daemon -x test && \  
cd $CRM_HOME/abs-webapp && ./gradlew clean build --no-daemon -x test && \  
cp $CRM_HOME/abs-webapp/build/libs/*.war $CATALINA_HOME/webapps/ROOT.war  

