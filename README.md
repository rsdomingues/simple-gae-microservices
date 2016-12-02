## simple-gae-microservices
Simple Gae Microservices, with multiple tecnologies. This project is to be used as an example to implement microservices architecture on GAE, with diferente tecnologies as base. This simple example was created on based on the documentation in https://cloud.google.com/appengine/docs/python/microservices-on-app-engine

Actualy this is the app instances:
[instances](https://raw.githubusercontent.com/rsdomingues/simple-gae-microservices/master/microservices-instances.png)

## Local installation
This are the dependencies that must be installed on the local machine:

Google Cloud SDK: https://cloud.google.com/sdk/downloads

after donwload and extract the app, run the following commands:

```console
cd <cloud_sdk_dir>
./google-cloud-sdk/install.sh
./google-cloud-sdk/bin/gcloud init
gcloud components install app-engine-java
gcloud components install app-engine-python
gcloud components install app-engine-go
```

After that you can clone and execute this sample app.

```console
git clone https://github.com/rsdomingues/simple-gae-microservices.git
cd simple-gae-microservices
mvn clean package -f time/pom.xml

dev_appserver.py dispatch/dispatch.yaml front/front.yaml hello/hello.yaml repeat/repeat.yaml time/target/time-1.0-SNAPSHOT
```

Then just open the browser and accesss http://localhost:8080/index.html

[baseapp](https://github.com/rsdomingues/simple-gae-microservices/blob/master/web-page.png?raw=true)

Obs:
 - Google Cloud restrictions must be meet, like JDK 7. 
 - This tutorial was created on mac os plataform, but it should work on any *unix.