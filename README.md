### Hello

This is my solution for the interview task. 

Please note that I don't put any company name or actual details into this file on purpose as I'd like to give a chance to other candidates to go through on all subtasks and not use my configs etc. That would kill the fun, right?

This steps below are *not* written in a spoon-feeding style and contains only the high level steps of reproducing my work in (hopefully) any environment.

Just for the record I used Arch Linux.

I tried to keep the deployment as simple as I could but I'm sure there a lot of room for improvement.

Anyway, before starting make sure **docker** and **minikube** are installed, configured and started properly.

## Clone this repo
```
git clone https://github.com/nexusblink9k/task42

```

## Set docker to point to minikube 
```
eval $(minikube docker-env)
```

## Build the flask app via docker
```
docker build -t flask-app app/.
```

## Deploy configs and services
 
Except nginx, we do that later

```
for configfiles in $(ls config/*.yml); do minikube kubectl -- apply -f $configfiles; done
for deployfiles in $(ls deploy/*.yml | grep -v nginx); do minikube kubectl -- apply -f $deployfiles; done
```

## Wait until everything starts
eg. Check them by running these commands below
```
minikube kubectl -- get svc
minikube kubectl -- get pod
minikube service list
```

## Test flash app in browser
Get the url by running
```
minikube service app-service 
```

## Check grafana in browser
Login with ***admin:deadbeef (I know plain text password in a README.md file is not so clever, but it is in the config file too)

```
 minikube service grafana-service 
```

## Create new datasource as requested
Visualise it on a chart eg. *sum(kube_pod_container_status_running{namespace!="kube-system"})*

![grafana](/screenshots/grafana.png)

## Deploy nginx
With 15 replicas by default
```
minikube kubectl -- apply -f deploy/nginx-deploy.yml
```

## Wait, check if the alert is triggered by prometheus alertmanager
![prometheus](/screenshots/prometheus_alert.png)
![alertmanager](/screenshots/alertmanager_alert.png)

## Check the flash app logs
You might want to know if /alert is hit by the alertmanager, also check counter increased on the flask app, etc...

## Scale down nginx
```
minikube kubectl -- scale deployment nginx --replicas 3
```

## Check dashboard again, counter on the flask app, etc...


