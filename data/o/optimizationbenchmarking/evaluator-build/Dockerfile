#  
# optimizationbenchmarking/evaluator-build  
#  
# This is the image of the build tools needed to build the  
# by the elements of the optimizationBenchmarking evaluator.  
# We pre-install several required external dependencies and  
# maven plugins in order to reduce the build time.  
#  
#  
FROM optimizationbenchmarking/evaluator-runtime:0.8.6  
MAINTAINER Thomas Weise <tweise@ustc.edu.cn>  
  
RUN export LANG=C.UTF-8 &&\  
apt-get update &&\  
apt-get install -f -y sudo wget &&\  
cd /tmp/ &&\  
wget "http://raw.githubusercontent.com/optimizationBenchmarking/utils-
build/master/antWebInstallerLinux.sh" &&\  
chmod 755 antWebInstallerLinux.sh &&\  
./antWebInstallerLinux.sh &&\  
rm -f /tmp/antWebInstallerLinux.sh &&\  
apt-get install -f -y maven=3.0.* &&\  
wget http://github.com/optimizationBenchmarking/utils-base/archive/master.zip
&&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd utils-base-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
rm -rf ./src/test/java/examples &&\  
rm -rf ./src/test/java/test &&\  
rm -rf ./src/test/java/shared/junit/org &&\  
echo 'public class Tester { public Tester() { super(); } @org.junit.Test
public void doTest() { } }' > ./src/test/java/Tester.java &&\  
mvn -B clean compile test &&\  
cd /tmp/ &&\  
rm -rf /tmp/utils-math-master &&\  
wget http://github.com/optimizationBenchmarking/utils-math/archive/master.zip
&&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd utils-math-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/utils-math-master &&\  
wget http://github.com/optimizationBenchmarking/utils-
graphics/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd utils-graphics-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/utils-graphics-master &&\  
wget http://github.com/optimizationBenchmarking/utils-
charts/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd utils-charts-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/utils-charts-master &&\  
wget http://github.com/optimizationBenchmarking/utils-
documents/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd utils-documents-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/utils-documents-master &&\  
wget http://github.com/optimizationBenchmarking/utils-ml/archive/master.zip
&&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd utils-ml-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/utils-ml-master &&\  
wget http://github.com/optimizationBenchmarking/evaluator-
base/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd evaluator-base-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/evaluator-base-master &&\  
wget http://github.com/optimizationBenchmarking/evaluator-
attributes/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd evaluator-attributes-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/evaluator-attributes-master &&\  
wget http://github.com/optimizationBenchmarking/evaluator-
modules/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd evaluator-modules-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/evaluator-modules-master &&\  
wget http://github.com/optimizationBenchmarking/evaluator-
evaluator/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd evaluator-evaluator-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/evaluator-evaluator-master &&\  
wget http://github.com/optimizationBenchmarking/documentation-examples-
loader/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd documentation-examples-loader-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/documentation-examples-loader-master &&\  
wget http://github.com/optimizationBenchmarking/evaluator-
gui/archive/master.zip &&\  
unzip master.zip &&\  
rm -f master.zip &&\  
cd evaluator-gui-master &&\  
mvn -Dmaven.javadoc.skip=true -Dmaven.test.skip.exec=true -B clean compile
package install &&\  
cd /tmp/ &&\  
rm -rf /tmp/evaluator-gui-master &&\  
export SUDO_FORCE_REMOVE=yes &&\  
apt-get purge -f -y sudo wget &&\  
apt-get clean &&\  
apt-get autoclean -y &&\  
apt-get autoremove -y &&\  
apt-get clean &&\  
rm -rf /tmp/* /var/tmp/* &&\  
rm -rf /var/lib/apt/lists/* &&\  
rm -f /etc/ssh/ssh_host_*

